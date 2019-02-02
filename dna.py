#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict

with open(sys.argv[1],'r') as file:

	countNucl = defaultdict(int)

	for nucl in file.readlines()[0].rstrip():
		countNucl[nucl] += 1

	print(str(countNucl['A'])+' '+str(countNucl['C'])+' '+str(countNucl['G'])+' '+str(countNucl['T']))
