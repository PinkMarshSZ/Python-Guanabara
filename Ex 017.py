# faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo,
# e calcule e mostre o comprimento da hipotenusa
from math import pow, sqrt
n1 = float(input('Digite o cateto oposto: '))
n2 = float(input('Digite o cateto adjacente: '))
p1 = pow(n1, 2)
p2 = pow(n2,2)
sum = p1 + p2
hipo = sqrt(sum)
print('A hipotenusa é igual a: {}'.format(hipo))

