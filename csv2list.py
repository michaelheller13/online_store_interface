"""Reads a csv file, then converts it into a list of lists

https://stackoverflow.com/questions/24662571/python-import-csv-to-list
2017-07-18

With minor modifications to read .csv files with any name.
Usage:
python csv2list csv_file_name.csv
"""
import sys
import csv

if len(sys.argv) != 2:
    print("Usage: python " + sys.argv[0] + " csv_file_name.csv")
    sys.exit()

csvfile = open(sys.argv[1], 'r')

# first read the title line and split into a list of fields
title_line = csvfile.readline()
print(title_line)
title_fields = title_line.split(',')

reader = csv.reader(csvfile)
your_list = list(reader)

print(your_list)
