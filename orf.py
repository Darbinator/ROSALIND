#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import *

with open(sys.argv[1],'r') as file:

	seqs = nameToSeq(file)

	seq = list(seqs.values())[0]

	for frame in range(3):

		for i in range(len(seq)-frame):

			print(frame, seq[frame+i:(frame+i+3)])


