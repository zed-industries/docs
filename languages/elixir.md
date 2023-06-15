# Elixir

- Tree Sitter: [tree-sitter-elixir](https://github.com/elixir-lang/tree-sitter-elixir)
- Language Server: [elixir-ls](https://github.com/elixir-lsp/elixir-ls)

### Formatting with Mix

If you prefer to format your code with [Mix](https://hexdocs.pm/mix/Mix.html), use the following snippet in your `settings.json` file to configure it as an external formatter.  Formatting will occur on file save.

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
