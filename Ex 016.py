# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
num =float(input('Digite um número com casas decimais: '))
tr = trunc(num)
print('Sem casas decimais: {}'.format(tr))