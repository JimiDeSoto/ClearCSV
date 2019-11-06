#!csv/bin/python

import csv

#f = open('../pliki/pkp-test.txt')

with open('../pliki/pkp-test.txt', 'r') as f:
  reader = csv.reader(f)
  dane = list(reader)

print(dane)

for x in range(len(dane)): 
    print (dane[x])