#multiple exons from genomic DNA
genomic=open("genomic_dna2.txt").read()
positions=open("exons.txt").read().rstrip("\n")
positions_s=positions.split("\n")
posi=[]
for pos in positions_s:
	posi.append(pos.split(","))
seq=""
for exon in posi:
	s=int(exon[0])
	e=int(exon[1])
	seq+=genomic[s:e+1]
out=open("exon_seqments.txt","w").write(seq)
#first split by \n to seperate each exon index, then seperate by comma 
