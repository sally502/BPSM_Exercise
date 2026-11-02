#this is a python script for mission 1
#exon1:1-63,exon2:91-end
dna1=open("plain_genomic_seq.txt").read()
dna1=dna1.upper()
#make sure its uppercase
dna2=open("clean.fasta").read()
dna2=dna2.upper()

cod1=dna1[0:63]+dna1[92:]
uncod1=dna1[63:92]
cod2=dna2[28:409]
uncod2=dna2[:28]+dna2[409:]

outfile=open("cod1.fasta","w")
outfile.write(f">dna1_cod1_{len(cod1)}\n{cod1}\n")
outfile=open("cod2.fasta","w")
outfile.write(f">dna2_cod2_{len(cod2)}\n{cod2}\n")
outfile=open("uncod1.fasta","w")
outfile.write(f">dna1_uncod1_{len(uncod1)}\n{uncod1}\n")
outfile=open("uncod2.fasta","w")
outfile.write(f">dna2_uncod2_{len(uncod2)}\n{uncod2}\n")




