from src.sentence_camle_case import sentence_camel_case
from src.sentence_camle_case import sentence_plain_english
def test_sentence_camel_case_return_upper_camel_if_true():
    assert sentence_camel_case("this sentence", True) == "ThisSentence"
    assert sentence_camel_case("This Bigger strange Sentence", True) == "ThisBiggerStrangeSentence"

def test_sentence_camel_case_return_lower_camel_if_false():
    assert sentence_camel_case("this sentence", False) == "thisSentence"

def test_sentence_plain_english():
    assert sentence_plain_english('thisBiggerStrangeSentence') == "This bigger strange sentence."