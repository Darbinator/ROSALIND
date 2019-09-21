#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import nameToSeq

with open(sys.argv[1],'r') as file:

	numbers = file.readlines()[0].split()

	mounths, number = numbers[0], numbers[1].rstrip()

def fab(n,k):

	n = int(n)
	k = int(k)

	tot = 0

	youngs = 0
	adults = 1


		if i == 0:

			youngs += k

		else:

			youngsBef = youngs
			youngs = adults * k

			adults += youngsBef

	return(youngs+adults)


print(fab(mounths,number))


