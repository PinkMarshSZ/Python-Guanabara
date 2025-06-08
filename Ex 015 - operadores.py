#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa 60 por dia e  0.15 por km rodado.

Kmcorri = float(input('Quantos Km foram percorridos?'))
Quantdias = int(input('Quantos dias foi alugado?'))

calcdias = Quantdias * 60
calcKM = Kmcorri * 0.15

print('Preço a pagar: {}'.format(calcdias+calcKM))

