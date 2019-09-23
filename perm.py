#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Enumerating Gene Orders
Rosalind ID: PERM
Rosalind #: 019
URL: http://rosalind.info/problems/perm/
'''


import itertools as it

def factorial(n):
	'''Returns the value of n!'''
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)

with open('Inputs/rosalind_perm.txt') as input_data:
	perm_set = range(1, int(input_data.read())+1)

# Create a list containing ordered lists of all permutations.
perm_list = map(list,list(it.permutations(perm_set)))


print(str(factorial(len(perm_set))))

	# Write the permuations in the desired format.
for permutation in perm_list:
	print('\n'+' '.join(map(str,permutation)))


