# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = float(input('Digite o valor dos metros: '))
c = m * 100
mi = m * 1000
print('O valor em centimetros é de: {0}, o valor em milimetros é: {1}'.format(c,mi))