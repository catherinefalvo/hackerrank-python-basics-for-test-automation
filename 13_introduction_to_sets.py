# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/py-introduction-to-sets

def average(array):
    # Converte a lista em um conjunto para remover duplicatas
    distinct_heights = set(array)
    
    # Calcula a media usando a soma dos valores no conjunto dividido pelo tamanho do conjunto
    return sum(distinct_heights) / len(distinct_heights)
