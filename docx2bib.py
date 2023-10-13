# This file will handle getting the references as plain text from the docx file

import os
import pypandoc
import re
import os


def docx2ref(input_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.docx'):
                input_file = os.path.join(root, file)
                output_file = os.path.splitext(input_file)[0] + '.md'

                # Convert docx to md
                pypandoc.convert_file(input_file, 'md', outputfile=output_file)


def mdrefs2txt(input_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                input_file = os.path.join(root, file)

                with open(input_file, 'r') as f:
                    contents = f.read()

                # Split the contents into sections based on the section headings
                sections = re.split(r'(?<=\n)#+\s+', contents)

                # Find the section with the heading "references"
                for section in sections:
                    if section.startswith('References'):
                        # Extract the text within that section
                        references_text = section.split('References')[1].strip()

                        # Write the extracted text to a new txt file in the same directory as the markdown file
                        output_file = os.path.splitext(input_file)[0] + '.txt'
                        with open(output_file, 'w') as f:
                            f.write(references_text)
                            print(f"References extracted from {input_file} and saved to {output_file}")
                        break

def call_cli_on_txt_files(directory_path):
    cli_function = 'AnyStyle parse'
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                output_file = os.path.splitext(file_path)[0] + '.bib'
                os.system(f"{cli_function} {file_path} > {output_file}")

input_dir = input('Enter the path to the directory containing the docx files:')

docx2ref(input_dir)
mdrefs2txt(input_dir)
call_cli_on_txt_files(input_dir)