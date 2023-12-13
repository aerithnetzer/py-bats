import logging
from habanero import Crossref
import bibtexparser

def check_bib_entries(bib_file):
    # Configure logging
    logging.basicConfig(filename='api_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Load the .bib file using bibtexparser
    with open(bib_file, 'r') as f:
        bib_database = bibtexparser.load(f)

    # Create a Crossref client
    cr = Crossref()

    # Iterate over all entries in the .bib file
    for entry in bib_database.entries:
        # Get the title and author of the entry
        title = entry.get('title', '').replace('{', '').replace('}', '')
        author = entry.get('author', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '')

        # Search for the DOI using the title and author
        results = cr.works(query=title, query_author=author)
        if 'items' in results['message'] and len(results['message']['items']) > 0:
            doi = results['message']['items'][0].get('DOI')
            logging.info(f"Title: {title}, Author: {author}, DOI: {doi}")
            print("Title: ", title)
            print("Author: ", author)
            print("DOI: ", doi)
        else:
            logging.info(f"No DOI found for title: {title}")
            print("No DOI found for title: ", title)

check_bib_entries('/Users/aerith/warlock/py_bats/production/1/index.bib')