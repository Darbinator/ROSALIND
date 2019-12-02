#!/usr/bin/env python

import sys
import os
import re
from math import *
import Bio
from Bio import SeqIO
from rosalind import nameToSeq
import itertools as it



with open(sys.argv[1],'r') as input_data:

	file = nameToSeq(input_data)

	seqs = list(file.values())





def agregateContigs(seqs) :

	longueur = 500



	count = 0

	contigs = []

	for seqC in range(len(seqs)):

		contigs.append('')

		for i in range(ceil(len(seqs[seqC])/2)+1):

			tot = 0
			for j in range(seqC+1,len(seqs)):

				if seqs[seqC][i:(i+longueur)] in seqs[j]:

					debut = seqs[seqC][:(i+longueur)]
					match = seqs[seqC][i:(i+longueur)]

					for k in range(floor(len(seqs[j])/2)):

						if seqs[j][k:].startswith(match):

							end = seqs[j][k+longueur:]

							if len(debut+end) > tot:

								contigs[seqC] = debut+end

								tot = debut + end

	contigs = [value for value in contigs if value != '']

	print(contigs)

	if len(contigs) > 1:

		return agregateContigs(contigs)
	
	else:

		return contigs


assembly = agregateContigs(seqs)

print(assembly[0])



substrings=[]

with open(sys.argv[1]) as f:
    f.readline()
    curr=''
    line=f.readline().strip()
    while line!='':
        if line[0]==">":
            substrings.append(curr)
            curr=''
        else:
            curr+=line
        line=f.readline().strip()
    substrings.append(curr)

def shortestSuperstring(seqs):
    left=[i for i in range(1,len(seqs))]
    candidate=seqs[0]
    while len(left)>0:
        for i in left:
            before=True
            after=True
            for j in reversed(range(int(len(seqs[i])/2),len(seqs[i]))):
                if after:
                    if candidate.endswith(seqs[i][:j]):
                        candidate=candidate+seqs[i][j:]
                        left.remove(i)
                        after=False
                if before:
                    if seqs[i].endswith(candidate[:j]):
                        candidate=seqs[i][:-j]+candidate
                        left.remove(i)
                        before=False
    return candidate

print(shortestSuperstring(substrings))

