#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import nameToSeq

monoisotopic_table = '''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333'''

aa_to_mass = {}
for i in range(0,len(monoisotopic_table.split()),2):

	aa_to_mass[monoisotopic_table.split()[i]] = monoisotopic_table.split()[i+1]


tot = 0

with open(sys.argv[1],'r') as file:

	prot = file.readlines()[0].rstrip()

for aa in prot:
	tot += float(aa_to_mass[aa])

print(tot)