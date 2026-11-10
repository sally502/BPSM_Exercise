#this is a python function that will take a DNA sequence along with an optional threshold 
#return TRUE or FALSE to indicate whether the DNA sequence contains 
#a high proportion of undermined bases(not ATCG)
def base_counter(dna,threshold=0.6):
	dnau=dna.upper()
	unde=len(dnau)-dnau.count("A")-dnau.count("T")-dnau.count("G")-dnau.count("C")
	pro=unde/len(dnau)
	if pro>=threshold:
		return "TRUE"
	else:
		return "FALSE"
