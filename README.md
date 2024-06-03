While this code works and is all well and good, it is very specific to our workflow. I am creating a manuscript preparation package at [manus](https://github.com/aerithnetzer/manus)

# py-bats

## Introduction

This is a Python implemetation of a workflow engine used at Northwestern University Libraries for the *Bulletin of Applied Transgender Studies.* It is a simple workflow that by first converting the ```docx``` files to ```md``` files, then finding the references section of the md file. Then, a separate script will call the GPT API to generate a list of BibTeX references. Finally, the script will create a JATSXML file from the generated markdown file that has BibTex references.

## Docx to Markdown

From the ```py_bats``` directory, run the following command:

```bash
python3 docx2md.py -i <input_file> -o <output_file>
```

This will create a markdown file from the docx file. The markdown file will be saved in the ```output_file``` location.

## Markdown Extractor

You will also find a .txt file that contains the references in plaintext. We want to convert all of the citations to biblatex format. Use copilot, GPT, or zotero, as you wish. Make sure you change the file extension to ```.bib``` when you are done.


What is left to do in this project.
- [x] Automate the docx > markdown conversion
- [x] Add metadata to the markdown file
- [x] Split references into a txt file
- [x] Call GPT to convert the references to BibTeX
- [x] Add the BibTeX references to the markdown file
- [ ] Produce JATSXML file from the markdown file
- [ ] Parse author information and add to metadata section
