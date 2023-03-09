# JavaScript

### Editing JavaScript in Zed

When editing JavaScript, Zed provides code intelligence using the TypeScript compiler, via the [`typescript-language-server`](https://github.com/typescript-language-server/typescript-language-server) module.

#### Code formatting

Formatting on save is enabled by default for JavaScript, using TypeScript's built-in code formatting. But many JavaScript projects use other command-line code-formatting tools, such as [Prettier](https://prettier.io/). You can use one of these tools by specifying an _external_ code formatter for JavaScript in your settings. See the [configuration](../configuration/configuring-zed.md) documentation for more information.

For example, if you have Prettier installed and on your `PATH`, you can use it format JavaScript files by adding the following to your `settings.json`:

```json
{
  "languages": {
    "JavaScript": {
      "format_on_save": {
        "external": {
          "command": "prettier",
          "arguments": ["--stdin-filepath", "{buffer_path}"]
        }
      }
    }
  }
}
```
