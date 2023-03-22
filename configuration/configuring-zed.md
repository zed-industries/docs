---
description: Zed can be configured via a simple JSON file
---

# Configuring Zed

Zed can be configured via a simple JSON file located at `~/.config/zed/settings.json`.

## Opening your settings file

You can open `~/.config/zed/settings.json` via `cmd-,`, the command palette, or the `Zed > Preferences > Open Settings` application menu item.

You should see something that looks like this:

```json
{
  "theme": "One Dark",
  "buffer_font_family": "PragmataPro Liga",
  "buffer_font_size": 16
}
```

Here are all the currently available settings.

## Available settings

| **Option**                           | **Default**       | **Description**                                                                                                                                                              |
| ------------------------------------ | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `autosave`                           | `off`             | See 'autosave' section below                                                                                                                                                 |
| `buffer_font_family`                 | `zed-mono`        | `string` Either `zed-mono` or the name of an installed Font family                                                                                                           |
| `buffer_font_size`                   | `16`              | `number` The editor font size                                                                                                                                                |
| `buffer_font_features`               | `null`            | See 'font features' section below                                                                                                                                            |
| `enable_language_server`             | `true`            | `boolean` Whether language servers should be used                                                                                                                            |
| `ensure_final_newline_on_save`       | `true`            | `boolean` If missing, whether an empty newline will be added at the end of the file                                                                                          |
| `lsp`                                | `null`            | See 'lsp' section below                                                                                                                                                      |
| `format_on_save`                     | `on`              | See 'format on save' section below                                                                                                                                           |
| `formatter`                          | `language_server` | See 'formatter' section below                                                                                                                                                |
| `hard_tabs`                          | `false`           | `boolean` Indent using tabs instead of spaces                                                                                                                                |
| `hover_popover_enabled`              | `true`            | `boolean` Enables triggering the hover popover with the mouse                                                                                                                |
| `show_completions_on_input`          | `true`            | `boolean` Causes the completion menu to show in editors while typing                                                                                                         |
| `language_overrides`                 | `null`            | See 'overrides' section below                                                                                                                                                |
| `tab_size`                           | `4`               | The number of columns occupied by a tab                                                                                                                                      |
| `theme`                              | `One Dark`        | `string` The name of a Zed theme                                                                                                                                             |
| `preferred_line_length`              | `80`              | The number of characters at which to soft wrap lines, when soft wrap is enabled                                                                                              |
| `projects_online_by_default`         | `true`            | `boolean` Project goes online when opened.                                                                                                                                   |
| `remove_trailing_whitespace_on_save` | `true`            | `boolean` Whether all trailing whitespace will be removed on each line                                                                                                       |
| `soft_wrap`                          | `editor_width`    | `editor_width`, `none`, `preferred_line_length`                                                                                                                              |
| `active_pane_magnification`          | `1.0`             | Scale by which to zoom the active pane. When set to `1.0`, the active pane has the same size as others, but when set to a larger value, the active pane takes up more space. |
| `vim_mode`                           | `false`           | `boolean` Enables Vim mode (WIP)                                                                                                                                             |
| `terminal`                           | See below         | See 'Terminal' section below                                                                                                                                                 |

## Autosave

The `autosave` setting has four different modes:

1. To disable autosave, set it to `"off"`

   ```json
   {
     "autosave": "off"
   }
   ```

2. To autosave when focus changes, use `"on_focus_change"`:

   ```json
   {
     "autosave": "on_focus_change"
   }
   ```

3. To autosave when the active window changes, use `"on_window_change"`:

   ```json
   {
     "autosave": "on_window_change"
   }
   ```

4. To autosave after an inactivity period, use `"after_delay"`:

   ```json
   {
     "autosave": {
       "after_delay": {
         "milliseconds": 1000
       }
     }
   }
   ```

## Format On Save

The `format_on_save` setting controls if files are formatted before saving. There are two modes:

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

The `formatter` setting dictates how a format is performed and has two different modes:

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

## Lsp

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

## Overrides

The following settings can be overridden for specific languages:

- `tab_size`
- `hard_tabs`
- `soft_wrap`
- `preferred_line_length`
- `format_on_save`
- `formatter`
- `enable_language_server`

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

For a complete list of languages you can override settings for see [Supported Languages](../languages/support-languages.md).

## Font Features

Zed supports a subset of OpenType features that can be enabled or disabled for a given buffer or terminal font. For example, to disable ligatures for a given font you can add the following to your settings:

```json
{
  "buffer_font_features": {
    "calt": false
  }
}
```

Optionally, the following OpenType features can be enabled or disabled too: `calt`, `case`, `cpsp`, `frac`, `liga`, `onum`, `ordn`, `pnum`, `ss01`, `ss02`, `ss03`, `ss04`, `ss05`, `ss06`, `ss07`, `ss08`, `ss09`, `ss10`, `ss11`, `ss12`, `ss13`, `ss14`, `ss15`, `ss16`, `ss17`, `ss18`, `ss19`, `ss20`, `subs`, `sups`, `swsh`, `titl`, `tnum`, `zero`.

## Terminal

| **Option**          | **Default**                   | **Description**                                                                                            |
| ------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------          |
| `shell`             | `"system"`                    | What shell to use on launch, see below.                                                                    |
| `working_directory` | `"current_project_directory"` | What working directory strategy to use, see below.                                                         |
| `blinking`          | `"terminal_controlled"`       | Set the terminal cursor blink, see below.                                                                  |
| `alternate_scroll`  | `"on"`                        | Default for the terminal alternate scroll mode, see below.                                                 |
| `option_as_meta`    | `true`                        | Re-interprets the option keys to act like a 'meta' key, like in Emacs.                                     |
| `copy_on_select`    | `false`                       | Whether or not selecting text in the terminal will automatically copy to the system clipboard.             |
| `env`               | `{}`                          | See below.                                                                                                 |
| `font_size`         | not set                       | What font size to use for the terminal. When not set defaults to matching the editor's font size.          |
| `font_family`       | not set                       | What font to use for the terminal. When not set, defaults to matching the editor's font.                   |
| `font_features`     | not set                       | What font features to use for the terminal. When not set, defaults to matching the editor's font features. |

### Terminal: Launch Shell

What shell to use when opening a terminal. May take 3 values:

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
