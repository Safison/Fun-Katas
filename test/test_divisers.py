from src.calculate_divisers import calculatedivisers

def test_divisers_sum_multiples_of_three_five_belolw_num():
    assert calculatedivisers(6) == 8
    assert calculatedivisers(10)==23
    assert calculatedivisers(12) == 33