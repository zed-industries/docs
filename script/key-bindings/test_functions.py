import collections
import textwrap

from ward import test

from main import (
    create_markdown_table,
    get_readable_command_and_target,
    get_markdown_data,
    camel_case_to_readable,
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


@test("test create_markdown_table")
def _():
    column_data = {
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

    markdown_table = """
        | **Command**                 | **Target**   | **Default Shortcut**   |
        |-----------------------------|--------------|------------------------|
        | Cut to end of line          | Editor       | `Control + K`          |
        | Delete to beginning of line | Editor       | `Command + Backspace`  |
        | Transpose                   | Editor       | `Control + T`          |
    """

    assert create_markdown_table(column_data) == textwrap.dedent(markdown_table).strip()
