# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random

a1 = str(input('Digite o nome do Aluno: '))
a2 = str(input('Digite o nome do Aluno: '))
a3 = str(input('Digite o nome do Aluno: '))
a4 = str(input('Digite o nome do Aluno: '))

alunos = [a1,a2,a3,a4]

random.shuffle(alunos)

print('A ordem fica assim: {}'.format(alunos))