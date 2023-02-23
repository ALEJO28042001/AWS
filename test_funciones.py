from funciones import sumar,es_primo
def test_sumar():
    assert sumar(2,5) == 7
    assert sumar(2,2) == 4
    assert sumar(1,2) == 3
    
def test_es_primo():
    assert es_primo(4) is False
    assert es_primo(5) is True
    assert es_primo(9) is False
    assert es_primo(7) is True