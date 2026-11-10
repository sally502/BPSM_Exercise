#this is a python script for k-mer counting
#now modify it to a kmer counting function
def kmer_counting(dna,k,n):
	kmer=[]
	for i in range(len(dna)):
		if i+k-1>=len(dna):
		#if there is no more enough bases
			break
		kmer.append(dna[i:i+k])
		#what we get is from i to i+k-1
	c={}
	#define an empty dictionary for counting
	for km in kmer:
		if km not in c:
		#if the new kmer is not already inside, add one
			c[km]=0
		#count+=1 when encounter each kmer
		c[km]+=1
	#try to take out value out of dictionary
	#if value>n means appear more than n, print the key which is the kmer
	output=[]
	for key,value in c.items():
		if value>n:
			output.append(key)
	return output


