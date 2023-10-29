# Import Notion to Joplin

Simple script to convert a Notion export to a Joplin import (MD - Markdown directory).

## Requirements

- Python 3.6+

## Usage

1. Export your Notion workspace as Markdown & CSV (with subpages) and unzip the archive.

2. Download script.

```bash
curl -O https://github.com/tanrax/notion-to-joplin/raw/main/notion-to-joplin.py
```

3. Run the script:

```bash
python3 notion-to-joplin.py -f <path/to/your/export>
```

Example:

```bash
python3 notion-to-joplin.py -f b25c8352-f87b-4b5b-ce0a-61d09c5bd81b_Export-9e0c6ec4-762b-4d70-b30e-045ece8b4722.zip
```

4. Import the generated folder into Joplin.

You can now import the folder `import to joplin` to Joplin (File > Import > MD - Markdown directory).
