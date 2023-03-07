---
description: Zed UI and syntax themes explained
---

# Themes

{% hint style="warning" %}
Zed themes and their underlying systems are undergoing significant development. They should not be considered stable or final. Note that themes are subject to change or removal as the theme system moves towards a stable version.
{% endhint %}

A Zed Theme refers to and affects both the UI and the syntax highlighting of Zed.

We will not have formal UI and syntax themes the like Atom, but will provide a way to override syntax styles (and more) from a single theme.

---

## Philosophy

The theme you use in your editor is deeply personal. Whether it is focused on utterly on function, or just an asthetic that you enjoy, ultimately, a theme should be a reflection of what is imporant to you.

We want to provide the right balance of good defaults and a powerful toolkit to make your editor your own.

In practice, this means:

- **Default Themes**: We want to provide a set of themes that are beautiful, usable and accessible out of the box. Additionally, we would love to provide default versions of prominent themes that developers are already familiar with where possible.

- **Powerful Customization**: We want to provide a way to customize your theme to your heart's content. This could mean taking a default theme and just changing a few colors, or it could mean creating your own theme from scratch.

- **Community**: We want to enable the community to create and share their themes. We will provide a way to load themes in the app, and a toolkit for building themes.

- **Accessibility**: We want to ensure that the default themes are accessible to all users. We will also provide guardrails for you to ensure that your custom themes are accessible. We won't, however, require you to make your theme accessible. We may tag themes that don't meet our accessibility standards as such, but we won't prevent you from using or sharing them.

We want you to have the flexibility to express yourself while ensuring the editor remains a functional tool. We're working hard to create a theme system that strikes the right balance between customization and usability.

### Accessibility in Themes

{% hint style="warning" %}
Many of Zed's themes currently are largely inaccessible. We are working on a new theme system that will address this, but in the meantime, we recommend using `One Dark` if you need a theme that is more accessible.
{% endhint %}

_!!Under Construction!!_

### Roadmap

_Subject to extreme change. This is to provide some insight into our plans around themes, and the amount of work that needs to go into the system before user themes can be launched._

_!!Under Construction!!_

- [x] **Default Palette**: The set of colors that Zed pulls from to build it's default themes and uses for semantic colors. This is almost entirely internal facing, but eventually we will expose it for use in custon themes.
- [ ] **Syntax Overrides**: The ability to override syntax colors from a theme. This will ship before public beta to allow us to correctly color the One theme family, which will continue to be the default for now.
- [ ] **Theme 1.0 Specification**: The spec for a theme. This will include the ability to override syntax colors, as well as UI colors. We likely will define more features than we will build at the start, but this will allow us to add more features in the future without breaking existing themes.
- [ ] **Port Existing Themes**: We will need to bring our existing themes up spec. Some themes will likely be removed or replaced at this point.
- [ ] **Token Driven UI**: This is internal facing. Use standard design tokens to style every element in the UI. This is a pretty big step that won't have a lot of immediatly visible impact, but will allow us to build UI Overrides, and significantly improve the way we style every part of the app.
- [ ] **Loading Themes**: The ability to load a theme from disk.
- [ ] **UI Overrides**: Similar to syntax overrides, but for UI elements. This would, for example, allow you to change the color of the sidebar background or the label color of an active tab.

---

## Known issues

- **Low contrast**: The current contrast beween elements from theme to theme ranges from ok to very low. This will be addressed when we ship the tokens portion of our new system (see roadmap below)
- **The colors of errors/warnings/something else look wrong**: This comes from our internal lack of (internal) color overrides. Our semantic colors are not separated from syntax/accent colors currently, which leads to leads to some themes having awkward error colors, etc. This will be tackled in the very near future.

_!!Under Construction!!_

## Non-theme related issues

- Spacing between groups and elements in places is insufficient or inconsistent

_!!Under Construction!!_

---

### Theme FAQ

_!!Under Construction!!_

<details>

<summary>Can I create my own theme?</summary>

This is planned, though we don't have a timeline.

</details>

<details>

<summary>Can you add file type icons to themes?</summary>

Not yet, but it is [highly requested](https://github.com/zed-industries/community/issues/206) in our community board. If you would like to see this feature specifically, feel free to share any projects for sourcing these in the [GitHub issue](https://github.com/zed-industries/community/issues/206).

</details>
