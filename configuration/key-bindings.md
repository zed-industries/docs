# Key bindings

Zed can be configured via a simple JSON file located at `~/.config/zed/keymap.json`.

### Predefined keymaps

We have a growing collection of pre-defined keymaps in our [keymaps repository](https://github.com/zed-industries/keymaps).

### Custom key bindings

#### Accessing custom key bindings

You can open `keymap.json` via `CMD + K, CMD + S`, the command palette, or the `Zed > Preferences > Open Key Bindings` application menu item.

#### Adding a custom key binding

To customize key bindings, specify a context and the list of bindings to set. Re-mapping an existing binding will clobber the existing binding in favor of the custom one.

An example of adding a set of custom key bindings:

```json
[
  {
    "context": "Editor",
    "bindings": {
      "ctrl-w": "editor::SelectLargerSyntaxNode",
      "ctrl-shift-W": "editor::SelectSmallerSyntaxNode",
      "ctrl-c": "editor::Cancel"
    }
  }
]
```

You can see more examples in Zed's [`default.json`](https://zed.dev/ref/default.json)

{% hint style="info" %}
There are some key bindings that can't be overridden; we are working on an issue surrounding this.
{% endhint %}

### All key bindings

#### Editor

| **Command**                      | **Default Shortcut**             |
| -------------------------------- | -------------------------------- |
| Close focused modal or toolbar   | `Esc`                            |
| Backspace                        | `Backspace`                      |
| Backspace                        | `Shift + Backspace`              |
| Backspace                        | `Control + H`                    |
| Delete                           | `Delete`                         |
| Delete                           | `Control + D`                    |
| Tab                              | `Tab`                            |
| Backtab                          | `Shift + Tab`                    |
| Cut to end of line               | `Control + K`                    |
| Transpose                        | `Control + T`                    |
| Delete to beginning of line      | `Command + Backspace`            |
| Delete to end of line            | `Command + Delete`               |
| Delete to previous word start    | `Alt + Backspace`                |
| Delete to previous word end      | `Alt + Delete`                   |
| Delete to previous word start    | `Alt + H`                        |
| Move up                          | `Control + P`                    |
| Move down                        | `Control + N`                    |
| Move left                        | `Control + B`                    |
| Move right                       | `Control + F`                    |
| Move to previous word start      | `Alt + Left`                     |
| Move to previous word start      | `Alt + B`                        |
| Move to next word end            | `Alt + Right`                    |
| Move to next word end            | `Alt + F`                        |
| Move to beginning of line        | `Command + Left`                 |
| Move to beginning of line        | `Control + A`                    |
| Move to end of line              | `Command + Right`                |
| Move to end of line              | `Control + E`                    |
| Move to beginning                | `Command + Up`                   |
| Move to end                      | `Command + Down`                 |
| Select up                        | `Shift + Up`                     |
| Select up                        | `Control + Shift + P`            |
| Select down                      | `Shift + Down`                   |
| Select down                      | `Control + Shift + N`            |
| Select left                      | `Shift + Left`                   |
| Select left                      | `Control + Shift + B`            |
| Select right                     | `Shift +Right`                   |
| Select right                     | `Control + Shift + F`            |
| Select to previous word start    | `Alt + Shift + Left`             |
| Select to previous word start    | `Alt + Shift + B`                |
| Select to next word end          | `Alt + Shift + Right`            |
| Select to next word end          | `Alt + Shift + F`                |
| Select to beginning              | `Shift + Up`                     |
| Select to end                    | `Command + Shift + Down`         |
| Select all                       | `Command + A`                    |
| Select line                      | `Command + L`                    |
| Select to beginning of line      | `Command + Shift + Left`         |
| Select to beginning of line      | `Control + Shift + A`            |
| Select to end of line            | `Command + Shift + Right`        |
| Select to end of line            | `Control + Shift + E`            |
| Page up                          | `Page Up`                        |
| Page down                        | `Page Down`                      |
| New line                         | `Enter`                          |
| New line below                   | `Command + Enter`                |
| Deploy buffer search             | `Command + F`                    |
| Deploy buffer search             | `Command + E`                    |
| Input                            | `Alt + Enter`                    |
| Outdent                          | `Command + [`                    |
| Indent                           | `Command + ]`                    |
| Add selection above              | `Command + Alt + Up`             |
| Add selection above              | `Command + Control + P`          |
| Add selection below              | `Command + Alt + Down`           |
| Add selection below              | `Command + Control + N`          |
| Select next                      | `Command + D`                    |
| Select next                      | `Command + K, Command + D`       |
| Toggle comments                  | `Command + /`                    |
| Select larger syntax node        | `Alt + Up`                       |
| Select smaller syntax node       | `Alt + Down`                     |
| Undo selection                   | `Command + U`                    |
| Redo selection                   | `Command + Shift + U`            |
| Go to next diagnostic            | `F8`                             |
| Go to previous diagnostic        | `Shift + F8`                     |
| Rename                           | `F2`                             |
| Go to definition                 | `F12`                            |
| Go to type definition            | `Command + F12`                  |
| Find all references              | `Alt + Shift + F12`              |
| Move to enclosing bracket        | `Control + M`                    |
| Fold                             | `Alt + Command + [`              |
| Unfold lines                     | `Alt + Command + J`              |
| Show completions                 | `Control + Space`                |
| Toggle code actions              | `Command + -`                    |
| Toggle outline                   | `Command + Shift + O`            |
| Toggle go to line                | `Control + G`                    |
| Delete line                      | `Control + Shift + K`            |
| Duplicate line                   | `Command + Shift + D`            |
| Split selection into lines       | `Command + Shift + L`            |
| Move line up                     | `Control + Command + Up`         |
| Move line down                   | `Control + Command + Down`       |
| Delete to previous subword start | `Control + Alt + Backspace`      |
| Delete to previous subword start | `Control + Alt + H`              |
| Delete to next subword end       | `Control + Alt + Delete`         |
| Delete to next subword end       | `Control + Alt + D`              |
| Move to previous subword start   | `Control + Alt + Left`           |
| Move to previous subword start   | `Control + Alt + B`              |
| Move to next subword end         | `Control + Alt + Right`          |
| Move to next subword end         | `Control + Alt + F`              |
| Select to previous subword start | `Control + Alt + Shift + Left`   |
| Select to previous subword start | `Control + Alt + Shift + B`      |
| Select to next subword end       | `Control + Alt + Shift + Right`  |
| Select to next subword end       | `Control + Alt + Shift + F`      |
| Confirm completion               | `Enter`                          |
| Confirm completion               | `Tab`                            |
| Confirm code action              | `Enter`                          |
| Open exerpts                     | `Alt + Enter`                    |

#### Pane

| **Command**                 | **Default Shortcut**           |
| --------------------------- | ------------------------------ |
| Toggle focus                | `Command + F`                  |
| Select next match           | `Command + G`                  |
| Select previous match       | `Command + Shift + G`          |
| Go back                     | `Control + -`                  |
| Go forward                  | `Shift + Control + _`          |
| Toggle project search focus | `Command + Shift + F`          |
| Activate previous pane      | `Command + K , Command Left`   |
| Activate next pane          | `Command + K , Command Right`  |
| Activate the 1st pane       | `Command + 1`                  |
| Activate the 2nd pane       | `Command + 2`                  |
| Activate the 3rd pane       | `Command + 3`                  |
| Activate the 4th pane       | `Command + 4`                  |
| Activate the 5th pane       | `Command + 5`                  |
| Activate the 6th pane       | `Command + 6`                  |
| Activate the 7th pane       | `Command + 7`                  |
| Activate the 8th pane       | `Command + 8`                  |
| Activate the 9th pane       | `Command + 9`                  |
| Activate previous tab       | `Command + Shift + {`          |
| Activate previous tab       | `Alt + Command + Left`         |
| Activate next tab           | `Command + Shift + }`          |
| Activate next tab           | `Alt + Command + Right`        |
| Activate last tab           | `Control + 0`                  |
| Activate the 1st tab        | `Control + 1`                  |
| Activate the 2nd tab        | `Control + 2`                  |
| Activate the 3rd tab        | `Control + 3`                  |
| Activate the 4th tab        | `Control + 4`                  |
| Activate the 5th tab        | `Control + 5`                  |
| Activate the 6th tab        | `Control + 6`                  |
| Activate the 7th tab        | `Control + 7`                  |
| Activate the 8th tab        | `Control + 8`                  |
| Activate the 9th tab        | `Control + 9`                  |
| Split pane up               | `Command + K , Up`             |
| Split pane down             | `Command + K , Down`           |
| Split pane left             | `Command + K , Left`           |
| Split pane right            | `Command + K , Right`          |

#### Buffer Search Bar

| **Command**           | **Default Shortcut** |
| --------------------- | -------------------- |
| Dismiss               | `Escape`             |
| Focus editor          | `Command + F`        |
| Select next match     | `Enter`              |
| Select previous match | `Shift + Enter`      |
| Search in new         | `Command + Enter`    |

#### Workspace

| **Command**                 | **Default Shortcut**         |
| --------------------------- | ---------------------------- |
| Deploy project search       | `Command + Shift + F`        |
| Toggle theme selctor        | `Command + K , Command + T`  |
| Open key map                | `Command + K , Command + S`  |
| Toggle project symbols      | `Command + T`                |
| Toggle file finder          | `Command + P`                |
| Toggle command palette      | `Command + Shift + P`        |
| Deploy diagnostics          | `Command + Shift + M`        |
| Save all workspace          | `Command + Alt + S`          |
| Toggle left sidebar         | `Command + B`                |
| Toggle right sidebar        | `Command + Shift + B`        |
| Toggle project panel focus  | `Command + Shift + E`        |
| Toggle contacts panel focus | `Command + Shift + C`        |

#### Following

| **Command**              | **Default Shortcut**           |
| ------------------------ | ------------------------------ |
| Follow next collaborator | `Control + Alt + Command + F`  |
| Debug elements           | `Command Alt + I`              |

#### Project panel

| **Command**             | **Default Shortcut** |
| ----------------------- | -------------------- |
| Collapse selected entry | `Left`               |
| Expand selected entry   | `Right`              |
| Rename                  | `F2`                 |
| Delete                  | `Backspace`          |
