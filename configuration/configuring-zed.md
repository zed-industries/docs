---
description: Zed can be configured via a simple JSON file
---

# Configuring Zed

Zed can be configured via a simple JSON file located at `~/.config/zed/settings.json`.

## Opening your settings file

You can open `~/.config/zed/settings.json` via `cmd-,`, the command palette, or the `Zed > Settings > Open Settings` application menu item.

You should see something that looks like this:

```json
{
  "theme": "One Dark",
  "buffer_font_family": "PragmataPro Liga",
  "buffer_font_size": 16
}
```

Here are all the currently available settings.

## Active Pane Magnification

- Setting: `active_pane_magnification`
- Description: Scale by which to zoom the active pane. When set to `1.0`, the active pane has the same size as others, but when set to a larger value, the active pane takes up more space.
- Default: `1.0`

**Options**

`float` values

## Autosave

- Setting: `autosave`
- Description: When to automatically save edited buffers.
- Default: `off`

**Options**

1. To disable autosave, set it to `off`

```json
{
  "autosave": "off"
}
```

2. To autosave when focus changes, use `on_focus_change`:

```json
{
  "autosave": "on_focus_change"
}
```

3. To autosave when the active window changes, use `on_window_change`:

```json
{
  "autosave": "on_window_change"
}
```

4. To autosave after an inactivity period, use `after_delay`:

```json
{
  "autosave": {
    "after_delay": {
      "milliseconds": 1000
    }
  }
}
```

## Auto Update

- Setting: `auto_update`
- Description: Whether or not to automatically check for updates.
- Default: `true`

**Options**

`boolean`

## Buffer Font Family

- Setting: `buffer_font_family`
- Description: The name of a font to use for rendering text in the editor.
- Default: `Zed Mono`

**Options**

The name of any font family installed on the user's system

## Buffer Font Features

- Setting: `buffer_font_features`
- Description: The OpenType features to enable for text in the editor.
- Default: `null`

**Options**

Zed supports a subset of OpenType features that can be enabled or disabled for a given buffer or terminal font.  The following [OpenType features](https://en.wikipedia.org/wiki/List_of_typographic_features) can be enabled or disabled too: `calt`, `case`, `cpsp`, `frac`, `liga`, `onum`, `ordn`, `pnum`, `ss01`, `ss02`, `ss03`, `ss04`, `ss05`, `ss06`, `ss07`, `ss08`, `ss09`, `ss10`, `ss11`, `ss12`, `ss13`, `ss14`, `ss15`, `ss16`, `ss17`, `ss18`, `ss19`, `ss20`, `subs`, `sups`, `swsh`, `titl`, `tnum`, `zero`.

For example, to disable ligatures for a given font you can add the following to your settings:

```json
{
  "buffer_font_features": {
    "calt": false
  }
}
```

## Buffer Font Size

- Setting: `buffer_font_size`
- Description: The default font size for text in the editor.
- Default: `15`

**Options**

`integer`

## Confirm Quit

- Setting: `confirm_quit`
- Description: Whether or not to prompt the user to confirm before closing the application.
- Default: `false`

**Options**

`boolean`

## Cursor Blink

- Setting: `cursor_blink`
- Description: Whether or not the cursor blinks.
- Default: `true`

**Options**

`boolean`

## Default Dock Anchor

- Setting: `default_dock_anchor`
- Description: The default anchor for new docks.
- Default: `bottom`

**Options**

1. Position the dock attached to the bottom of the workspace: `bottom`
2. Position the dock to the right of the workspace like a side panel: `right`
3. Position the dock full screen over the entire workspace: `expanded`

## Enable Language Server

- Setting: `enable_language_server`
- Description: Whether or not to use language servers to provide code intelligence.
- Default: `true`

**Options**

`boolean`

## Ensure Final Newline On Save

- Setting: `ensure_final_newline_on_save`
- Description: Whether or not to ensure there's a single newline at the end of a buffer when saving it.
- Default: `true`

**Options**

`boolean`

## LSP

- Setting: `lsp`
- Description: Configuration for language servers.
- Default: `null`

**Options**

The following settings can be overridden for specific language servers:

- `initialization_options`

To override settings for a language, add an entry for that language server's name to the `lsp` value. Example:

```json
"lsp": {
  "rust-analyzer": {
    "initialization_options": {
      "checkOnSave": {
        "command": "clippy" // rust-analyzer.checkOnSave.command
      }
    }
  }
}
```

## Format On Save

- Setting: `format_on_save`
- Description: Whether or not to perform a buffer format before saving.
- Default: `on`

**Options**

1. `on`, enables format on save obeying `formatter` setting:

```json
{
  "format_on_save": "on"
}
```

2. `off`, disables format on save:

```json
{
  "format_on_save": "off"
}
```

## Formatter

- Setting: `formatter`
- Description: How to perform a buffer format.
- Default: `language_server`

**Options**

1. To use the current language server, use `"language_server"`:

```json
{
  "formatter": "language_server"
}
```

2. Or to use an external command, use `"external"`. Specify the name of the formatting program to run, and an array of arguments to pass to the program. The buffer's text will be passed to the program on stdin, and the formatted output should be written to stdout. For example, the following command would strip trailing spaces using [`sed(1)`](https://linux.die.net/man/1/sed):

```json
{
  "formatter": {
    "external": {
      "command": "sed",
      "arguments": ["-e", "s/ *$//"]
    }
  }
}
```

## Hard Tabs

- Setting: `hard_tabs`
- Description: Whether to indent lines using tab characters or multiple spaces.
- Default: `false`

**Options**

`boolean`

## Hover Popover Enabled

- Setting: `hover_popover_enabled`
- Description: Whether or not to show the informational hover box when moving the mouse over symbols in the editor.
- Default: `true`

**Options**

`boolean`

## Language Overrides

- Setting: `language_overrides`
- Description: Configuration overrides for specific languages.
- Default: `null`

**Options**

To override settings for a language, add an entry for that languages name to the `language_overrides` value. Example:

```json
"language_overrides": {
  "C": {
    "format_on_save": "off",
    "preferred_line_length": 64,
    "soft_wrap": "preferred_line_length"
  },
  "JSON": {
    "tab_size": 4
  }
}
```

The following settings can be overridden for each specific languages:

- `enable_language_server`
- `ensure_final_newline_on_save`
- `format_on_save`
- `formatter`
- `hard_tabs`
- `preferred_line_length`
- `remove_trailing_whitespace_on_save`
- `soft_wrap`
- `tab_size`

## Preferred Line Length

- Setting: `preferred_line_length`
- Description: The column at which to soft-wrap lines, for buffers where soft-wrap is enabled.
- Default: `80`

**Options**

`integer`

## Projects Online By Default

- Setting: `projects_online_by_default`
- Description: Whether or not to show the online projects view by default.
- Default: `true`

**Options**

`boolean`

## Remove Trailing Whitespace On Save

- Setting: `remove_trailing_whitespace_on_save`
- Description: Whether or not to remove any trailing whitespace from lines of a buffer before saving it.
- Default: `true`

**Options**

`boolean`

## Show Call Status Icon

- Setting: `show_call_status_icon`
- Description: Whether or not to show the call status icon in the status bar.
- Default: `true`

**Options**

`boolean`

## Show Completions On Input

- Setting: `show_completions_on_input`
- Description: Whether or not to show completions as you type.
- Default: `true`

**Options**

`boolean`

## Soft Wrap

- Setting: `soft_wrap`
- Description: Whether or not the screen sharing icon is shown in the os status bar.
- Default: `none`

**Options**

1. `editor_width`
2. `preferred_line_length`
3. `none`

## Tab Size

- Setting: `tab_size`
- Description: The number of spaces to use for each tab character.
- Default: `4`

**Options**

`integer`

## Telemetry

- Setting: `telemetry`
- Description: Control what info is collected by Zed.
- Default: `"diagnostics": true`, `"metrics": true`

**Options**

- Setting for sending debug-related info (crash reports): `diagnostics`
- Setting for sending anonymized usage data like what languages you're using Zed with: `metrics`

```json
"telemetry": {
  "diagnostics": true,
  "metrics": true
},
```

## Terminal

| **Option**          | **Default**                   | **Description**                                                                                            |
| ------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `working_directory` | `"current_project_directory"` | What working directory strategy to use, see below.                                                         |
| `blinking`          | `"terminal_controlled"`       | Set the terminal cursor blink, see below.                                                                  |
| `alternate_scroll`  | `"on"`                        | Default for the terminal alternate scroll mode, see below.                                                 |
| `option_as_meta`    | `true`                        | Re-interprets the option keys to act like a 'meta' key, like in Emacs.                                     |
| `copy_on_select`    | `false`                       | Whether or not selecting text in the terminal will automatically copy to the system clipboard.             |
| `env`               | `{}`                          | See below.                                                                                                 |
| `font_size`         | not set                       | What font size to use for the terminal. When not set defaults to matching the editor's font size.          |
| `font_family`       | not set                       | What font to use for the terminal. When not set, defaults to matching the editor's font.                   |
| `font_features`     | not set                       | What font features to use for the terminal. When not set, defaults to matching the editor's font features. |

### Terminal: Shell

- Setting: `shell`
- Description: What working directory to use when launching the terminal.
- Default: `system`

**Options**

1. Use the system's default terminal configuration (usually the pw file).
   ```json
   "shell": "system"
   ```
2. A program to launch:
   ```json
   "shell": {
     "program": "sh"
   }
   ```
3. A program with arguments:
   ```json
   "shell": {
       "with_arguments": {
         "program": "/bin/bash",
         "arguments": ["--login"]
       }
   }
   ```

### Terminal: Working Directory Strategy

There are four possible values:

1. Use the current file's project directory. Will Fallback to the first project directory strategy if unsuccessful
   ```json
   "working_directory": "current_project_directory"
   ```
2. Use the first project in this workspace's directory. Will fallback to using this platform's home directory.
   ```json
   "working_directory": "first_project_directory"
   ```
3. Always use this platform's home directory (if we can find it)
   ```json
   "working_directory": "always_home"
   ```
4. Always use a specific directory. This value will be shell expanded. If this path is not a valid directory the terminal will default to this platform's home directory.
   ```json
     "working_directory": {
       "always": {
         "directory": "~/zed/projects/"
       }
     }
   ```

### Terminal: Cursor Blink

Set the cursor blinking behavior in the terminal.
May take 3 values:

1. Never blink the cursor, ignore the terminal mode
   ```json
   "blinking": "off",
   ```
2. Default the cursor blink to off, but allow the terminal to turn blinking on
   ```json
   "blinking": "terminal_controlled",
   ```
3. Always blink the cursor, ignore the terminal mode
   ```json
   "blinking": "on",
   ```

### Terminal: Alternate Scroll Mode

Set whether Alternate Scroll mode (DECSET code: `?1007`) is active by default. Alternate Scroll mode converts mouse scroll events into up / down key presses when in the alternate screen (e.g. when running applications like vim or less). The terminal can still set and unset this mode with ANSI escape codes.
May take 2 values:

1. Default alternate scroll mode to on
   ```json
   "alternate_scroll": "on",
   ```
2. Default alternate scroll mode to off
   ```json
   "alternate_scroll": "off",
   ```

### Terminal: Environment Variables

Any key-value pairs added to this object will be added to the terminal's
environment. Keys must be unique, use `:` to separate multiple values in a single variable:

```json
"env": {
    "ZED": "1",
    "KEY": "value1:value2"
}
```

## Theme

- Setting: `theme`
- Description: The name of the Zed theme to use for the UI.
- Default: `One Dark`

**Options**

Run the `theme selector: toggle` action in the command palette to see a current list of valid themes names.

## Vim

- Setting: `vim_mode`
- Description: Whether or not to enable vim mode (work in progress).
- Default: `false`

**Options**

`boolean`

## An example configuration:

```json
// ~/.config/zed/settings.json
{
  "theme": "cave-light",
  "tab_size": 2,
  "preferred_line_length": 80,
  "soft_wrap": "none",

  "buffer_font_size": 18,
  "buffer_font_family": "Zed Mono",

  "autosave": "on_focus_change",
  "format_on_save": "off",
  "vim_mode": false,
  "projects_online_by_default": true,
  "terminal": {
    "font_family": "FiraCode Nerd Font Mono",
    "blinking": "off"
  },
  "language_overrides": {
    "C": {
      "format_on_save": "language_server",
      "preferred_line_length": 64,
      "soft_wrap": "preferred_line_length"
    }
  }
}
```
