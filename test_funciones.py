"""from funciones import sumar,es_primo
def test_sumar():
    assert sumar(2,5) == 7
    assert sumar(2,2) == 4
    assert sumar(1,2) == 3
    
def test_es_primo():
    assert es_primo(4) is False
    assert es_primo(5) is True
    assert es_primo(9) is False
    assert es_primo(7) is True
"""
from funciones import cal_min
def test_cal_min():
    assert cal_min([4,5,8,643,284,548,5,487]) == 4
    assert cal_min([40,5,8,643,284,548,0,487]) == 0
    assert cal_min([45,5,8,-643,284,548,5,487]) == -643
    assert cal_min([47,5,8,643,284,548,5,487]) == 5
    assert cal_min([0.4,5,8,643,284,548,5,487]) == 0.4
