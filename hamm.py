#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict

with open(sys.argv[1],'r') as file:
	seq1,seq2 = map(str,file.readlines())

	print(seq1[0],seq2[0])
	hamming = 0

	for i in range(len(seq1.rstrip())):
		if seq1[i] != seq2[i]:
			hamming+=1

