# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto = float(input('Informe o preço do produto: '))
calc = produto * (5/100)
result = produto - calc
print('O produto com desconto de 5% é : {}'.format(result))