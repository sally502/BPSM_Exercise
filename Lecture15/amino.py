#this is a python script for lecture 15 exercise 1
#write a python function that takes two arguments:a protein sequence and an amino acid residue code
#returns the percentage of the protein that the amino acid makes up
def amino_acid_percentages(protein,amino_list=["A","I","L","M","F","W","Y","V"]):
	c=0
	for amino in amino_list:
		for i in protein:
			if amino==i:
				c+=1
	per=c/len(protein)*100
	return per

