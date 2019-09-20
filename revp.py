#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import nameToSeq

def reverseComplement(seq):
	complement = {'A':'T','T':'A','G':'C','C':'G'}

	reverseSeq = seq[::-1]
	revComplementSeq = ''

	for i in range(len(reverseSeq)):
		revComplementSeq += complement[reverseSeq[i]]

	return revComplementSeq


with open(sys.argv[1],'r') as file:
	seq = nameToSeq(file)

	seq = list(seq.values())[0]


for kmer in range(4,13):
	for i in range(len(seq)-kmer+1):

		if seq[i:(i+kmer)] == reverseComplement(seq[i:(i+kmer)]):
			print(str(i+1)+" "+str(kmer))

