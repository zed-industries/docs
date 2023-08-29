import collections
import pathlib
import re

import commentjson
import pandas

SCRIPT = pathlib.Path(__file__)
KEY_BINDINGS_SCRIPT_DIRECTORY = SCRIPT.parent
SCRIPT_DIRECTORY = KEY_BINDINGS_SCRIPT_DIRECTORY.parent
DOCS_ROOT_DIRECTORY = SCRIPT_DIRECTORY.parent

KEY_BINDINGS_DOCUMENT = DOCS_ROOT_DIRECTORY / "configuration" / "key-bindings.md"
SOURCE_DIRECTORY = KEY_BINDINGS_SCRIPT_DIRECTORY / "source"
KEY_BINDINGS_TEMPLATE = SOURCE_DIRECTORY / "key-bindings-template.md"
DEFAULT_KEY_BINDINGS = SOURCE_DIRECTORY / "default.json"

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


def main():
    with open(DEFAULT_KEY_BINDINGS, "r") as keymap_file:
        keymap_data = commentjson.load(keymap_file)

    markdown_tables = get_markdown_tables(keymap_data)

    with open(KEY_BINDINGS_TEMPLATE, "r") as key_bindings_document:
        markdown_content = key_bindings_document.read()

    for marker, markdown_table in markdown_tables.items():
        markdown_content = markdown_content.replace(marker, markdown_table)

    with open(KEY_BINDINGS_DOCUMENT, "w") as key_bindings_document:
        key_bindings_document.write(markdown_content)


def get_markdown_tables(keymap_data):
    markdown_column_data = get_markdown_column_data(keymap_data)
    markdown_tables = {}

    for context, column_data in markdown_column_data.items():
        markdown_table = get_markdown_table(column_data)

        marker = "_".join(context.split())
        marker = f"{{{{ {marker}_bindings }}}}"

        markdown_tables[marker] = markdown_table

    return markdown_tables


def get_markdown_table(column_data):
    command_column_name = "**Command**"
    target_column_name = "**Target**"
    shortcut_column_name = "**Default Shortcut**"

    data = {
        command_column_name: column_data["commands"],
        target_column_name: column_data["targets"],
        shortcut_column_name: column_data["shortcuts"],
    }

    data_frame = pandas.DataFrame(data).sort_values(
        by=[target_column_name, command_column_name, shortcut_column_name]
    )

    return data_frame.to_markdown(tablefmt="github", index=False)


def get_markdown_column_data(keymap_data):
    markdown_data = collections.defaultdict(lambda: collections.defaultdict(list))

    for binding_dictionary in keymap_data:
        context_string: str = binding_dictionary.get("context", "Global")
        context_list = parse_context_string(context_string)

        if not context_list:
            continue

        # We don't currently don't use anything, but the first item in the list
        context_dictionary = context_list[0]
        context_name = context_dictionary["name"]
        context_name = camel_case_to_readable(context_dictionary["name"])
        mode = context_dictionary.get("mode", None)

        if mode:
            context_name = f"{mode}_{context_name}"

        for shortcut, command in binding_dictionary["bindings"].items():
            result = get_readable_command_and_target(command, context_name)

            if result is None:
                continue

            readable_command, readable_target = result
            readable_shortcut = get_readable_shortcut(shortcut)

            markdown_data[context_name]["commands"].append(readable_command)
            markdown_data[context_name]["targets"].append(readable_target)

            # Special case for shortcuts that end in backticks
            # Unfortunately, these will render with an extra trailing space on GitHub.com
            if readable_shortcut.endswith("`"):
                markdown_data[context_name]["shortcuts"].append(
                    f"``{readable_shortcut} ``"
                )
            else:
                markdown_data[context_name]["shortcuts"].append(
                    f"`{readable_shortcut}`"
                )

    return markdown_data


def parse_context_string(context_string):
    context_list = []
    parts = context_string.split(" > ")

    for part in parts:
        bools = []
        mode = None

        if "&&" in part:
            key, *values = part.split(" && ")

            for value in values:
                if "==" in value:
                    mode_key, mode_value = value.split(" == ")
                    mode = mode_value
                else:
                    bools.append(value)

            context_list.append({"name": key, "bools": bools, "mode": mode})
        else:
            context_list.append({"name": part, "bools": [], "mode": None})

    return context_list


def get_readable_command_and_target(command, context):
    original_command = command

    # Special cases - pre-processing
    if isinstance(command, list):
        # In place of some commands, are lists that contain the command and additional information
        # See `Workspace -> cmd-1` or `Terminal -> cmd-right` for examples
        command, misc_text = command

        if context == "terminal":
            if command == "terminal::SendText":
                command = TERMINAL_CONTROL_CODE_MAP[misc_text]
            elif command == "terminal::SendKeystroke":
                return None

    readable_target, readable_command = command.split("::")
    readable_target = snake_case_to_readable(readable_target).title()

    readable_command = camel_case_to_readable(readable_command)
    readable_command = readable_command.lower().capitalize()

    # Special cases - post-processing
    if isinstance(original_command, list):
        command, misc_text = original_command

        if command in ["pane::ActivateItem", "workspace::ActivatePane"]:
            readable_command = f"{readable_command} {misc_text + 1}"

    return readable_command, readable_target


def get_readable_shortcut(shortcut):
    shortcut_components = re.split("(-|\s)+", shortcut)
    readable_shortcut_components = [
        KEY_NAME_MAP.get(component, component).title()
        for component in shortcut_components
    ]
    readable_shortcut = "".join(readable_shortcut_components)

    return readable_shortcut


def camel_case_to_readable(text):
    return (
        "".join(
            [
                " " + character if character.isupper() else character
                for character in text
            ]
        )
        .lower()
        .strip()
    )


def snake_case_to_readable(text):
    return " ".join(text.split("_"))


if __name__ == "__main__":
    main()
