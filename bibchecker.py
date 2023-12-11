import requests
import bibtexparser

def check_bib_entries(bib_file):
    # Load the .bib file using bibtexparser
    with open(bib_file, 'r') as f:
        bib_database = bibtexparser.load(f)

    # Iterate over all entries in the .bib file
    for entry in bib_database.entries:
        # Get the title and author of the entry
        title = entry.get('title', '')
        author = entry.get('author', '')

        # Call the API to check if the entry is valid
        response = requests.get(f'https://api.openalex.org/works?search={title}&{author}')

        # Check the response status code
        if response.status_code == 200:
            # The API returned a successful response
            result = response.json()
            if result['valid']:
                print(f'{entry["ID"]} is valid')
            else:
                print(f'{entry["ID"]} is invalid: {result["error"]}')
        else:
            # The API returned an error
            print(f'Error checking {entry["ID"]}: {response.status_code}')

# Example usage
check_bib_entries('/Users/aerith/Library/CloudStorage/OneDrive-NorthwesternUniversity/Documents/warlock/py_bats/production/3/index.bib')