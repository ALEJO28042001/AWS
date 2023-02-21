from funciones import *
def test_sumar(x,y):
    assert sumar(2,5) == 7
    assert sumar(2,2) == 4
    assert sumar(1,2) == 3
    
def test_es_primo():
    assert es_primo(4) == True
    assert es_primo(5) == True
    assert es_primo(9) == True
    assert es_primo(7) == True