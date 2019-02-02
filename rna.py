#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict

with open(sys.argv[1],'r') as file:

	rna = ''

	for nucl in file.readlines()[0].rstrip():

		if nucl == 'T':
			rna+= 'U'

		else:
			rna+= nucl

	print(rna)