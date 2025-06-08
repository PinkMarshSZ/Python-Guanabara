#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados
l = float(input('qual a largura da parede: '))
a = float(input('qual a altura da parede: '))
area = l * a
tinta = area / 2
print('A quantidade de tinta necessária será de: {} litros' .format(tinta))
