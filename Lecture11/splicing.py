#last exercise for bpsm11, splicing out introns, this is still a python scirpt
dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1=dna[:63]
exon2=dna[90:]
codseq=exon1+exon2
ncodseq=len(codseq)
procod=ncodseq/len(dna)*100
print("length of the coding sequence:",ncodseq)
print("proportion:",str(procod)+"%")

intron=dna[63:89]
longseq=exon1+intron.lower()+exon2
print(longseq)

