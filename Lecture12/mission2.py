#this is a python script to run blast for 2 sequnce
#importing os
import os
os.system("blastx -query cod1.fasta -db nem -outfmt 7 > cod1.out")
os.system("blastx -query cod2.fasta -db nem -outfmt 7 > cod2.out")
