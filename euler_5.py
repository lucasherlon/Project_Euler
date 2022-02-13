# Smallest multiple
''' 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder. What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?'''


def divisivel(lista, num):
    for i in lista:
        if num % i != 0:
            return False
        else:
            continue
    return True


lista = list(range(1, 21))
n = 2520 #O número 'n' deve ser o máximo divisor conhecido do número que procuramos
while True:
    if divisivel(lista, n):
        print(n) 
        break
    else:
        n += 2520 #O número a ser adicionado dever ser igual ao valor original do 'n'
