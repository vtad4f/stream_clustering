

from collections import OrderedDict
import csv
import json
import os


DATA_DIR = 'data'


if __name__ == '__main__':
    """
        BRIEF  Parse https://db.ygoprodeck.com/api/v7/cardinfo.php
               and translate it to a csv file so that the multiflow
               FileStream can read it.
    """
    # read everything
    with open(os.path.join(DATA_DIR, 'prices.json'), 'r') as f:
        content = json.loads(f.read(), object_pairs_hook=OrderedDict)['data']
        
    header_row = content[0].keys()
    
    # write everything
    with open(os.path.join(DATA_DIR, 'prices.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header_row)
        for row in content:
            try:
                writer.writerow(row.values())
            except UnicodeEncodeError:
                print("Invalid row! ID {0}".format(row["id"]))
                
                