import collections
import textwrap

from ward import test

from main import (
    camel_case_to_readable,
    get_markdown_column_data,
    get_markdown_table,
    get_markdown_tables,
    get_readable_command_and_target,
    get_readable_shortcut,
    parse_context_string,
    snake_case_to_readable,
)


@test("test snake_case_to_readable")
def _():
    assert snake_case_to_readable("project_panel") == "project panel"


@test("test camel_case_to_readable")
def _():
    assert camel_case_to_readable("ResetBufferFontSize") == "reset buffer font size"


@test("test parse_context_string")
def _():
    assert parse_context_string("Editor") == [
        {"name": "Editor", "bools": [], "mode": None}
    ]
    # We aren't outputting anything in the script for this case
    assert parse_context_string("Editor && renaming") == [
        {"name": "Editor", "bools": ["renaming"], "mode": None}
    ]
    assert parse_context_string("Editor && mode == full") == [
        {"name": "Editor", "bools": [], "mode": "full"}
    ]
    # We aren't outputting anything in the script for this case, it may not make
    # any sense for it to be this way.
    assert parse_context_string("ConversationEditor > Editor") == [
        {
            "name": "ConversationEditor",
            "bools": [],
            "mode": None,
        },
        {"name": "Editor", "bools": [], "mode": None},
    ]


@test("test get_readable_shortcut")
def _():
    assert get_readable_shortcut("ctrl-shift-e") == "Control + Shift + E"
    assert get_readable_shortcut("cmd-k cmd-right") == "Command + K, Command + Right"


@test("test get_readable_command_and_target")
def _():
    assert get_readable_command_and_target(
        "editor::DeleteToPreviousWordStart", "Editor"
    ) == ("Delete to previous word start", "Editor")
    assert get_readable_command_and_target(
        "editor::DeleteToPreviousWordStart", "Workspace"
    ) == ("Delete to previous word start", "Editor")


@test("test get_readable_command_and_target for special cases")
def _():
    assert get_readable_command_and_target(
        ["terminal::SendText", "\u0001"], "terminal"
    ) == ("Move to beginning of line", "Terminal")
    assert (
        get_readable_command_and_target(
            ["terminal::SendKeystroke", "ctrl-c"], "terminal"
        )
        == None
    )

    assert get_readable_command_and_target(["pane::ActivateItem", 0], "pane") == (
        "Activate item 1",
        "Pane",
    )
    assert get_readable_command_and_target(
        ["workspace::ActivatePane", 0], "workspace"
    ) == ("Activate pane 1", "Workspace")

    assert get_readable_command_and_target(["workspace::ActivatePaneInDirection", "Left"], "pane") == (
        "Activate pane in direction left",
        "Workspace",
    )


@test("test get_markdown_column_data")
def _():
    keymap_data = [
        {
            "context": "Editor",
            "bindings": {
                "ctrl-k": "editor::CutToEndOfLine",
                "ctrl-t": "editor::Transpose",
                "cmd-backspace": "editor::DeleteToBeginningOfLine",
            },
        }
    ]

    markdown_data = {
        "editor": {
            "commands": [
                "Cut to end of line",
                "Transpose",
                "Delete to beginning of line",
            ],
            "targets": ["Editor", "Editor", "Editor"],
            "shortcuts": ["`Control + K`", "`Control + T`", "`Command + Backspace`"],
        }
    }

    assert get_markdown_column_data(keymap_data) == markdown_data


@test("test get_markdown_column_data for special cases")
def _():
    keymap_data = [
        {
            "bindings": {"ctrl-`": "workspace::NewTerminal"},
        }
    ]

    markdown_data = {
        "global": {
            "commands": ["New terminal"],
            "targets": ["Workspace"],
            "shortcuts": ["``Control + ` ``"],
        }
    }

    assert get_markdown_column_data(keymap_data) == markdown_data


@test("test get_markdown_tables")
def _():
    keymap_data = [
        {
            "bindings": {
                "pagedown": "menu::SelectLast",
                "shift-pagedown": "menu::SelectFirst",
                "down": "menu::SelectNext",
            }
        },
        {
            "context": "Editor",
            "bindings": {
                "ctrl-l": "editor::NextScreen",
                "ctrl-f": "editor::MoveRight",
                "alt-left": "editor::MoveToPreviousWordStart",
            },
        },
        {
            "context": "Editor && mode == full",
            "bindings": {
                "cmd-shift-o": "outline::Toggle",
                "ctrl-g": "go_to_line::Toggle",
            },
        },
        {
            "context": "Pane",
            "bindings": {
                "ctrl--": "pane::GoBack",
                "ctrl-_": "pane::GoForward",
                "ctrl-0": "pane::ActivateLastItem",
            },
        },
    ]

    global_markdown_table = """
        | **Command**   | **Target**   | **Default Shortcut**   |
        |---------------|--------------|------------------------|
        | Select first  | Menu         | `Shift + Page Down`    |
        | Select last   | Menu         | `Page Down`            |
        | Select next   | Menu         | `Down`                 |
    """

    editor_markdown_table = """
        | **Command**                 | **Target**   | **Default Shortcut**   |
        |-----------------------------|--------------|------------------------|
        | Move right                  | Editor       | `Control + F`          |
        | Move to previous word start | Editor       | `Alt + Left`           |
        | Next screen                 | Editor       | `Control + L`          |
    """

    full_editor_markdown_table = """
        | **Command**   | **Target**   | **Default Shortcut**   |
        |---------------|--------------|------------------------|
        | Toggle        | Go To Line   | `Control + G`          |
        | Toggle        | Outline      | `Command + Shift + O`  |
    """

    pane_markdown_table = """
        | **Command**        | **Target**   | **Default Shortcut**   |
        |--------------------|--------------|------------------------|
        | Activate last item | Pane         | `Control + 0`          |
        | Go back            | Pane         | `Control + `           |
        | Go forward         | Pane         | `Control + _`          |
    """

    markdown_tables = {
        "{{ global_bindings }}": textwrap.dedent(global_markdown_table).strip(),
        "{{ editor_bindings }}": textwrap.dedent(editor_markdown_table).strip(),
        "{{ full_editor_bindings }}": textwrap.dedent(
            full_editor_markdown_table
        ).strip(),
        "{{ pane_bindings }}": textwrap.dedent(pane_markdown_table).strip(),
    }

    assert get_markdown_tables(keymap_data) == markdown_tables
