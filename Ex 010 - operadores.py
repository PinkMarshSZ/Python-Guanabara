#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
n = float(input('Digite quanto dinheiro possui: '))
convert = n / 3.27
print('O valor em dórales que conseguiria é de: {:3.4}'.format(convert))