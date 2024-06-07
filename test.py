import csv
import time
from digikeyAPI import *
dk = digikeyAPI()

_delay = 1  # in seconds

f = open('output.txt',"w",encoding='utf8')

with open('parts.csv', newline='') as csvfile:
    for row in csv.reader(csvfile):
        time.sleep(_delay)
        value = dk.get(row[1],'Operating Temperature')
        print(row[1])
        print(value)
        f.write(row[1])
        f.write("\t")
        f.write(str(value))
        f.write("\n")
f.close()