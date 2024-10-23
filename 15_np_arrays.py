# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/np-arrays

def arrays(arr):
    # Converte a lista de strings em uma array NumPy de floats
    arr = numpy.array(arr, float)
    # Retorna o array invertido
    return arr[::-1]
