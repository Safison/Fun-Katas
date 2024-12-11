def dna_pairs(dna_string=''):
    dna_list=[]
    dna_base = {
        'A':'T',
        'T':'A',
        'G':'C',
        'C':'G'
    }
    for letter in dna_string:
        if letter in dna_base:
            dna_list.append([letter, dna_base[letter]])
    return dna_list
    pass
