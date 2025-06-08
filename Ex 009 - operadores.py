# fazer uma tabuada 
n = int(input('Digite um número: '))
cont = 1
while cont < 11 :
    print('{0} x {1} = {2}'.format(cont,n,n*cont))
    cont += 1
print('Fim')