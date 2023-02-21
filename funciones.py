"""
Your module description
"""
def sumar(x,y):
    return x+y
    
def es_primo(n):
    """
    Verifica si un número es primo
    """
    # Verifica si el número es menor que 2, ya que los números primos deben ser mayores o iguales a 2
    if n < 2:
        return False
    
    # Verifica si el número es 2, que es el único número primo par
    if n == 2:
        return True
    
    # Verifica si el número es par, ya que ningún número primo mayor que 2 puede ser par
    if n % 2 == 0:
        return False
    
    # Comprueba si el número es divisible por algún número impar menor que él
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

   

