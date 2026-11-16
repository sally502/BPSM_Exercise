gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# Function to translate a DNA sequence into protein
def translate(dna, start, gencode):
    protein = ""

    # Read three bases at a time
    for i in range(start, len(dna) - 2, 3):
        codon = dna[i:i+3]

        # Translate using the genetic code dictionary
        if codon in gencode:
            protein += gencode[codon]
        else:
            protein += "X"

    return protein


# Function to generate the reverse complement
def reverse_complement(dna):
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse_dna = ""

    # Read the DNA sequence backwards
    for base in dna[::-1]:
        if base in complement:
            reverse_dna += complement[base]
        else:
            reverse_dna += "N"

    return reverse_dna


# Main programme
dna = input("Enter a DNA sequence: ").upper().strip()

# Translate the three forward frames
print("\nForward frames:")

for start in range(0, 3):
    protein = translate(dna, start, gencode)
    print(f"Frame +{start + 1}: {protein}")


# Generate the reverse complement
reverse_dna = reverse_complement(dna)

# Translate the three reverse frames
print("\nReverse frames:")

for start in range(0, 3):
    protein = translate(reverse_dna, start, gencode)
    print(f"Frame -{start + 1}: {protein}")
