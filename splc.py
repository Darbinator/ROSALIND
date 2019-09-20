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

seq = list(seqs.values())[0]
introns = list(seqs.values())[1:]

for intron in introns:
	seq = seq.replace(intron,'')

print(rnaToProt(seq.replace('T','U')))