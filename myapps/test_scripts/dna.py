#dna script

def DNA_strand(dna):
    result = ""
    for i in dna:
        if i == "A": 
            result += "T"
        elif i == "T": 
            result += "A"
        elif i == "G": 
            result += "C"
        elif i == "C": 
            result += "G"
    print result


DNA_strand("AAAA")
DNA_strand("ATTGC")
DNA_strand("GTAT")
DNA_strand ("ATTGC") 
DNA_strand ("GTAT")             
