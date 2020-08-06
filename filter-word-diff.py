#!/usr/bin/env python

import sys
import re

header = ""
chunk = ""
skip = 0
change = False

COLOR="(\x1b\[\d*m)?"
def printChunk():
    global header, chunk, change
    if change:
        if header:
            print(header)
            header = ""
        print(chunk)
    chunk = ""
    change = False

for line in sys.stdin:
    if re.match("^"+COLOR+"diff --git", line):
        printChunk()
        header = ""
        skip = 5

    if (skip > 0):
        header += line
        skip -= 1
        continue
        
    if re.match("^"+COLOR+"~", line):
        continue

    if re.match("^"+COLOR+"@@", line):
        #new chunk. does the actual contains a change
        printChunk()

    chunk += line

    if not change:
        change = re.match("^"+COLOR+"\+", line) or re.match("^"+COLOR+"-", line)

printChunk()

