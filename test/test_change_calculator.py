from src.change_calculator import change_calculator

def test_change_calculator_return_changes_if_in_change_list():
    assert change_calculator(1) == {'1':1}
    assert change_calculator(2) == {'2':1}
    assert change_calculator(5) == {'5':1}
    assert change_calculator(10) == {'10':1}

def test_change_calculator_return_changes_if_not_in_change_list():
    assert change_calculator(13) == {'10':1,'2':1,'1':1}
    assert change_calculator(18) == {'10':1,'5':1,'2':1,'1':1}
    
    pass