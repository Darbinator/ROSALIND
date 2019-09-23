#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import nameToSeq
import itertools as it

with open(sys.argv[1],'r') as file:

	seqs = nameToSeq(file)

	seq = list(seqs.values())[0]
	print(seq)
array_kmer = []

for elem in it.product('ACGT',repeat=4):
	kmer = ''.join(list(elem))
	occ_kmer = 0

	for scan in range(len(seq)-3):
		if kmer == seq[scan:scan+4]:

			occ_kmer += 1

	array_kmer.append(str(occ_kmer))

print(' '.join(array_kmer))