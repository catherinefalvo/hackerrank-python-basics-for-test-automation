# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/exceptions

# Le o numero de casos de teste
T = int(input())

# Itera sobre cada caso de teste
for _ in range(T):
    try:
        # Le os valores de a e b
        a, b = map(int, input().split())
        
        # Tenta realizar a divisao e imprime o resultado
        print(a // b)
    
    # Trata o erro de divisao por zero
    except ZeroDivisionError as e:
        print("Error Code:", e)
    
    # Trata o erro de valores invalidos (ex.: entrada que nao pode ser convertida para int)
    except ValueError as e:
        print("Error Code:", e)
