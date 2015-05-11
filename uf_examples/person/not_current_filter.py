#!/usr/bin/env/python

"""
    not_current_filter.py -- handle people leaving uf.  Set their contact info and workingtitle to None to ensure
    these values are removed.
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2015, University of Florida"
__license__ = "New BSD License"
__version__ = "0.01"

from vivopump import read_csv_fp, write_csv_fp
import shelve
import sys

data_in = read_csv_fp(sys.stdin)
data_out = {}
not_current = 0
for row, data in data_in.items():
    new_data =dict(data)
    if new_data['current'] == 'no':  # the person has left.  Set their contact info to None
        not_current += 1
        new_data['remove'] = ''
        new_data['uri'] = ''
        new_data['current'] = ''
    data_out[row] = new_data
print >>sys.stderr, "Not current count", not_current
write_csv_fp(sys.stdout, data_out)





