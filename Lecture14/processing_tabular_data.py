#this is a python script for lecture14 exercise1 processing tabular data
#working file is data.csv
#contains fields in this order: 
#species name, sequence, gene name, expression level
#seperated by commas
data=open("data.csv").read()
#1.print out the gene names 
dataclean=data.strip().split("\n")
datadone=[]
for gene in dataclean:
	datadone.append(gene.split(","))
print("1.all genes name")
for gene in datadone:
	print(gene[2])
#2.all genes name that are between 90 and 110 bases long
print("2.all genes name that genes are between 90 and 110 bases long")
for gene in datadone:
	if len(gene[1])>=90 and len(gene[1])<=110:
		print(gene[2])
#3.genes whose AT content is less than 0.5 and whose expression level is greater than 200
print("3.AT content is less than 0.5 and expression level is greater than 200")
for gene in datadone:
	if int(gene[3])>200:
		seq=gene[1]
		if (seq.count("a")+seq.count("t"))/len(seq)<0.5:
			print(gene[2])
#4.print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Dm
print("4.begins with k or h except belong to Dm")
for gene in datadone:
	if gene[0]!= "Drosophila melanogaster":
		name=gene[2]
		if name.startswith("k"):
			print(name)
		elif name.startswith("h"):
			print(name)
#5.for each gene see its AT content
print("5.check on each gene's AT content")
for gene in datadone:
	at=(gene[1].count("a")+gene[1].count("t"))/len(gene[1])
	if at>0.65:
		print(gene[2],"high")
	elif at<0.45:
		print(gene[2],"low")
	else:
		print(gene[2],"medium")


