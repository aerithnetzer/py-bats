# Convert references to markdown
import os

def bib2md():
    '''This function handles transforming the .bib file to markdown using pypandoc'''
    for root, _, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".bib"):
                bibfile = os.path.join(root, file)
                mdfile = os.path.join(root, "references.md")
                print("Transforming " + bibfile + " to " + mdfile + "")
                os.system("pandoc " + bibfile + " -s -f biblatex -t markdown -o " + mdfile + "")

def concatenate_yaml_file(input_dir):
    yamlfile = os.path.join(os.getcwd(), 'utils/article-metadata.yaml')
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file == 'references.md':
                mdfile = os.path.join(root, file)
                print("Writing yaml to " + mdfile + "")
                with open(yamlfile, 'r') as f:
                    data = f.read().splitlines()[:-1]
                    print(data)
                with open(mdfile, 'r') as f:
                    data2 = f.read().splitlines()[1:]
                    print(data2)
                with open(os.path.join(root, "index.md"), 'r+') as f:
                    content = f.read()
                    f.seek(0, 0)
                    f.write("\n".join(data + data2) + "\n" + content)

bib2md()
concatenate_yaml_file(os.getcwd())
