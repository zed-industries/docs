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
| :------------------------------- | :------------------------------ |
| Add selection above              | `Command + Alt + Up`            |
| Add selection above              | `Command + Control + P`         |
| Add selection below              | `Command + Alt + Down`          |
| Add selection below              | `Command + Control + N`         |
| Backspace                        | `Backspace`                     |
| Backspace                        | `Control + H`                   |
| Backspace                        | `Shift + Backspace`             |
| Cancel                           | `Escape`                        |
| Confirm code action              | `Enter`                         |
| Confirm completion               | `Enter`                         |
| Confirm completion               | `Tab`                           |
| Confirm rename                   | `Enter`                         |
| Copy                             | `Command + C`                   |
| Cut                              | `Command + X`                   |
| Cut to end of line               | `Control + K`                   |
| Delete                           | `Control + D`                   |
| Delete                           | `Delete`                        |
| Delete line                      | `Control + Shift + K`           |
| Delete to beginning of line      | `Command + Backspace`           |
| Delete to end of line            | `Command + Delete`              |
| Delete to next subword end       | `Control + Alt + D`             |
| Delete to next subword end       | `Control + Alt + Delete`        |
| Delete to next word end          | `Alt + D`                       |
| Delete to next word end          | `Alt + Delete`                  |
| Delete to previous subword start | `Control + Alt + Backspace`     |
| Delete to previous subword start | `Control + Alt + H`             |
| Delete to previous word start    | `Alt + Backspace`               |
| Delete to previous word start    | `Alt + H`                       |
| Deploy                           | `Command + E`                   |
| Deploy                           | `Command + F`                   |
| Duplicate line                   | `Command + Shift + D`           |
| Find all references              | `Alt + Shift + F12`             |
| Fold                             | `Alt + Command + [`             |
| Format                           | `Command + Shift + I`           |
| Go to definition                 | `F12`                           |
| Go to diagnostic                 | `F8`                            |
| Go to hunk                       | `Command + F8`                  |
| Go to prev diagnostic            | `Shift + F8`                    |
| Go to prev hunk                  | `Command + Shift + F8`          |
| Go to type definition            | `Command + F12`                 |
| Hover                            | `Command + K, Command + I`      |
| Indent                           | `Command + ]`                   |
| Move down                        | `Control + N`                   |
| Move down                        | `Down`                          |
| Move left                        | `Control + B`                   |
| Move left                        | `Left`                          |
| Move line down                   | `Control + Command + Down`      |
| Move line up                     | `Control + Command + Up`        |
| Move page down                   | `Control + V`                   |
| Move page down                   | `Shift + Page Down`             |
| Move page up                     | `Alt + V`                       |
| Move page up                     | `Shift + Page Up`               |
| Move right                       | `Control + F`                   |
| Move right                       | `Right`                         |
| Move to beginning                | `Command + Up`                  |
| Move to beginning of line        | `Command + Left`                |
| Move to beginning of line        | `Control + A`                   |
| Move to beginning of line        | `Home`                          |
| Move to enclosing bracket        | `Control + M`                   |
| Move to end                      | `Command + Down`                |
| Move to end of line              | `Command + Right`               |
| Move to end of line              | `Control + E`                   |
| Move to end of line              | `End`                           |
| Move to next subword end         | `Control + Alt + F`             |
| Move to next subword end         | `Control + Alt + Right`         |
| Move to next word end            | `Alt + F`                       |
| Move to next word end            | `Alt + Right`                   |
| Move to previous subword start   | `Control + Alt + B`             |
| Move to previous subword start   | `Control + Alt + Left`          |
| Move to previous word start      | `Alt + B`                       |
| Move to previous word start      | `Alt + Left`                    |
| Move up                          | `Control + P`                   |
| Move up                          | `Up`                            |
| Newline                          | `Alt + Enter`                   |
| Newline                          | `Enter`                         |
| Newline below                    | `Command + Alt + Enter`         |
| Newline below                    | `Command + Enter`               |
| Next screen                      | `Control + L`                   |
| Open excerpts                    | `Alt + Enter`                   |
| Outdent                          | `Command + [`                   |
| Page down                        | `Page Down`                     |
| Page up                          | `Page Up`                       |
| Paste                            | `Command + V`                   |
| Redo                             | `Command + Shift + Z`           |
| Redo selection                   | `Command + Shift + U`           |
| Rename                           | `F2`                            |
| Reveal in finder                 | `Alt + Command + R`             |
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
| Select right                     | `Shift + Right`                 |
| Select smaller syntax node       | `Alt + Down`                    |
| Select to beginning              | `Command + Shift + Up`          |
| Select to beginning of line      | `Command + Shift + Left`        |
| Select to beginning of line      | `Control + Shift + A`           |
| Select to beginning of line      | `Shift + Home`                  |
| Select to end                    | `Command + Shift + Down`        |
| Select to end of line            | `Command + Shift + Right`       |
| Select to end of line            | `Control + Shift + E`           |
| Select to end of line            | `Shift + End`                   |
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
| Show character palette           | `Control + Command + Space`     |
| Show completions                 | `Control + Space`               |
| Split selection into lines       | `Command + Shift + L`           |
| Tab                              | `Tab`                           |
| Tab prev                         | `Shift + Tab`                   |
| Toggle                           | `Command + Shift + O`           |
| Toggle                           | `Control + G`                   |
| Toggle code actions              | `Command + .`                   |
| Toggle comments                  | `Command + /`                   |
| Toggle soft wrap                 | `Alt + Z`                       |
| Transpose                        | `Control + T`                   |
| Undo                             | `Command + Z`                   |
| Undo selection                   | `Command + U`                   |
| Unfold lines                     | `Alt + Command + ]`             |

#### Pane

| **Command**           | **Default Shortcut**  |
| :-------------------- | :-------------------- |
| Activate item         | `Control + 1`         |
| Activate item         | `Control + 2`         |
| Activate item         | `Control + 3`         |
| Activate item         | `Control + 4`         |
| Activate item         | `Control + 5`         |
| Activate item         | `Control + 6`         |
| Activate item         | `Control + 7`         |
| Activate item         | `Control + 8`         |
| Activate item         | `Control + 9`         |
| Activate last item    | `Control + 0`         |
| Add tab to dock       | `Command + Escape`    |
| Go back               | `Control + `          |
| Go forward            | `Control + _`         |
| Hide dock             | `Shift + Escape`      |
| Remove tab from dock  | `Command + Escape`    |
| Reopen closed item    | `Command + Shift + T` |
| Select next match     | `Command + G`         |
| Select prev match     | `Command + Shift + G` |
| Split down            | `Command + K, Down`   |
| Split left            | `Command + K, Left`   |
| Split right           | `Command + K, Right`  |
| Split up              | `Command + K, Up`     |
| Toggle case sensitive | `Alt + Command + C`   |
| Toggle focus          | `Command + F`         |
| Toggle focus          | `Command + Shift + F` |
| Toggle regex          | `Alt + Command + R`   |
| Toggle whole word     | `Alt + Command + W`   |

#### Buffer Search Bar

| **Command**       | **Default Shortcut** |
| :---------------- | :------------------- |
| Dismiss           | `Escape`             |
| Focus editor      | `Tab`                |
| Select next match | `Enter`              |
| Select prev match | `Shift + Enter`      |

#### Workspace

| **Command**         | **Default Shortcut**       |
| :------------------ | :------------------------- |
| Activate pane       | `Command + 1`              |
| Activate pane       | `Command + 2`              |
| Activate pane       | `Command + 3`              |
| Activate pane       | `Command + 4`              |
| Activate pane       | `Command + 5`              |
| Activate pane       | `Command + 6`              |
| Activate pane       | `Command + 7`              |
| Activate pane       | `Command + 8`              |
| Activate pane       | `Command + 9`              |
| Deploy              | `Command + Shift + M`      |
| Focus dock          | `Shift + Escape`           |
| New search          | `Command + Shift + F`      |
| Open keymap         | `Command + K, Command + S` |
| Save all            | `Command + Alt + S`        |
| Toggle              | `Command + K, Command + T` |
| Toggle              | `Command + T`              |
| Toggle              | `Command + P`              |
| Toggle              | `Command + Shift + P`      |
| Toggle              | `Command + K, M`           |
| Toggle focus        | `Command + Shift + E`      |
| Toggle left sidebar | `Command + B`              |

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
