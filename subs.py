#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO

with open(sys.argv[1],'r') as file:

	seq,string = map(str,file.readlines())

	for i in range(len(seq.rstrip())):

		if seq.rstrip()[i:].startswith(string.rstrip()):

			print(str(i+1),end=" ")



