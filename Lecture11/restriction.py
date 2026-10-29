#this is a python script for question3
dna="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif="GAATTC"
n=dna.find(motif)
seq1=dna[0:n+1]
seq2=dna[n+1:]
print(n,"seq1:",seq1,len(seq1),"seq2:",seq2,len(seq2))
