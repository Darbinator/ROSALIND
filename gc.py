#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from rosalind import nameToSeq



with open(sys.argv[1],'r') as file:

	file = nameToSeq(file)

	print(file)

# 	GC = 0
# 	Seq = ''

# 	for ligne in file.readlines():

# 		if ligne.startswith(">"):

# 			SeqC = ligne.lstrip(">")

# 		elif ( ligne.count("C") + ligne.count("G") ) / len(ligne.rstrip()) > GC:

# 			Seq = SeqC
# 			GC = ( ligne.count("C") + ligne.count("G") ) / len(ligne.rstrip())

# 	print(Seq+str(GC))





