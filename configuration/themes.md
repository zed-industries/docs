---
description: Zed UI and syntax themes explained
---

# Themes

{% hint style="warning" %}
Zed themes and their underlying systems are undergoing significant development. They should not be considered stable or final. Note that themes are subject to change or removal as the theme system moves towards a stable version.
{% endhint %}

A Zed Theme refers to and effects both the UI and the syntax highlighting of Zed.

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

In short, we want you to have the flexibility to express yourself while ensuring the editor remains a functional tool. We're working hard to create a theme system that strikes the right balance between customization and usability.

### Accessibility in Themes

{% hint style="warning" %}
Many of Zed's themes currently are largely inaccessible. We are working on a new theme system that will address this, but in the meantime, we recommend using `One Dark` if you need a theme that is more accessible.
{% endhint %}

_!!Under Construction!!_

### Roadmap

_Subject to change_

_!!Under Construction!!_

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
