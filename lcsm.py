#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict
from Bio import SeqIO
from rosalind import nameToSeq

with open(sys.argv[1],'r') as file:

	seqs = nameToSeq(file)
	
	first_seq = list(seqs.values())[0]

	lenMotif = len(first_seq)
	
	
	sortir = False
	while lenMotif>0 and not sortir:

		motifs = [ first_seq[i:(i+lenMotif)] for i in range(len(first_seq)-lenMotif+1)]

		

		final_motif = []

		for motif in motifs:

				seqC = 1

				for seq in list(seqs.values()):

					continuer = True
					
					

					if continuer:


				

						

						if motif not in seq:

							continuer = False

						elif seqC == len(list(seqs.values())):

							final_motif.append(motif)

							sortir = True

						else:
							seqC += 1



					

		lenMotif-=1

print(final_motif)

