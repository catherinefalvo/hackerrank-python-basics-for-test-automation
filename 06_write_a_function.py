# Link: https://www.hackerrank.com/contests/python-basics-for-test-automation/challenges/write-a-function

def is_leap(year):
    # Inicializa a variavel leap como False
    leap = False
    
    # Verifica se o ano e divisivel por 4
    if year % 4 == 0:
        # Se for divisivel por 100, deve tambem ser divisivel por 400 para ser bissexto
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        # Se nao for divisivel por 100, apenas ser divisivel por 4 ja e suficiente
        else:
            leap = True
    
    return leap
