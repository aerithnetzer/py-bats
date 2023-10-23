# Convert references to markdown
import os

def bib2md():
    '''This function handles transforming the .bib file to markdown using pypandoc'''
    for root, _, files in os.walk(os.getcwd() + '/production'):
        for file in files:
            if file.endswith(".bib"):
                bibfile = os.path.join(root, file)
                mdfile = os.path.join(root, "references.md")
                print("Transforming " + bibfile + " to " + mdfile + "")
                os.system("pandoc " + bibfile + " -s -f biblatex -t markdown -o " + mdfile + "")

bib2md()