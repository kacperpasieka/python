import random
import sympy as primenumbers  # Moduł sympy zawiera funkcję isprime

# Losujemy liczbę z zakresu 1-100
losowa_liczba = random.randint(1, 100) 

# Sprawdzamy, czy liczba jest pierwsza
jest_pierwsza = primenumbers.isprime(losowa_liczba) #false

# Drukujemy wynik
print(f"Wylosowana liczba to: {losowa_liczba}")
if jest_pierwsza: #is_true
    print("Ta liczba jest liczbą pierwszą.")
else:
    print("Ta liczba nie jest liczbą pierwszą.")