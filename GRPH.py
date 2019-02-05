#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import nameToSeq

with open(sys.argv[1],'r') as file:

	seqs = nameToSeq(file)

	dico_Nodes = defaultdict(list)

	for name,seq in seqs.items():

		for name2,seq2 in seqs.items():

			if name != name2 and seq[-3:] == seq2[:3]:

				dico_Nodes[name.lstrip(">")].append(name2.lstrip(">"))


for a,b in dico_Nodes.items():

	for c in b:

		print(a+" "+c)

