import nbformat as nbf
from glob import glob
import re
# Collect a list of all notebooks in the content folder
notebooks = glob("./*.ipynb", recursive=False) # recursive = True to search in subfolders


# Search through each notebook and look for the text, add a tag if necessary

def musterloesung(notebooks,hide_musterloesung = True):
    for ipath in notebooks:
        ntbk = nbf.read(ipath, nbf.NO_CONVERT)

        for cell in ntbk.cells:
            cell_tags = cell.get('metadata', {}).get('tags', [])
            if "Musterlösung" in cell["source"]:
                cell_tags = [i for i in cell_tags if not re.match("remove|hide-.+",i)]
                if hide_musterloesung: cell_tags.append("remove-cell")    
            if len(cell_tags) > 0:
                cell['metadata']['tags'] = cell_tags

        nbf.write(ntbk, ipath)
        
musterloesung(notebooks, True)