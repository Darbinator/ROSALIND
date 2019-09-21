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

seq1 = list(seqs.values())[0]
seq2 = list(seqs.values())[1]

transi = 0
transver = 0



for i in range(len(seq1)):

	if seq1[i] != seq2[i]:
		if (seq1[i] == "A" and seq2[i] == "G") or (seq1[i] == "G" and seq2[i] == "A")\
		or (seq1[i] == "C" and seq2[i] == "T") or (seq1[i] == "T" and seq2[i] == "C"):

			transi+= 1

		else:
			transver+= 1

print(transi/transver)


