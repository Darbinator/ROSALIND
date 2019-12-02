import sys
from rosalind import reverseComplement
from collections import defaultdict
seqs = '''
>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC
'''

sequences = []

for i in range(1,len(seqs.split()),2):

	sequences.append(seqs.split()[i])



seqs_to_count = defaultdict(int)

for seq in sequences:

	curr = sorted([seq,reverseComplement(seq)])
	curr = str(curr) 
	seqs_to_count[curr] += 1

news = []
old = []

for seqs,count in seqs_to_count.items():

	if count == 2:

		news.append(seqs)

	else:

		old.append(seqs)

for seq in old:


	cleanold = seq.replace('[','').replace('\'','').replace(']','').replace(',','').replace(' ','')

	for seq2 in news:
		hamming = 0
		cleannew = seq2.replace('[','').replace('\'','').replace(']','').replace(',','').replace(' ','')

		for nucl in range(len(cleanold)):



			if cleanold[nucl] != cleannew[nucl]:

				hamming+=1


		if hamming == 2:

			print(seq.split(',')[0].lstrip('[\'').rstrip('\'')+"->"+seq2.split(',')[0].lstrip('[\'').rstrip('\''))




	