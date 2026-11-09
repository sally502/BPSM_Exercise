#this is a python script for pairwise distances:how similar are two sequences
dna=['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
#outside loop:i
#second loop, from i to the end:j
#index for inside sequence:t
per=[[0 for x in range(len(dna))] for y in range(len(dna))]
for i in range(len(dna)):
	per[i][i]=1
#initialize the diagonal
for i in range(len(dna)-1):
	for j in range(i+1,len(dna)):
		c=0
		#count for same bases
		for t in range(len(dna[i])):
			if dna[i][t]==dna[j][t]:
				c+=1
		per[i][j]=c/len(dna[i])
		#fill in the downside triangle
		per[j][i]=per[i][j]
for row in per:
	print(row)
