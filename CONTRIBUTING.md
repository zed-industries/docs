# How to contribute to the Zed documentation

Thank you for your interest in contributing to the Zed documentation! We use Markdown and we welcome contributions from the community. This document describes how to get started.

## GitBook

The Markdown files you see in this repository are the source files for the Zed documentation. Each file corresponds to a page. We use [GitBook](https://www.gitbook.com/) to host the documentation. Every merge to the `main` branch triggers a synchronization action with GitBook, which publishes the documentation at [https://docs.zed.dev](https://docs.zed.dev). The structure of the documentation is defined in the `SUMMARY.md` file in this repository.

## Contributing

We welcome contributions from the community. If you'd like to contribute, please follow these steps:

- Fork this repository
- Make your changes on a new branch that has a descriptive and meaningful name
- Submit a pull request that targets the `main` branch of this repository

## Previewing your proposed changes

Unfortunately, there's no way currently to build the documentation locally and preview your changes. GitBook may enable previewing in the future. In the meantime, if you stick to simple Markdown, most things should render correctly. We will review your changes before merging them to make sure they look good.

## Proprietary GitBook content blocks

GitBook offers a number of proprietary content blocks that are not expressed in plain Markdown. For example the hint block:

```markdown
{% hint style="info" %}
This is a hint block
{% endhint %}
```

Or in some cases, GitBook will fall back to HTML. For example, images:

```html
<figure><img src="../.gitbook/assets/add-contacts.png" alt=""><figcaption><p>Adding a contact</p></figcaption></figure>
```

In these cases, there are two ways to figure out how to write the proper markup:

- Look at the source of the documentation in this repository to see how it's done
- Create a GitBook account (it's free) and experiment with your own git repository to test the content there first and see how GitBook exports it in Markdown.

## Assets

If you need to add an image or other asset to the documentation, please add it to the `.gitbook/assets` directory in this repository.

Best practices:

- If you can avoid adding a new image, please do so
- Reuse existing images if possible
- Use PNG format for images
- Keep the images as small as possible
- Use descriptive names for the images (they need to be unique across)
- Please use lowercase letters and dashes for the image names

## Table of contents in SUMMARY.md

The `SUMMARY.md` file in this repository is the table of contents for the documentation. It holds the whole structure of the documentation. If you want to propose changes to the structure of the documentation, please edit the `SUMMARY.md` file.

If you need to add a new file, please also add it to the `SUMMARY.md` file so that it will be included in the documentation. Otherwise, the next synchronization action with GitBook will not pick it up.
