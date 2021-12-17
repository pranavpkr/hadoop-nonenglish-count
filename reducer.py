# -*- coding: utf-8 -*-
"""
@author: pranav
"""

import sys

summ = 0
previouskey = None

for line in sys.stdin:
    # get key and english flag in data array
    data = line.split()
    #get key from input
    key = data[0]

    # if new file words start output previous files
    # non english word count
    if previouskey and previouskey != key:
        print(previouskey, summ)
        # reset summ for new file
        summ = 0
        
    # update previous row key with current key for next iteration
    previouskey = key
    summ+=int(data[1])

# output count of last file
if previouskey:
    print(key, summ)
