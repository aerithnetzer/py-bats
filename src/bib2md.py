# Convert references to markdown
import os

def bib2md(input_dir):
    '''This function handles transforming the .bib file to markdown using pypandoc'''
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".bib"):
                bibfile = os.path.join(root, file)
                mdfile = bibfile[:-4] + ".md"
                print("Transforming " + bibfile + " to " + mdfile + "")
                os.system("pandoc " + bibfile + " -s -f biblatex -t markdown -o " + mdfile + "")

input_dir = input('Enter the path to the directory containing the .bib files:')
bib2md(input_dir)