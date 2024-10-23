# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/nested-list

# Inicializa uma lista vazia para armazenar os dados dos alunos
students = []

# Le o numero de alunos
for _ in range(int(input())):
    name = input()  # Le o nome do aluno
    score = float(input())  # Le a nota do aluno
    students.append([name, score])  # Adiciona nome e nota a lista students

# Encontra a segunda menor nota
scores = sorted(set([score for name, score in students]))  # Cria uma lista de notas unicas e ordenadas
second_lowest = scores[1]  # A segunda menor nota

# Cria uma lista com os nomes dos alunos que tem a segunda menor nota
names_with_second_lowest = [name for name, score in students if score == second_lowest]

# Ordena os nomes em ordem alfabetica e imprime um por linha
for name in sorted(names_with_second_lowest):
    print(name)
