#this is a python script for exercise 1 processing DNA in a file
dna=open("input.txt").read()
dna_split=dna.splitlines("\n")
dna_clean=[]
for i in range(len(dna_split)):
	dna_clean.append(dna_split[i][14:])
	print(len(dna_clean[i]))

#first set a index, for each index inside range of dna_split,slicing it 
#to remove the first 14 base pairs, and append the trimmed one to clean
#print out the cleaned lengths
#almost forget to write a new file
out=open("cleanedseq.txt", "w")
for seq in dna_clean:
	out.write(seq)
out.close()
