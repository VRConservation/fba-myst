# This script builds pdfs of every chapter using the myst command myst build my-document.md --pdf

import subprocess
import glob

# Create chapters dictionary
chapters = glob.glob("chapters/*.md") 

# Run the myst build pdf for all markdown files in the chapters directory
for filename in chapters:
    try:
        subprocess.run(
            ["myst", "build", filename, "--pdf"],
            check=True
        )
        print(f"Built PDF for {filename}")
    except subprocess.CalledProcessError:
        print(f"Failed to build PDF for {filename}")