# Contributing to key bindings

### Setup

The Markdown tables in the `configuration/key-bindings.md` are generated via a script, `script/key-bindings/main.py`.  In order to run this script, you'll need to install Python and complete the following setup instructions:

1. Change directories to the key bindings script directory: `cd script/key-bindings`
2. Create a virtual environment: `<path to python interpreter> -m venv <path to virtual_environment_directory>`
3. Install the requirements: `pip install -r requirements.txt`
4. Activate the environment: `source virtual_environment/bin/activate`

### Updating key binding content

The script works by:

1. Taking in Zed's default key bindings file (`script/key-bindings/source/default.json`)
2. Creating Markdown tables based on the key bindings file
3. Injecting those Markdown tables into a template file (`script/key-bindings/source/key-bindings-template.md`)
4. Writing the final product to the document file (`configuration/key-bindings.md`)

Note: Don't modify `configuration/key-bindings.md` directly - only files within the `script/key-bindings/source/` directory should be modified.  You'll notice that we have a `.gitignore` line `script/key-bindings/source/default.json`.  It is expected that you make this file and populate it by:

1. Running the `zed: open default keymap` command in Zed
2. Copying and pasting the contents into `script/key-bindings/source/default.json`

Once the updates are in place, run the script via `python main.py`.
