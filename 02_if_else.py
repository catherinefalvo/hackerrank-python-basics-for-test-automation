# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/py-if-else

n = int(input())  # Le a entrada e converte para inteiro

# Verifica se o numero e impar
if n % 2 != 0:
    print("Weird")  # Imprime "Weird" se for impar

# Verifica se o numero e par e esta entre 2 e 5
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")  # Imprime "Not Weird" para esse intervalo

# Verifica se o numero e par e esta entre 6 e 20
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")  # Imprime "Weird" para esse intervalo

# Se o numero for par e maior que 20
else:
    print("Not Weird")  # Imprime "Not Weird" para numeros pares > 20
