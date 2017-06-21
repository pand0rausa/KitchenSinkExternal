#!/usr/bin/python
import ipcalc
import sys

for x in ipcalc.Network(sys.argv[1]):
   print x
pip install ipcalc first
give it any cidr range it will print each individual ip in the range
python cidrtoips.py 1.1.1.1/8 
