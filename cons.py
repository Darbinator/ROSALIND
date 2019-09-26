#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
import Bio
from Bio import SeqIO
from rosalind import nameToSeq
import itertools as it

with open(sys.argv[1],'r') as input_data:

 	file_ = nameToSeq(input_data)

 	seqs = list(file_.values())

A = ''
T = ''
C = ''
G = ''


for i in range(len(seqs[0])):

	counter = {'A':0, 'T':0, 'C':0, 'G':0}
	for j in range(len(seqs)):
		if seqs[j][i] =="A":
			counter['A'] +=1
		if seqs[j][i] =="T":
			counter['T'] +=1
		if seqs[j][i] =="C":
			counter['C'] +=1
		if seqs[j][i] =="G":
			counter['G'] +=1
	A+=str(counter['A'])
	T+=str(counter['T'])
	C+=str(counter['C'])
	G+=str(counter['G'])


	print(max(counter, key=counter.get),end='')
print()
print('A: ',end='')
for nucl in A:
	print(nucl,end=" ")
print()
print('C: ',end='')
for nucl in C:
	print(nucl,end=" ")
print()
print('G: ',end='')
for nucl in G:
	print(nucl,end=" ")
print()
print('T: ',end='')
for nucl in T:
	print(nucl,end=" ")


