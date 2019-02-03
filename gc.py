#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from rosalind import nameToSeq



with open(sys.argv[1],'r') as file:

	seqs = nameToSeq(file)

	GC = 0
	seq_GC = ''

	for name,seq in seqs.items():
		if (( seq.count("C") + seq.count("G") ) / len(seq.rstrip())) * 100  > GC:

			GC = (( seq.count("C") + seq.count("G") ) / len(seq.rstrip())) * 100 
			seq_GC = name.lstrip(">")


	print(seq_GC+"\n"+str(GC))





