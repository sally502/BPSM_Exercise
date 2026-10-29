#this is another python script for complementing DNA
dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
i=0
reverse=""
for i in range(len(dna)):
	if dna[i]=="A":
		reverse+="T"
	elif dna[i]=="T":
		reverse+="A"
	elif dna[i]=="C":
		reverse+="G"
	else:
		reverse+="C"
	i+=1
print(reverse)
