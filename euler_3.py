#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

from math import sqrt
num = 600851475143
lista = []
for i in range(2, int(sqrt(num) + 1)):
    if num % i == 0:
        lista.append(i)
        num /= i
print(lista[-1])



    

