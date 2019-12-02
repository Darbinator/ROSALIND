import sys
import numpy

seqs = '''
>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA
'''


sequences = []

for i in range(1,len(seqs.split()),2):

	sequences.append(seqs.split()[i])

distance_C = []

for i in range(len(sequences)):
	
	for j in range(i,len(sequences)):
		if i != j:

			hamming = 0

			for nucl in range(len(sequences[i])):

				if sequences[i][nucl] != sequences[j][nucl]:

					hamming+=1

			distance_C.append(hamming/len(sequences[i]))


matrix_dist = len(sequences)

x = numpy.zeros([matrix_dist, matrix_dist])

x[numpy.triu_indices(matrix_dist, 1)] = distance_C

x += x.T

for liste in x:

	for li in liste:
		print(li,end=' ')
	print()


