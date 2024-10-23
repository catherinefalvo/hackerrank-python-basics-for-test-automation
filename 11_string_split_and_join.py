# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/python-string-split-and-join

def split_and_join(line):
    # Divide a string usando espacos e cria uma lista
    words = line.split(" ")
    
    # Junta a lista usando '-' como delimitador
    return "-".join(words)
