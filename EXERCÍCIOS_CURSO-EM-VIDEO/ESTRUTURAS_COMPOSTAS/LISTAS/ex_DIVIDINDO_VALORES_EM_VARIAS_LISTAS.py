lista=[]
lista_par=[]
lista_imp=[]

while True:
    lista.append(int(input('DIGITE UM VALOR INTEIRO.\n')))
    resp=str(input('Quer continuar? [S/N]\n'))
    if resp in 'Nn':
        break
    
for i, v in enumerate(lista):
    if v % 2==0:
        lista_par.append(v)
    elif v %2==1:
        lista_imp.append(v)
        
print (lista)
print (lista_par)
