# escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

celsius = float(input('Digite a temperatura em graus celsius: '))
fa = celsius * 1.8 + 32
print('A temperatura em Fahrenheit é de: {}'.format(fa))