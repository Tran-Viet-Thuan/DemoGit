#!/usr/bin/python
"""mapper.py"""

import sys
import csv

# input comes from STDIN (standard input)
for line in sys.stdin:
    # Parse the input as CSV
    row = line.strip().split(',')
    
    # Extract the book title and price
    title = row[0]
    price = row[1]
    
    # Output the title and price to be processed by the reducer
    print('%s\t%s' % (title, price))
