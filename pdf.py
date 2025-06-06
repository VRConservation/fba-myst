# This script builds pdfs of every chapter using the myst command myst build my-document.md --pdf

import subprocess
import glob

chapters = glob.glob("chapters/*.md") 


chapters = ["../chapters/*.md"]

for filename in chapters:
    try:
        subprocess.run(
            ["myst", "build", filename, "--pdf"],
            check=True
        )
        print(f"Built PDF for {filename}")
    except subprocess.CalledProcessError:
        print(f"Failed to build PDF for {filename}")