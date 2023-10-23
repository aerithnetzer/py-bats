from docx2bib import *
from gpt4bibtex import *
from bib2md import *

def main():
    # Convert docx to bib
    docx2bib()
    # Call GPT-3 to convert plaintext citations to biblatex
    gpt4bibtex()
    # Convert bib to markdown
    bib2md()

main()