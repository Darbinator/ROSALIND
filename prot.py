#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO


codonTable = ''' UUU F      CUU L      AUU I      GUU V
	UUC F      CUC L      AUC I      GUC V
	UUA L      CUA L      AUA I      GUA V
	UUG L      CUG L      AUG M      GUG V
	UCU S      CCU P      ACU T      GCU A
	UCC S      CCC P      ACC T      GCC A
	UCA S      CCA P      ACA T      GCA A
	UCG S      CCG P      ACG T      GCG A
	UAU Y      CAU H      AAU N      GAU D
	UAC Y      CAC H      AAC N      GAC D
	UAA Stop   CAA Q      AAA K      GAA E
	UAG Stop   CAG Q      AAG K      GAG E
	UGU C      CGU R      AGU S      GGU G
	UGC C      CGC R      AGC S      GGC G
	UGA Stop   CGA R      AGA R      GGA G
	UGG W      CGG R      AGG R      GGG G '''


with open(sys.argv[1],'r') as file:

	seq = file.readline().rstrip()
	prot=''

	codon_to_aa = {}

	for i in range(0,len(codonTable.split()),2):
		codon_to_aa[codonTable.split()[i]] = codonTable.split()[i+1]

	for j in range(0,len(seq),3):

		if codon_to_aa[seq[j:j+3]] != "Stop":
			prot += codon_to_aa[seq[j:j+3]]

		else:
			break

	print(prot)