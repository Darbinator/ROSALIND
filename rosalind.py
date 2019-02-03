#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict



def nameToSeq(file):

	''' Dictionnaire associant le nom d'une séquence et la séquence,
	à partir d'un fichier FASTA multilines '''

	lignes = file.readlines()

	sequences = {}

	for ligne in lignes:

		if ligne.startswith(">"):
			seq = ligne.rstrip()
			sequences[seq] = ''

		else:
			sequences[seq] += ligne.rstrip()

	return sequences










