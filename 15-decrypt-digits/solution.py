
import csv
import argparse

from CipheredDigit import CipheredDigit
from uncipher_utils import *

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# process infile
ciphers = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        cipher = []

        for i in range(10):
            cipher.append(CipheredDigit(row[i]))

        for i in range(11, 15):
            cipher.append(CipheredDigit(row[i]))

        ciphers.append(cipher)

good_digits = { 2: 1, 4: 4, 3: 7, 7: 8 }
known_digits = { 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 0: [] }

print()
founded_1478 = 0
for cipher in ciphers:
    #print("Working with cipher: %s" %cipher)
    for item in cipher:
        if len(item.chars) in good_digits.keys():
            item.known = True
            item.unciphered = good_digits[len(item.chars)]
            #print("\titem.chars: %s -> %d" %(item.chars, good_digits[len(item.chars)]))
            known_digits[good_digits[len(item.chars)]] = list(item.chars)
        else:
            ...
            #print("\titem.chars: %s -> UNKNOWN" %(item.chars))

    # counting founded 1,4,7,8
    for item in cipher[-4:]:
        if item.known and item.unciphered in (1,4,7,8):
            founded_1478 += 1

print("Founded 1,4,7,8: %d" %founded_1478)
