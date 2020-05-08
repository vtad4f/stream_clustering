

import csv
import os
import random
import re


DATA_DIR = 'data'
WORD = re.compile(r'([a-zA-Z0-9_]+)', re.MULTILINE)


def ReadAll():
    """
        BRIEF  Read everything, remove newlines, add stars col
    """
    rows = []
    for n_stars in range(12 + 1):
        with open(os.path.join(DATA_DIR, '{0}.csv'.format(n_stars)), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Card Name']:
                    row['Stars'] = str(n_stars)
                    rows.append(row)
                else:
                    rows[-1]['Card Text'] += ' ;; ' + row['Card Text']
                    
    header_row = ['Stars'] + reader.fieldnames
    
    return header_row, rows
    
    
def ProcessText(rows):
    """
        BRIEF  Translate the card text into a word count
    """
    for row in rows:
        if row['Type'] == 'Normal Monster':
            row['Word Count'] = 0 # Just some lore, doesn't mean anything
        else:
            row['Word Count'] = len(WORD.findall(row['Card Text']))
            
            
def FixNumeric(rows):
    """
        BRIEF  Normalize the input
    """
    max_atk = 0
    max_def = 0
    max_ct = 0
    
    # Replace ??? with 0
    for row in rows:
        for label in ['ATK', 'DEF']:
            if '?' in row[label] or 'X' in row[label]:
                row[label] = '0'
                
    for row in rows:
        # print(row['Card Name']) # for debugging
        atk_ = int(row['ATK'])
        def_ = int(row['DEF'])
        ct   = int(row['Word Count'])
        
        if atk_ > max_atk:
            max_atk = atk_
        if def_ > max_def:
            max_def = def_
        if ct > max_ct:
            max_ct = ct
            
    for row in rows:
        row['attrib1'] = float(row['ATK'])/max_atk
        row['attrib2'] = float(row['DEF'])/max_def
        row['attrib3'] = float(row['Word Count'])/max_ct
        row['class']   = row['Stars']
        
def Write(header_row, rows, filename):
    """
        BRIEF  Write the specified columns to the file
    """
    with open(os.path.join(DATA_DIR, filename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header_row)
        for row in rows:
            writer.writerow(row[label] for label in header_row)
            
            
if __name__ == '__main__':
    """
        BRIEF  Parse and assemble a single csv with star columns
               https://www.yugiohcardguide.com/level/0.html
               all the way through .../12.html
               
               Note that the page contents have been copied manually
    """
    header_row, rows = ReadAll()
    Write(header_row, rows, 'stars.csv')
    
    ProcessText(rows)
    FixNumeric(rows)
    random.shuffle(rows)
    Write([
        'attrib1', # atk
        'attrib2', # def
        # 'attrib3', # word ct
        'class'    # level
    ], rows, 'stream1.csv')
    
    