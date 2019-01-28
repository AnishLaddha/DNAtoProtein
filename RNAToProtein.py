##RNA to protein dictionary
import sys
dictionary = {"UUU":"Phenylalanine", "UUC":"Phenylaline", "UUA":"Leucine", "UUG":"Leucine",
    "UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG":"Serine",
    "UAU":"Tyrosine", "UAC":"Tyrosine", "UAA":"STOP", "UAG":"STOP",
    "UGU":"Cysteine", "UGC":"Cysteine", "UGA":"STOP", "UGG":"Tryptophan",
    "CUU":"Leucine", "CUC":"Leucine", "CUA":"Leucine", "CUG":"Leucine",
    "CCU":"Proline", "CCC":"Proline", "CCA":"Proline", "CCG":"Proline",
    "CAU":"Histidine","CAC":"Histidine", "CAA":"Glutamine", "CAG":"Glutamine",
    "CGU":"Arginine", "CGC":"Arginine", "CGA":"Arginine", "CGG":"Arginine",
    "AUU":"IsoLeucine", "AUC":"IsoLeucine", "AUA":"IsoLeucine", "AUG":"Methionine",
    "ACU":"Threonine", "ACC":"Threonine", "ACA":"Threonine", "ACG":"Threonine",
    "AAU":"Asparagine", "AAC":"Asparagine", "AAA":"Lysine", "AAG":"Lysine",
    "AGU":"Serine", "AGC":"Serine", "AGA":"Arginine", "AGG":"Arginine",
    "GUU":"Valine", "GUC":"Valine", "GUA":"Valine", "GUG":"Valine",
    "GCU":"Alanine", "GCC":"Alanine", "GCA":"Alanine", "GCG":"Alanine",
    "GAU":"Aspartate", "GAC":"Aspartate", "GAA":"Glutamate", "GAG":"Glutamate",
    "GGU":"Glycine", "GGC":"Glycine", "GGA":"Glycine", "GGG":"Glycine",}
x = 1
y = 3
i = 0
proteinlist = []
RNAinput = input("ENTER RNA STRAND: ")
RNAinput = list(' ' + RNAinput)
if len(RNAinput) % 3 != 1:
    print("Please enter complete codons.")
    sys.exit()
while y <= len(RNAinput):
    if i == 0:
        codon = ''.join(RNAinput[x-1:y+1])
        if ' ' in codon:
            codon = codon.strip()
        amino = dictionary[codon]
        if amino == 'Stop':
            proteinlist.append(amino)
            break
        else:
            proteinlist.append(amino)
            x = x+3
            y=y+3
            i = 1+1
    else:
        codon = ''.join(RNAinput[x:y+1])
        amino = dictionary[codon]
        proteinlist.append(" - ")
        if amino == 'Stop':
            proteinlist.append(amino)
            break
        else:
            proteinlist.append(amino)
            x = x+3
            y=y+3
        x = x+3
        y=y+3

    
print(''.join(proteinlist))
