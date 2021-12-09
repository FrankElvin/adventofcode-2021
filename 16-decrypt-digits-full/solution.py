
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
data_sum = 0

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

    #print("\tKnown digits: %s" %known_digits)

    if cipher_ready(cipher):
        data_sum += get_data(cipher, "1,4,7,8")
        continue
    
    chars_60 = []
    # seeking 9
    for item in cipher:
        if len(item.chars) == 6:
            #print("Possible 9: %s" %item.chars)

            for char in known_digits[4]:
                if char not in item.chars:
                    #print("Not 9 -> 6 or 0: %s" %item)
                    chars_60.append(item)
                    break
            else:
                item.mark(9)
                #print("Found item.chars for 9: %s" %item.chars)
                known_digits[9] = list(item.chars)

    if cipher_ready(cipher):
        data_sum += get_data(cipher, "9")
        continue

    # seeking 0 and 6
    for item in chars_60:
        for char in known_digits[7]:
            if char not in item.chars:
                item.mark(6)
                #print("Found item.chars for 6: %s" %item.chars)
                known_digits[6] = list(item.chars)
                break
        else:
            item.mark(0)
            #print("Found item.chars for 0: %s" %item.chars)
            known_digits[0] = list(item.chars)

    if cipher_ready(cipher):
        data_sum += get_data(cipher, "0, 6")
        continue

    chars_25 = []
    # seeking 3
    for item in cipher:
        if len(item.chars) == 5:
            for char in known_digits[1]:
                if char not in item.chars:
                    chars_25.append(item)
                    break
            else:
                item.mark(3)
                #print("Found item.chars for 3: %s" %item.chars)
                known_digits[3] = list(item.chars)

    if cipher_ready(cipher):
        data_sum += get_data(cipher, "3")
        continue
    
    # seeking 2 and 5
    c_unciphered = get_one_absent_character(known_digits[6])
    for item in chars_25:
        if c_unciphered in item.chars:
            item.mark(2)
        else:
            item.mark(5)

    if cipher_ready(cipher):
        data_sum += get_data(cipher, "2,5 - end")
        continue
    else:
        print("ERROR: Something went wrong for cipher: %s" %cipher)
        break

print("Overall data sum: %d" %data_sum)
