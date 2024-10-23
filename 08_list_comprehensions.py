# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/list-comprehensions

# Le os valores de x, y, z e n
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Gera todas as combinações possíveis de i, j, k e filtra aquelas cuja soma i + j + k não seja igual a n
result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

# Imprime o resultado
print(result)

