#!/usr/bin/env python3
from argparse import ArgumentParser
import sys
import zipfile
import glob
import shutil
from os import path
import ntpath
import urllib.parse


# Step 1: Get the notion export zip file
# Step 2: Unzip the notion export zip file
# Step 3: Rename every file with a .md extension with the heading of the file and fix all the links
# Step 4: Rename all folder. Remove the "hash" from the ending of the folder name

# VARIABLES
FOLDER_EXTRACTION = "import to joplin"
MARKDOWN_EXTENSION = "md"
filename_backup = ""

## Step 1: Get the notion export zip file
# Delete the folder if it exists
if path.exists(FOLDER_EXTRACTION):
    shutil.rmtree(FOLDER_EXTRACTION)
# Get parameter
parser = ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)
parser.add_argument("-f", "--file", help="File to be processed", required=True)
try:
    args = parser.parse_args()
    filename_backup = args.file
except:
    parser.print_help()
    sys.exit(0)

## Step 2: Unzip the file
print("Unzipping backup file...")
with zipfile.ZipFile(filename_backup, "r") as zip_ref:
    zip_ref.extractall(FOLDER_EXTRACTION)
print("Unzipping done.")

## Step 3: Rename every file with a .md extension with the heading of the file and fix all the links
print("Renaming files and fixing links...")
# Get all markdown files
path_to_files = path.join(FOLDER_EXTRACTION, "**/*." + MARKDOWN_EXTENSION)
for filename in glob.iglob(path_to_files, recursive=True):
    # Get the heading of the file
    with open(filename, "r") as file:
        # Get the heading
        first_line = file.readline()
        heading = first_line.replace("# ", "").replace("\n", "")
        # Delete two first lines
        lines = file.readlines()
        lines_without_heading = lines[1:]
    # Write the file without the heading
    with open(filename, "w") as file:
        file.write("".join(lines_without_heading))
    # Rename the file
    new_filename = path.join(path.dirname(filename), heading + "." + MARKDOWN_EXTENSION)
    shutil.move(filename, new_filename)
    # Fix all the links
    old_filename_encoded = urllib.parse.quote(ntpath.basename(filename))
    heading_encoded = urllib.parse.quote(heading) + "." + MARKDOWN_EXTENSION
    for filename_to_fix in glob.iglob(path_to_files, recursive=True):
        with open(filename_to_fix, "r") as file:
            lines_to_fix = file.readlines()
        with open(filename_to_fix, "w") as file:
            text_to_write = "".join(lines_to_fix).replace(
                old_filename_encoded, heading_encoded
            )
            file.write(text_to_write)
