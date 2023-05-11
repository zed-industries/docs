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

#### Global

| **Command**               | **Target**   | **Default Shortcut**                           |
|---------------------------|--------------|------------------------------------------------|
| Activate next item        | Pane         | `Alt + Command + Right`                        |
| Activate next item        | Pane         | `Command + }`                                  |
| Activate next pane        | Workspace    | `Command + K, Command + Right`                 |
| Activate prev item        | Pane         | `Alt + Command + Left`                         |
| Activate prev item        | Pane         | `Command + {`                                  |
| Activate previous pane    | Workspace    | `Command + K, Command + Left`                  |
| Anchor dock bottom        | Dock         | `Command + Shift + K, Command + Shift + Down`  |
| Anchor dock right         | Dock         | `Command + Shift + K, Command + Shift + Right` |
| Cancel                    | Menu         | `Control + C`                                  |
| Cancel                    | Menu         | `Escape`                                       |
| Close active item         | Pane         | `Command + W`                                  |
| Close all items           | Pane         | `Command + K, Command + W`                     |
| Close clean items         | Pane         | `Command + K, U`                               |
| Close inactive items      | Pane         | `Alt + Command + T`                            |
| Close window              | Workspace    | `Command + Shift + W`                          |
| Confirm                   | Menu         | `Enter`                                        |
| Debug elements            | Zed          | `Command + Alt + I`                            |
| Decrease buffer font size | Zed          | `Command + `                                   |
| Expand dock               | Dock         | `Command + Shift + K, Command + Shift + Up`    |
| Follow next collaborator  | Workspace    | `Control + Alt + Command + F`                  |
| Hide                      | Zed          | `Command + H`                                  |
| Hide others               | Zed          | `Alt + Command + H`                            |
| Increase buffer font size | Zed          | `Command + =`                                  |
| Minimize                  | Zed          | `Command + M`                                  |
| New file                  | Workspace    | `Command + N`                                  |
| New terminal              | Workspace    | ```Control + ````                              |
| New window                | Workspace    | `Command + Shift + N`                          |
| Open                      | Workspace    | `Command + O`                                  |
| Open recent               | Projects     | `Alt + Command + O`                            |
| Open settings             | Zed          | `Command + ,`                                  |
| Quit                      | Zed          | `Command + Q`                                  |
| Reset buffer font size    | Zed          | `Command + 0`                                  |
| Save                      | Workspace    | `Command + S`                                  |
| Save as                   | Workspace    | `Command + Shift + S`                          |
| Select first              | Menu         | `Command + Up`                                 |
| Select first              | Menu         | `Page Up`                                      |
| Select first              | Menu         | `Shift + Page Down`                            |
| Select first              | Menu         | `Shift + Page Up`                              |
| Select last               | Menu         | `Command + Down`                               |
| Select last               | Menu         | `Page Down`                                    |
| Select next               | Menu         | `Control + N`                                  |
| Select next               | Menu         | `Down`                                         |
| Select prev               | Menu         | `Control + P`                                  |
| Select prev               | Menu         | `Up`                                           |
| Toggle contacts menu      | Collab       | `Command + Shift + C`                          |
| Toggle full screen        | Zed          | `Control + Command + F`                        |

#### Editor

| **Command**                      | **Target**    | **Default Shortcut**            |
|----------------------------------|---------------|---------------------------------|
| Add selection above              | Editor        | `Command + Alt + Up`            |
| Add selection above              | Editor        | `Command + Control + P`         |
| Add selection below              | Editor        | `Command + Alt + Down`          |
| Add selection below              | Editor        | `Command + Control + N`         |
| Backspace                        | Editor        | `Backspace`                     |
| Backspace                        | Editor        | `Control + H`                   |
| Backspace                        | Editor        | `Shift + Backspace`             |
| Cancel                           | Editor        | `Escape`                        |
| Confirm code action              | Editor        | `Enter`                         |
| Confirm completion               | Editor        | `Enter`                         |
| Confirm completion               | Editor        | `Tab`                           |
| Confirm rename                   | Editor        | `Enter`                         |
| Copy                             | Editor        | `Command + C`                   |
| Cut                              | Editor        | `Command + X`                   |
| Cut to end of line               | Editor        | `Control + K`                   |
| Delete                           | Editor        | `Control + D`                   |
| Delete                           | Editor        | `Delete`                        |
| Delete line                      | Editor        | `Control + Shift + K`           |
| Delete to beginning of line      | Editor        | `Command + Backspace`           |
| Delete to end of line            | Editor        | `Command + Delete`              |
| Delete to next subword end       | Editor        | `Control + Alt + D`             |
| Delete to next subword end       | Editor        | `Control + Alt + Delete`        |
| Delete to next word end          | Editor        | `Alt + D`                       |
| Delete to next word end          | Editor        | `Alt + Delete`                  |
| Delete to previous subword start | Editor        | `Control + Alt + Backspace`     |
| Delete to previous subword start | Editor        | `Control + Alt + H`             |
| Delete to previous word start    | Editor        | `Alt + Backspace`               |
| Delete to previous word start    | Editor        | `Alt + H`                       |
| Deploy                           | Buffer Search | `Command + E`                   |
| Deploy                           | Buffer Search | `Command + F`                   |
| Duplicate line                   | Editor        | `Command + Shift + D`           |
| Find all references              | Editor        | `Alt + Shift + F12`             |
| Fold                             | Editor        | `Alt + Command + [`             |
| Format                           | Editor        | `Command + Shift + I`           |
| Go to definition                 | Editor        | `F12`                           |
| Go to diagnostic                 | Editor        | `F8`                            |
| Go to hunk                       | Editor        | `Command + F8`                  |
| Go to prev diagnostic            | Editor        | `Shift + F8`                    |
| Go to prev hunk                  | Editor        | `Command + Shift + F8`          |
| Go to type definition            | Editor        | `Command + F12`                 |
| Hover                            | Editor        | `Command + K, Command + I`      |
| Indent                           | Editor        | `Command + ]`                   |
| Move down                        | Editor        | `Control + N`                   |
| Move down                        | Editor        | `Down`                          |
| Move left                        | Editor        | `Control + B`                   |
| Move left                        | Editor        | `Left`                          |
| Move line down                   | Editor        | `Control + Command + Down`      |
| Move line up                     | Editor        | `Control + Command + Up`        |
| Move page down                   | Editor        | `Control + V`                   |
| Move page down                   | Editor        | `Shift + Page Down`             |
| Move page up                     | Editor        | `Alt + V`                       |
| Move page up                     | Editor        | `Shift + Page Up`               |
| Move right                       | Editor        | `Control + F`                   |
| Move right                       | Editor        | `Right`                         |
| Move to beginning                | Editor        | `Command + Up`                  |
| Move to beginning of line        | Editor        | `Command + Left`                |
| Move to beginning of line        | Editor        | `Control + A`                   |
| Move to beginning of line        | Editor        | `Home`                          |
| Move to enclosing bracket        | Editor        | `Control + M`                   |
| Move to end                      | Editor        | `Command + Down`                |
| Move to end of line              | Editor        | `Command + Right`               |
| Move to end of line              | Editor        | `Control + E`                   |
| Move to end of line              | Editor        | `End`                           |
| Move to next subword end         | Editor        | `Control + Alt + F`             |
| Move to next subword end         | Editor        | `Control + Alt + Right`         |
| Move to next word end            | Editor        | `Alt + F`                       |
| Move to next word end            | Editor        | `Alt + Right`                   |
| Move to previous subword start   | Editor        | `Control + Alt + B`             |
| Move to previous subword start   | Editor        | `Control + Alt + Left`          |
| Move to previous word start      | Editor        | `Alt + B`                       |
| Move to previous word start      | Editor        | `Alt + Left`                    |
| Move up                          | Editor        | `Control + P`                   |
| Move up                          | Editor        | `Up`                            |
| Newline                          | Editor        | `Alt + Enter`                   |
| Newline                          | Editor        | `Enter`                         |
| Newline below                    | Editor        | `Command + Alt + Enter`         |
| Newline below                    | Editor        | `Command + Enter`               |
| Next screen                      | Editor        | `Control + L`                   |
| Next suggestion                  | Copilot       | `Alt + ]`                       |
| Open excerpts                    | Editor        | `Alt + Enter`                   |
| Outdent                          | Editor        | `Command + [`                   |
| Page down                        | Editor        | `Page Down`                     |
| Page up                          | Editor        | `Page Up`                       |
| Paste                            | Editor        | `Command + V`                   |
| Previous suggestion              | Copilot       | `Alt + [`                       |
| Redo                             | Editor        | `Command + Shift + Z`           |
| Redo selection                   | Editor        | `Command + Shift + U`           |
| Rename                           | Editor        | `F2`                            |
| Reveal in finder                 | Editor        | `Alt + Command + R`             |
| Select all                       | Editor        | `Command + A`                   |
| Select down                      | Editor        | `Control + Shift + N`           |
| Select down                      | Editor        | `Shift + Down`                  |
| Select larger syntax node        | Editor        | `Alt + Up`                      |
| Select left                      | Editor        | `Control + Shift + B`           |
| Select left                      | Editor        | `Shift + Left`                  |
| Select line                      | Editor        | `Command + L`                   |
| Select next                      | Editor        | `Command + D`                   |
| Select next                      | Editor        | `Command + K, Command + D`      |
| Select right                     | Editor        | `Control + Shift + F`           |
| Select right                     | Editor        | `Shift + Right`                 |
| Select smaller syntax node       | Editor        | `Alt + Down`                    |
| Select to beginning              | Editor        | `Command + Shift + Up`          |
| Select to beginning of line      | Editor        | `Command + Shift + Left`        |
| Select to beginning of line      | Editor        | `Control + Shift + A`           |
| Select to beginning of line      | Editor        | `Shift + Home`                  |
| Select to end                    | Editor        | `Command + Shift + Down`        |
| Select to end of line            | Editor        | `Command + Shift + Right`       |
| Select to end of line            | Editor        | `Control + Shift + E`           |
| Select to end of line            | Editor        | `Shift + End`                   |
| Select to next subword end       | Editor        | `Control + Alt + Shift + F`     |
| Select to next subword end       | Editor        | `Control + Alt + Shift + Right` |
| Select to next word end          | Editor        | `Alt + Shift + F`               |
| Select to next word end          | Editor        | `Alt + Shift + Right`           |
| Select to previous subword start | Editor        | `Control + Alt + Shift + B`     |
| Select to previous subword start | Editor        | `Control + Alt + Shift + Left`  |
| Select to previous word start    | Editor        | `Alt + Shift + B`               |
| Select to previous word start    | Editor        | `Alt + Shift + Left`            |
| Select up                        | Editor        | `Control + Shift + P`           |
| Select up                        | Editor        | `Shift + Up`                    |
| Show character palette           | Editor        | `Control + Command + Space`     |
| Show completions                 | Editor        | `Control + Space`               |
| Split selection into lines       | Editor        | `Command + Shift + L`           |
| Suggest                          | Copilot       | `Alt + \`                       |
| Tab                              | Editor        | `Tab`                           |
| Tab prev                         | Editor        | `Shift + Tab`                   |
| Toggle                           | Outline       | `Command + Shift + O`           |
| Toggle                           | Go To Line    | `Control + G`                   |
| Toggle code actions              | Editor        | `Command + .`                   |
| Toggle comments                  | Editor        | `Command + /`                   |
| Toggle soft wrap                 | Editor        | `Alt + Z`                       |
| Transpose                        | Editor        | `Control + T`                   |
| Undo                             | Editor        | `Command + Z`                   |
| Undo selection                   | Editor        | `Command + U`                   |
| Unfold lines                     | Editor        | `Alt + Command + ]`             |

#### Pane

| **Command**           | **Target**     | **Default Shortcut**   |
|-----------------------|----------------|------------------------|
| Activate item 1       | Pane           | `Control + 1`          |
| Activate item 2       | Pane           | `Control + 2`          |
| Activate item 3       | Pane           | `Control + 3`          |
| Activate item 4       | Pane           | `Control + 4`          |
| Activate item 5       | Pane           | `Control + 5`          |
| Activate item 6       | Pane           | `Control + 6`          |
| Activate item 7       | Pane           | `Control + 7`          |
| Activate item 8       | Pane           | `Control + 8`          |
| Activate item 9       | Pane           | `Control + 9`          |
| Activate last item    | Pane           | `Control + 0`          |
| Add tab to dock       | Dock           | `Command + Escape`     |
| Go back               | Pane           | `Control + `           |
| Go forward            | Pane           | `Control + _`          |
| Hide dock             | Dock           | `Shift + Escape`       |
| Remove tab from dock  | Dock           | `Command + Escape`     |
| Reopen closed item    | Pane           | `Command + Shift + T`  |
| Select next match     | Search         | `Command + G`          |
| Select prev match     | Search         | `Command + Shift + G`  |
| Split down            | Pane           | `Command + K, Down`    |
| Split left            | Pane           | `Command + K, Left`    |
| Split right           | Pane           | `Command + K, Right`   |
| Split up              | Pane           | `Command + K, Up`      |
| Toggle case sensitive | Search         | `Alt + Command + C`    |
| Toggle focus          | Project Search | `Command + F`          |
| Toggle focus          | Project Search | `Command + Shift + F`  |
| Toggle regex          | Search         | `Alt + Command + R`    |
| Toggle whole word     | Search         | `Alt + Command + W`    |

#### Buffer Search Bar

| **Command**       | **Target**    | **Default Shortcut**   |
|-------------------|---------------|------------------------|
| Dismiss           | Buffer Search | `Escape`               |
| Focus editor      | Buffer Search | `Tab`                  |
| Select next match | Search        | `Enter`                |
| Select prev match | Search        | `Shift + Enter`        |

#### Workspace

| **Command**         | **Target**        | **Default Shortcut**       |
|---------------------|-------------------|----------------------------|
| Activate pane 1     | Workspace         | `Command + 1`              |
| Activate pane 2     | Workspace         | `Command + 2`              |
| Activate pane 3     | Workspace         | `Command + 3`              |
| Activate pane 4     | Workspace         | `Command + 4`              |
| Activate pane 5     | Workspace         | `Command + 5`              |
| Activate pane 6     | Workspace         | `Command + 6`              |
| Activate pane 7     | Workspace         | `Command + 7`              |
| Activate pane 8     | Workspace         | `Command + 8`              |
| Activate pane 9     | Workspace         | `Command + 9`              |
| Deploy              | Diagnostics       | `Command + Shift + M`      |
| Focus dock          | Dock              | `Shift + Escape`           |
| New search          | Workspace         | `Command + Shift + F`      |
| Open keymap         | Zed               | `Command + K, Command + S` |
| Save all            | Workspace         | `Command + Alt + S`        |
| Toggle              | Theme Selector    | `Command + K, Command + T` |
| Toggle              | Language Selector | `Command + K, M`           |
| Toggle              | File Finder       | `Command + P`              |
| Toggle              | Command Palette   | `Command + Shift + P`      |
| Toggle              | Project Symbols   | `Command + T`              |
| Toggle focus        | Project Panel     | `Command + Shift + E`      |
| Toggle left sidebar | Workspace         | `Command + B`              |

#### Project Panel

| **Command**             | **Target**    | **Default Shortcut**        |
|-------------------------|---------------|-----------------------------|
| Collapse selected entry | Project Panel | `Left`                      |
| Copy                    | Project Panel | `Command + C`               |
| Copy path               | Project Panel | `Command + Alt + C`         |
| Copy relative path      | Project Panel | `Alt + Command + Shift + C` |
| Cut                     | Project Panel | `Command + X`               |
| Delete                  | Project Panel | `Backspace`                 |
| Expand selected entry   | Project Panel | `Right`                     |
| Paste                   | Project Panel | `Command + V`               |
| Rename                  | Project Panel | `F2`                        |
| Reveal in finder        | Project Panel | `Alt + Command + R`         |

#### Project Search Bar

| **Command**   | **Target**     | **Default Shortcut**   |
|---------------|----------------|------------------------|
| Search in new | Project Search | `Command + Enter`      |

#### Terminal

| **Command**                 | **Target**   | **Default Shortcut**        |
|-----------------------------|--------------|-----------------------------|
| Clear                       | Terminal     | `Command + K`               |
| Copy                        | Terminal     | `Command + C`               |
| Delete line                 | Terminal     | `Command + Backspace`       |
| Move to beginning of line   | Terminal     | `Command + Left`            |
| Move to end of line         | Terminal     | `Command + Right`           |
| Move to next word end       | Terminal     | `Alt + Right`               |
| Move to previous word start | Terminal     | `Alt + Left`                |
| Paste                       | Terminal     | `Command + V`               |
| Show character palette      | Terminal     | `Control + Command + Space` |
