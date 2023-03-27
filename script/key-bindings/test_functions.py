import collections
import textwrap

from ward import test

from main import (
    camel_case_to_readable,
    get_markdown_data,
    get_markdown_table,
    get_markdown_tables,
    get_readable_command_and_target,
    get_readable_shortcut,
    snake_case_to_readable
)

@test("test snake_case_to_readable")
def _():
    assert snake_case_to_readable("project_panel") == "project panel"


@test("test camel_case_to_readable")
def _():
    assert camel_case_to_readable("ResetBufferFontSize") == "reset buffer font size"


@test("test get_readable_shortcut")
def _():
    assert get_readable_shortcut("ctrl-shift-e") == "Control + Shift + E"
    assert get_readable_shortcut("cmd-k cmd-right") == "Command + K, Command + Right"


@test("test get_readable_command_and_target")
def _():
    assert get_readable_command_and_target("editor::DeleteToPreviousWordStart", "Editor") == ("Delete to previous word start", "Editor")
    assert get_readable_command_and_target("editor::DeleteToPreviousWordStart", "Workspace") == ("Delete to previous word start", "Editor")


@test("test get_readable_command_and_target for special terminal cases")
def _():
    assert get_readable_command_and_target(["terminal::SendText", "\u0001"], "terminal") == ("Move to beginning of line", "Terminal")
    assert get_readable_command_and_target(["terminal::SendKeystroke", "ctrl-c"], "terminal") == None


@test("test get_markdown_data")
def _():
    keymap_data = [
        {
            "context": "Editor",
            "bindings": {
                "ctrl-k": "editor::CutToEndOfLine",
                "ctrl-t": "editor::Transpose",
                "cmd-backspace": "editor::DeleteToBeginningOfLine",
            }
        }
    ]

    markdown_data = {
        "editor": {
            "commands": [
                "Cut to end of line",
                "Transpose",
                "Delete to beginning of line"
            ],
            "targets": [
                "Editor",
                "Editor",
                "Editor"
            ],
            "shortcuts": [
                "`Control + K`",
                "`Control + T`",
                "`Command + Backspace`"
            ],
        }
    }
    assert get_markdown_data(keymap_data) == markdown_data


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
            }
        },
        {
            "context": "Pane",
            "bindings": {
                "ctrl--": "pane::GoBack",
                "ctrl-_": "pane::GoForward",
                "ctrl-0": "pane::ActivateLastItem",
            }
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

    pane_markdown_table = """
        | **Command**        | **Target**   | **Default Shortcut**   |
        |--------------------|--------------|------------------------|
        | Activate last item | Pane         | `Control + 0`          |
        | Go back            | Pane         | `Control + `           |
        | Go forward         | Pane         | `Control + _`          |
    """

    markdown_tables = {
        "insert_global_bindings": textwrap.dedent(global_markdown_table).strip(),
        "insert_editor_bindings": textwrap.dedent(editor_markdown_table).strip(),
        "insert_pane_bindings": textwrap.dedent(pane_markdown_table).strip(),
    }

    assert get_markdown_tables(keymap_data) == markdown_tables
