#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import nameToSeq
import itertools as it



# with open(sys.argv[1],'r') as input_data:

# 	file = input_data.readlines()

# 	seq = ''.join(file[0].split()).rstrip()

# 	number = int(file[1])

seq = " DNA"
number = 3

elements = []

for string in seq:
	for i in range(1,number+1):
		for elem in it.product(seq,repeat=i):
			if ''.join(list(elem)).startswith(string):
				elements.append(''.join(list(elem)))

print(elements)

for elem in elements:
	print(elem)