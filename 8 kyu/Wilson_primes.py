import math

def is_wilson_prime(numero):
    #Primos de Wilson são maiores que 1
    if numero <= 1:
        return False
    
    #Calcula (P-1)!
    fatorial_p_minus_1 = math.factorial(numero - 1)

    # Calcula((P-1)! + 1) / (P * P))
    verificacao_wilson = (fatorial_p_minus_1 + 1) /(numero * numero)

    # Verifica se o resultado é um número inteiro
    return verificacao_wilson.is_integer()

print(is_wilson_prime(5))