#!/usr/bin/env python

import re
import sys
from urllib.request import urlopen

import ssl

ssl._create_default_https_context = ssl._create_unverified_context



with open(sys.argv[1],'r') as file:

	prots = [prot.rstrip() for prot in file.readlines()]

for prot in prots:

	try:
		f = urlopen("http://www.uniprot.org/uniprot/"+str(prot)+".fasta").read().decode('utf-8')

	except:
		continue

	name, seq = f.split("\n")[0], "".join(f.split("\n")[1:])
	
	iters = re.finditer("(?=N[^P][ST][^P])",seq)

	starts = ''
	for match in iters:
		starts+= str(match.start()+1)+' '

	if starts != '':
		print(prot)
		print(starts)
	

