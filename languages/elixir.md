# Elixir

- Tree Sitter: [tree-sitter-elixir](https://github.com/elixir-lang/tree-sitter-elixir)
- Language Server: [elixir-ls](https://github.com/elixir-lsp/elixir-ls)

### Formatting with Mix

A standard tool for formatting Elixir code is [Mix](https://hexdocs.pm/mix/Mix.html). With the following snippet in your `settings.json` file, Zed will format Elixir files on save using Mix:

```json
{
  "language_overrides": {
    "Elixir": {
      "format_on_save": {
        "external": {
          "command": "mix",
          "arguments": ["format", "--stdin-filename", "{buffer_path}", "-"]
        }
      }
    }
  }
}
```
