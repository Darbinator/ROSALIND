#!/usr/bin/env python

from re import finditer
from sys import argv
from urllib.request import urlopen

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

uniprot = "http://www.uniprot.org/uniprot/P07204_TRBM_HUMAN.fasta"

f = urlopen(uniprot).read().decode('utf-8')

print(f)