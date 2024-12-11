from src.dna_pairs import dna_pairs

def test_dna_pairs_get_empty_string_return_nested_list():
    input_dna_string= ''
    expect = []
    result = dna_pairs(input_dna_string)
    assert result == expect

def test_dna_pairs_recieve_G_return__nested_list_GC():
    input_dna_string= 'G'
    expect = [['G','C']]
    result = dna_pairs(input_dna_string)
    assert result == expect

def test_dna_pairs_recieve_AG_return__nested_list():
    input_dna_string= 'AG'
    expect = [ ["A", "T"], ["G", "C"] ]
    result = dna_pairs(input_dna_string)
    assert result == expect
