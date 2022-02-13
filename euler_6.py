# Sum square difference
from math import pow
lista = list(range(1, 101))
soma = sum(lista)
soma_q = pow(soma, 2)  # quadrado da soma dos números da lista
lista_q = [pow(x, 2) for x in lista]
q_soma = sum(lista_q)  # soma dos quadrados dos números da lista
diferenca = soma_q - q_soma
print(diferenca)
