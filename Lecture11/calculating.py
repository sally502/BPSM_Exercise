#this is a python  script for calculating A+T content
dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
counta=dna.count("A")
countt=dna.count("T")
countadd=counta+countt
pro=countadd/len(dna)

print("number of A:",counta,"number of T:",countt,"proportion:",pro)
