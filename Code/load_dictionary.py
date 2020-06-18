import csv
# Load L1 dictionary from CSV-file
L1_DICTIONARY = dict()
with open('Dictionary/l1_lexicon.csv', mode='r') as csvfile:
    l1_lexicon = csv.reader(csvfile, delimiter=";")
    for row in l1_lexicon:
        if row[0] == 'keyword':
            continue
        L1_DICTIONARY[row[0]] = float(row[1])
# Load L2 dictionary from CSV-file
L2_DICTIONARY = dict()
with open('Dictionary/l2_lexicon.csv', mode='r') as csvfile:
    l1_lexicon = csv.reader(csvfile, delimiter=";")
    for row in l1_lexicon:
        if row[0] == 'keyword':
            continue
        if row[1] == 'positive':
            score = 1
        elif row[1] == 'negative':
            score = -1
        else:
            score = 0
        L2_DICTIONARY[row[0]] = score
