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

### Global

{% include "./key-bindings/global.md" %}

#### Editor

{% include "./key-bindings/editor.md" %}

#### Pane

{% include "./key-bindings/pane.md" %}

#### Buffer Search Bar

{% include "./key-bindings/buffer-search-bar.md" %}

#### Workspace

{% include "./key-bindings/workspace.md" %}

#### Following

{% include "./key-bindings/following.md" %}

#### Project Panel

{% include "./key-bindings/project-panel.md" %}

#### Project Search Bar

{% include "./key-bindings/project-search-bar.md" %}

#### Terminal

{% include "./key-bindings/terminal.md" %}
