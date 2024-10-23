# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/python-string-formatting

def print_formatted(number):
    # Calcula o tamanho do numero binario mais longo
    width = len(bin(number)) - 2

    # Loop de 1 ate o numero especificado
    for i in range(1, number + 1):
        # Formata e imprime os valores decimal, octal, hexadecimal e binario
        # O :{width} garante que todos os valores estejam alinhados de acordo com o numero binario mais longo
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")
