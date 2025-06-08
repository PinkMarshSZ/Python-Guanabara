#faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de aumento
sal = float(input('Digite seu salário: '))
valor = sal * (15/100)
novo = sal + valor
print('O seu novo salário é: {}'.format(novo))