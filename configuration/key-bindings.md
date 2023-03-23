# Key bindings

Zed can be configured via a simple JSON file located at `~/.config/zed/keymap.json`.

### Predefined keymaps

We have a growing collection of pre-defined keymaps in our [keymaps repository](https://github.com/zed-industries/keymaps).

### Custom key bindings

#### Accessing custom key bindings

You can open `keymap.json` via `CMD + K, CMD + S`, the command palette, or the `Zed > Settings > Open Key Bindings` application menu item.

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

| **Command**                      | **Default Shortcut**            |
| -------------------------------- | ------------------------------- |
| Add selection above              | `Command + Alt + Up`            |
| Add selection above              | `Command + Control + P`         |
| Add selection below              | `Command + Alt + Down`          |
| Add selection below              | `Command + Control + N`         |
| Backspace                        | `Backspace`                     |
| Backspace                        | `Control + H`                   |
| Backspace                        | `Shift + Backspace`             |
| Backtab                          | `Shift + Tab`                   |
| Close focused modal or toolbar   | `Esc`                           |
| Confirm code action              | `Enter`                         |
| Confirm completion               | `Enter`                         |
| Confirm completion               | `Tab`                           |
| Cut to end of line               | `Control + K`                   |
| Delete                           | `Control + D`                   |
| Delete                           | `Delete`                        |
| Delete line                      | `Control + Shift + K`           |
| Delete to beginning of line      | `Command + Backspace`           |
| Delete to end of line            | `Command + Delete`              |
| Delete to next subword end       | `Control + Alt + D`             |
| Delete to next subword end       | `Control + Alt + Delete`        |
| Delete to previous subword start | `Control + Alt + Backspace`     |
| Delete to previous subword start | `Control + Alt + H`             |
| Delete to previous word end      | `Alt + Delete`                  |
| Delete to previous word start    | `Alt + Backspace`               |
| Delete to previous word start    | `Alt + H`                       |
| Deploy buffer search             | `Command + E`                   |
| Deploy buffer search             | `Command + F`                   |
| Duplicate line                   | `Command + Shift + D`           |
| Find all references              | `Alt + Shift + F12`             |
| Fold                             | `Alt + Command + [`             |
| Go to definition                 | `F12`                           |
| Go to next diagnostic            | `F8`                            |
| Go to previous diagnostic        | `Shift + F8`                    |
| Go to type definition            | `Command + F12`                 |
| Indent                           | `Command + ]`                   |
| Input                            | `Alt + Enter`                   |
| Move down                        | `Control + N`                   |
| Move left                        | `Control + B`                   |
| Move line down                   | `Control + Command + Down`      |
| Move line up                     | `Control + Command + Up`        |
| Move right                       | `Control + F`                   |
| Move to beginning                | `Command + Up`                  |
| Move to beginning of line        | `Command + Left`                |
| Move to beginning of line        | `Control + A`                   |
| Move to enclosing bracket        | `Control + M`                   |
| Move to end                      | `Command + Down`                |
| Move to end of line              | `Command + Right`               |
| Move to end of line              | `Control + E`                   |
| Move to next subword end         | `Control + Alt + F`             |
| Move to next subword end         | `Control + Alt + Right`         |
| Move to next word end            | `Alt + F`                       |
| Move to next word end            | `Alt + Right`                   |
| Move to previous subword start   | `Control + Alt + B`             |
| Move to previous subword start   | `Control + Alt + Left`          |
| Move to previous word start      | `Alt + B`                       |
| Move to previous word start      | `Alt + Left`                    |
| Move up                          | `Control + P`                   |
| New line                         | `Enter`                         |
| New line below                   | `Command + Enter`               |
| Open excerpts                    | `Alt + Enter`                   |
| Outdent                          | `Command + [`                   |
| Page down                        | `Page Down`                     |
| Page up                          | `Page Up`                       |
| Redo selection                   | `Command + Shift + U`           |
| Rename                           | `F2`                            |
| Select all                       | `Command + A`                   |
| Select down                      | `Control + Shift + N`           |
| Select down                      | `Shift + Down`                  |
| Select larger syntax node        | `Alt + Up`                      |
| Select left                      | `Control + Shift + B`           |
| Select left                      | `Shift + Left`                  |
| Select line                      | `Command + L`                   |
| Select next                      | `Command + D`                   |
| Select next                      | `Command + K, Command + D`      |
| Select right                     | `Control + Shift + F`           |
| Select right                     | `Shift +Right`                  |
| Select smaller syntax node       | `Alt + Down`                    |
| Select to beginning              | `Shift + Up`                    |
| Select to beginning of line      | `Command + Shift + Left`        |
| Select to beginning of line      | `Control + Shift + A`           |
| Select to end                    | `Command + Shift + Down`        |
| Select to end of line            | `Command + Shift + Right`       |
| Select to end of line            | `Control + Shift + E`           |
| Select to next subword end       | `Control + Alt + Shift + F`     |
| Select to next subword end       | `Control + Alt + Shift + Right` |
| Select to next word end          | `Alt + Shift + F`               |
| Select to next word end          | `Alt + Shift + Right`           |
| Select to previous subword start | `Control + Alt + Shift + B`     |
| Select to previous subword start | `Control + Alt + Shift + Left`  |
| Select to previous word start    | `Alt + Shift + B`               |
| Select to previous word start    | `Alt + Shift + Left`            |
| Select up                        | `Control + Shift + P`           |
| Select up                        | `Shift + Up`                    |
| Show completions                 | `Control + Space`               |
| Split selection into lines       | `Command + Shift + L`           |
| Tab                              | `Tab`                           |
| Toggle code actions              | `Command + -`                   |
| Toggle comments                  | `Command + /`                   |
| Toggle go to line                | `Control + G`                   |
| Toggle outline                   | `Command + Shift + O`           |
| Transpose                        | `Control + T`                   |
| Undo selection                   | `Command + U`                   |
| Unfold lines                     | `Alt + Command + J`             |

#### Pane

| **Command**                 | **Default Shortcut**          |
| --------------------------- | ----------------------------- |
| Activate last tab           | `Control + 0`                 |
| Activate next pane          | `Command + K , Command Right` |
| Activate next tab           | `Alt + Command + Right`       |
| Activate next tab           | `Command + Shift + }`         |
| Activate previous pane      | `Command + K , Command Left`  |
| Activate previous tab       | `Alt + Command + Left`        |
| Activate previous tab       | `Command + Shift + {`         |
| Activate the 1st pane       | `Command + 1`                 |
| Activate the 1st tab        | `Control + 1`                 |
| Activate the 2nd pane       | `Command + 2`                 |
| Activate the 2nd tab        | `Control + 2`                 |
| Activate the 3rd pane       | `Command + 3`                 |
| Activate the 3rd tab        | `Control + 3`                 |
| Activate the 4th pane       | `Command + 4`                 |
| Activate the 4th tab        | `Control + 4`                 |
| Activate the 5th pane       | `Command + 5`                 |
| Activate the 5th tab        | `Control + 5`                 |
| Activate the 6th pane       | `Command + 6`                 |
| Activate the 6th tab        | `Control + 6`                 |
| Activate the 7th pane       | `Command + 7`                 |
| Activate the 7th tab        | `Control + 7`                 |
| Activate the 8th pane       | `Command + 8`                 |
| Activate the 8th tab        | `Control + 8`                 |
| Activate the 9th pane       | `Command + 9`                 |
| Activate the 9th tab        | `Control + 9`                 |
| Go back                     | `Control + -`                 |
| Go forward                  | `Shift + Control + _`         |
| Select next match           | `Command + G`                 |
| Select previous match       | `Command + Shift + G`         |
| Split pane down             | `Command + K , Down`          |
| Split pane left             | `Command + K , Left`          |
| Split pane right            | `Command + K , Right`         |
| Split pane up               | `Command + K , Up`            |
| Toggle focus                | `Command + F`                 |
| Toggle project search focus | `Command + Shift + F`         |

#### Buffer Search Bar

| **Command**           | **Default Shortcut** |
| --------------------- | -------------------- |
| Dismiss               | `Escape`             |
| Focus editor          | `Command + F`        |
| Search in new         | `Command + Enter`    |
| Select next match     | `Enter`              |
| Select previous match | `Shift + Enter`      |

#### Workspace

| **Command**                 | **Default Shortcut**        |
| --------------------------- | --------------------------- |
| Deploy diagnostics          | `Command + Shift + M`       |
| Deploy project search       | `Command + Shift + F`       |
| Open keymap                 | `Command + K , Command + S` |
| Save all workspace          | `Command + Alt + S`         |
| Toggle command palette      | `Command + Shift + P`       |
| Toggle contacts panel focus | `Command + Shift + C`       |
| Toggle file finder          | `Command + P`               |
| Toggle left sidebar         | `Command + B`               |
| Toggle project panel focus  | `Command + Shift + E`       |
| Toggle project symbols      | `Command + T`               |
| Toggle right sidebar        | `Command + Shift + B`       |
| Toggle theme selector       | `Command + K , Command + T` |

#### Following

| **Command**              | **Default Shortcut**          |
| ------------------------ | ----------------------------- |
| Debug elements           | `Command Alt + I`             |
| Follow next collaborator | `Control + Alt + Command + F` |

#### Project Panel

| **Command**             | **Default Shortcut** |
| :---------------------- | :------------------- |
| Collapse selected entry | `Left`               |
| Copy                    | `Command + C`        |
| Copy path               | `Command + Alt + C`  |
| Cut                     | `Command + X`        |
| Delete                  | `Backspace`          |
| Expand selected entry   | `Right`              |
| Paste                   | `Command + V`        |
| Rename                  | `F2`                 |
| Reveal in finder        | `Alt + Command + R`  |

#### Project Search Bar

| **Command**   | **Default Shortcut** |
| :------------ | :------------------- |
| Search in new | `Command + Enter`    |

#### Terminal

| **Command**                 | **Default Shortcut**        |
| :-------------------------- | :-------------------------- |
| Clear                       | `Command + K`               |
| Copy                        | `Command + C`               |
| Delete line                 | `Command + Backspace`       |
| Move to beginning of line   | `Command + Left`            |
| Move to end of line         | `Command + Right`           |
| Move to next word end       | `Alt + Right`               |
| Move to previous word start | `Alt + Left`                |
| Paste                       | `Command + V`               |
| Show character palette      | `Control + Command + Space` |
