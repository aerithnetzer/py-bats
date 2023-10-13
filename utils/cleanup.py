# For an input directory, clean up all files that are not .docx files

import os

def cleanup(input_dir):
    """This function handles cleaning up the input directory
    It removes all files that are not .docx files
    """
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith(".docx"):
                file_to_remove = os.path.join(root, file)
                print("Removing " + file_to_remove)
                os.remove(file_to_remove)

input_dir = input('Enter the path to the directory containing the docx files:')

cleanup(input_dir)                