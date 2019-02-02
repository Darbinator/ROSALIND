#!/usr/bin/env python

import sys
import os
import re
from collections import defaultdict

with open(sys.argv[1],'r') as file:

	print(file.readlines()[0].rstrip().replace("T", "U"))