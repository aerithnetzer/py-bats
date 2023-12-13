import os
import logging
import bibtexparser
from habanero import Crossref

def check_bib_entries(directory):
    # Iterate over all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.bib'):
                bib_file = os.path.join(root, file)
                log_file = os.path.join(root, 'api_log.txt')  # New line

                # Configure logging
                logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')  # Modified line

                # Load the .bib file using bibtexparser
                with open(bib_file, 'r') as f:
                    bib_database = bibtexparser.load(f)

                # Create a Crossref client
                cr = Crossref()

                # Iterate over all entries in the .bib file
                for entry in bib_database.entries:
                    # Get all elements in the entry
                    elements = entry.values()

                    # Search for the DOI using all elements
                    results = cr.works(query=' '.join(elements))
                    if 'items' in results['message'] and len(results['message']['items']) > 0:
                        doi = results['message']['items'][0].get('DOI')
                        logging.info(f"Elements: {elements}, DOI: {doi}")
                        print("Elements: ", elements)
                        print("DOI: ", doi)
                    else:
                        logging.info(f"No DOI found for elements: {elements}")
                        print("No DOI found for elements: ", elements)

check_bib_entries(os.getcwd())