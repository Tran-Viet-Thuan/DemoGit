#!/usr/bin/python
"""reducer.py"""

import sys

current_title = None
total_price = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    title, price = line.split('\t', 1)

    # convert price to float
    try:
        price = float(price)
    except ValueError:
        # price was not a number, so silently ignore/discard this line
        continue

    # if this is the first title or the title has changed
    if current_title != title:
        # if this is not the first title, output the total price
        if current_title:
            print('%s\t%.2f' % (current_title, total_price))
        
        # reset the total price for the new title
        total_price = 0
        current_title = title
    
    # add the price to the total for the current title
    total_price += price

# output the total price for the last title
if current_title:
    print('%s\t%.2f' % (current_title, total_price))
