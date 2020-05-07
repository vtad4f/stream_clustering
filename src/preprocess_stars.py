

import csv
import os


DATA_DIR = 'data'


def ReadAll():
    """
        BRIEF  Read everything, remove newlines, add Stars col
    """
    rows = []
    for n_stars in range(12 + 1):
        with open(os.path.join(DATA_DIR, '{0}.csv'.format(n_stars)), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Card Name']:
                    row['Stars'] = str(n_stars)
                    for label in ['ATK', 'DEF']:
                        if '?' in row[label]:
                            row[label] = '0'
                    rows.append(row)
                else:
                    rows[-1]['Card Text'] += ' ;; ' + row['Card Text']
                    
    header_row = ['Stars'] + reader.fieldnames
    
    return header_row, rows
    
    
def Write(header_row, rows):
    """
        BRIEF   
    """
    with open(os.path.join(DATA_DIR, 'stars.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header_row)
        for row in rows:
            try:
                writer.writerow(row[label] for label in header_row)
            except UnicodeEncodeError:
                print("Invalid row! Name {0}".format(row["Card Name"]))
                
                
if __name__ == '__main__':
    """
        BRIEF  Parse each page of https://www.yugiohcardguide.com/level/0.html - .../12.html
               and assemble a single csv with star columns
               
               Note that the page contents have been copied by hand to individual csv's
               because that step was faster to do manually than automatically
    """
    header_row, rows = ReadAll()
    Write(header_row, rows)
    
    