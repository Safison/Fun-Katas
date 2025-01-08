from src.till_addition import till_addition

def test_till_addition_return_cash_sum():
    assert till_addition({ "1p": 1, "2p": 1 }) == '£0.03'
    assert till_addition({ "1p": 1, "2p": 1, "5p": 1, "10p": 1, "20p": 1 })=='£0.38'
    assert till_addition({ "5p": 1, "10p": 1, "20p": 1, "50p": 1, "£1": 1 })=='£1.85'