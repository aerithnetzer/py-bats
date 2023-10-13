# This file handles transcoding the .bib file to a markdown file 

import os

def bib2md():
    """This function handles transforming the .bib file to markdown
    It crawls through all subdirectories and transforms each .bib file
    to a .md file with the same name
    """
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".bib"):
                bibfile = os.path.join(root, file)
                mdfile = bibfile[:-3] + "md"
                print("Transforming " + bibfile + " to " + mdfile + "")
                os.system("pandoc " + bibfile + " -s -f biblatex -t markdown -o " + mdfile + "")
        



