#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import rnaToProt
from rosalind import nameToSeq

with open(sys.argv[1],'r') as file:
	seqs = nameToSeq(file)

target = list(seqs.values())[0]
sub = list(seqs.values())[1]

toStart = 0

for letter in sub:
	for i in range(toStart, len(target)):
		if letter == target[i]:
			toStart = i + 1
			print(toStart , end=' ')

			break
print('')
