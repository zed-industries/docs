---
description: Zed UI and syntax themes explained
---

# Themes

{% hint style="warning" %}
Themes in Zed are heavily a work in progress. Themes are not guaranteed to stay the same or stay in the app as we iterate on the theme system.
{% endhint %}

The Theme currently refers to both the UI theme and the syntax theme. These are currently linked, but in the future will likely be separated or individually customizable.

### Known issues

-   Theme contrast is insufficient in places and inconsistent across the app
-   Spacing between groups and elements in places is insufficient or inconsistent
-   Semantic colors are not currently separated from syntax/accent colors (leads to some themes having awkward error colors, etc)

### Themes in Zed

Come discuss themes in more depth with the team in [our community forum](https://github.com/zed-industries/community/discussions).

### Experimental themes

Experimental themes are a way for us to share new themes before they are fully dialed in, or keep some themes that don't work quite right in Zed yet but people are enjoying.

These themes won't get support for any issues until we have had time to update them and move them out of our experiments.

There is no guarantee that experimental themes will be kept in the app or added to themes once added as an experiment.

#### Using experimental themes

You can enable experimental themes in your `settings.json`:

```json
"experiments": {
  "experimental_themes": true
}
```

### Planned features

We'll talk more soon about our plans for exactly what will be themable, but likely _most_(but not all) of the Zed UI should be able to be accessed by the theme.

Themes likely will start with only a small amount of customization (provide colors, recommend a font, etc) and grow more customizable over time.

**Custom themes**

-   There should be a list of curated themes available to download
-   Themes should be able to be loaded from a directory on the local machine
-   A format and builder should be available to help theme creators build themes for Zed.

### Theme FAQ

<details>

<summary>Can I create my own theme?</summary>

This is planned, though we don't have a timeline.

</details>

<details>

<summary>Can you add file type icons to themes?</summary>

Not yet, but it is [highly requested](https://github.com/zed-industries/community/issues/206) in our community board. If you would like to see this feature specifically, feel free to share any projects for sourcing these in the [GitHub issue](https://github.com/zed-industries/community/issues/206).

</details>
