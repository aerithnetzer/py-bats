# Puts the references generated in references.md into the index.md file metadata header
import os

def ref_in_article(input_dir):
    '''This function handles writing the references to the article metadata header'''
    # Find all instances of references.md and index.md files in the input directory
    ref_files = []
    index_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file == 'references.md':
                ref_files.append(os.path.join(root, file))
            elif file == 'index.md':
                index_files.append(os.path.join(root, file))
    # Check if there is at least one references file
    if not ref_files:
        print("No references file found in " + input_dir)
        return
    # Write the references to the header of each index.md file
    for index_file in index_files:
        # Open the references.md file and read the contents
        with open(ref_files[0], 'r') as f:
            ref_content = f.read()
        # Open the index.md file and read the contents
        with open(index_file, 'r') as f:
            index_content = f.read()
        # Split the index.md file into the header, references, and body
        index_parts = index_content.split('---')
        index_header = index_parts[1]
        index_references = index_parts[2]
        index_body = index_parts[3]
        # Write the references to the header
        with open(index_file, 'w') as f:
            f.write('---\n')
            f.write(index_header)
            f.write('references: |\n')
            f.write(ref_content)
            f.write(index_references)
            f.write('---\n')
            f.write(index_body)           
            print("References written to " + index_file + "")

input_dir = input('Enter the path to the directory containing the .md files:')
ref_in_article(input_dir)