# This file will handle getting the references as plain text from the docx file

import os
import re
import os

def mdrefs2txt(input_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                input_file = os.path.join(root, file)

                with open(input_file, 'r') as f:
                    contents = f.read()

                # Split the contents into sections based on the section headings, allow for any heading that contains "References"
                # Find the section with a heading that contains "references", case insensitive
                sections = re.split(r'^#{0,6}.References.$', contents, flags=re.IGNORECASE | re.MULTILINE)
                for section in sections:
                    if 'References' in section:
                        print(f"Found references in {input_file}")
                        # Extract the text within that section
                        references_text = section.split('References')[1].strip()

                        # Write the extracted text to a new txt file in the same directory as the markdown file
                        output_file = os.path.splitext(input_file)[0] + '.txt'
                        with open(output_file, 'w') as f:
                            for line in references_text.split('\n'):
                                if line.strip():
                                    f.write(line + '\n')
                            print(f"References extracted from {input_file} and saved to {output_file}")
                        break


# Write the content of utils/article_metadata.yaml to the head of the markdown file

input_dir = os.path.join(os.getcwd(), 'production')

def docx2ref(input_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.docx'):
                input_file = os.path.join(root, file)
                print(f"Converting {input_file} to markdown")
                output_file = os.path.join(root, os.path.splitext(file)[0] + '.md')

                # Convert docx to md
                os.system(f"pandoc {input_file} --wrap none -o {output_file}")

                print(f"Converted {input_file} to {output_file}")

def docx2bib():
    docx2ref(input_dir)
    mdrefs2txt(input_dir)


docx2bib()

