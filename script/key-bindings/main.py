import collections
import json
import os
import pathlib
import re

import commentjson
import pandas

SCRIPT = pathlib.Path(__file__)

KEY_BINDINGS_SCRIPT_DIRECTORY = SCRIPT.parent
SCRIPT_DIRECTORY = KEY_BINDINGS_SCRIPT_DIRECTORY.parent
DOCS_ROOT = SCRIPT_DIRECTORY.parent

SOUCE_DIRECTORY = KEY_BINDINGS_SCRIPT_DIRECTORY / "source"

KEY_BINDINGS_TEMPLATE = SOUCE_DIRECTORY / "key-bindings-template.md"
DEFAULT_KEY_BINDINGS = SOUCE_DIRECTORY / "default.json"

KEY_BINDINGS_DOCUMENT = DOCS_ROOT / "configuration" / "key-bindings.md"

KEY_NAME_MAP = {
    "cmd": "command",
    "ctrl": "control",
    "pageup": "page up",
    "pagedown": "page down",
    "-": " + ",
    " ": ", ",
}

# This information isn't available in the default.json keymap, but the control codes are.  This map is used to bridge that gap.
# Maybe we can find a way to add this information to the default.json keymap, for consistency, then we can remove code here related to this map.
TERMINAL_CONTROL_CODE_MAP = {
    "\u0001": "terminal::MoveToBeginningOfLine",
    "\u0005": "terminal::MoveToEndOfLine",
    "\u0015": "terminal::DeleteLine",
    "\u001bb": "terminal::MoveToPreviousWordStart",
    "\u001bf": "terminal::MoveToNextWordEnd",
}

# TODO: Add Following to the default.json file?
# Add activate tab


# Missing
# | Toggle contacts panel focus | `Command + Shift + C`       |
# Lose descriptions on open pane 1, 2, 3
# Some items moved around, as they were in the wrong spot, so if something looks like it went away, check for it elsewhere in the file
# Somethings changed for the worse "Backtab" -> Tab prev... this just means we need to adjust the naming of these in Zed to match what we want to see in docs
# Open up issue for terminal commands

def main():
    with open(DEFAULT_KEY_BINDINGS, "r") as keymap_file:
        keymap_data = commentjson.load(keymap_file)

    markdown_data = get_markdown_data(keymap_data)

    with open(KEY_BINDINGS_TEMPLATE, "r") as key_bindings_document:
        markdown_content = key_bindings_document.read()

    for context, column_data in markdown_data.items():
        data = {"**Command**": column_data["commands"], "**Target**": column_data["targets"], "**Default Shortcut**": column_data["shortcuts"]}
        dataframe = pandas.DataFrame(data).sort_values(by=["**Command**", "**Default Shortcut**"])
        markdown_table = dataframe.to_markdown(tablefmt="github", index=False)

        marker = "_".join(context.lower().split())
        marker = f"insert_{marker}_bindings"

        markdown_content = markdown_content.replace(marker, markdown_table)

    with open(KEY_BINDINGS_DOCUMENT, "w") as key_bindings_document:
        key_bindings_document.write(markdown_content)


def get_markdown_data(keymap_data):
    markdown_data = collections.defaultdict(lambda: collections.defaultdict(list))

    for binding_dictionary in keymap_data:
        context = binding_dictionary.get("context", "Global")

        for operator in ("&&", ">"):
            if operator in context:
                context = context.split(operator)[0].strip()

        context = camel_case_to_readable(context)

        commands = []
        targets = []
        shortcuts = []

        for shortcut, command in binding_dictionary["bindings"].items():
            result = get_readable_command_and_target(command, context)

            if result is None:
                continue

            readable_command, readable_target = result
            readable_shortcut = get_readable_shortcut(shortcut)

            commands.append(readable_command)
            targets.append(readable_target)
            shortcuts.append(f"`{readable_shortcut}`")

        markdown_data[context]["commands"] += commands
        markdown_data[context]["targets"] += targets
        markdown_data[context]["shortcuts"] += shortcuts

    return markdown_data


def get_readable_command_and_target(command, context):
    if isinstance(command, list):
        # In place of some commands, are lists that contain the command and additional information
        # See `Workspace -> cmd-1` or `Terminal -> cmd-right` for examples
        command, misc_text = command

        # Special cases for terminal
        if context == "Terminal":
            if command == "terminal::SendText":
                command = TERMINAL_CONTROL_CODE_MAP[misc_text]
            elif command == "terminal::SendKeystroke":
                return None

    readable_target, readable_command = command.split("::")
    readable_target = snake_case_to_readable(readable_target).title()

    readable_command = camel_case_to_readable(readable_command)
    readable_command = readable_command.lower().capitalize()

    return readable_command, readable_target


def get_readable_shortcut(shortcut):
    shortcut_components = re.split("(-|\s)+", shortcut)
    readable_shortcut_components = [KEY_NAME_MAP.get(component, component).title() for component in shortcut_components]
    readable_shortcut = "".join(readable_shortcut_components)

    return readable_shortcut


def camel_case_to_readable(text):
    return "".join([" " + character if character.isupper() else character for character in text]).strip()


def snake_case_to_readable(text):
    return " ".join(text.split("_"))


if __name__ == "__main__":
    main()