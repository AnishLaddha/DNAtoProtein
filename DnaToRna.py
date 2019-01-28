print("DNA to RNA conversion.")
DnaInput = input("Enter DNA Strand: ")
DnaUpper = DnaInput.upper()
Dnalist = list(DnaUpper)
Rnalist = []
for base in Dnalist:
##    if base == "A" or base == "G" or base == "C" or base == "T":
        if base == 'A':
            Rnalist.append("G")
        elif base == "G":
            Rnalist.append("A")
        elif base == "C":
            Rnalist.append("T")
        elif base == "T":
            Rnalist.append("C")
        else:
            print("Please make sure your base is valid!")
            break
Rnaseq = ''.join(Rnalist)
print(Rnaseq)
