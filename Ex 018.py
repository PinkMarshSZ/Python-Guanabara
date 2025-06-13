# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse angulo
import math
ang = float(input('Digite um ângulo: '))
angulo_radianos = math.radians(ang)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print('O valor do seno é: {0}, O valor do cosseno:{1}, O valor da tangente é: {2}'.format(seno,cosseno,tangente))