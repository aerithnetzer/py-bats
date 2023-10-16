tbh this is jankey as hell but it works so whatever
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

## Markdown to JATSXML