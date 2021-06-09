#!/usr/bin/python
import os
import sys
import fileinput

filenames = ['beamer.tex', sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]
with open(sys.argv[6], 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

#filenames = ['beamer.tex', sys.argv[1], sys.argv[2]]
#with open(sys.argv[3], 'w') as outfile:
#    for fname in filenames:
#        with open(fname) as infile:
#            outfile.write(infile.read())
