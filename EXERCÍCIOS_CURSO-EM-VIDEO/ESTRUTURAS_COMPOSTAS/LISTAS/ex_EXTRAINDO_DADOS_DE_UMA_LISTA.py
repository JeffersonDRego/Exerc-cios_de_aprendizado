lista=[]
c=0
while True:
    n=int(input('Digite um valor inteiro \n'))
    c+=1
    lista.append(n)

    resp=str(input('VOCÊ QUER CONTINUAR? [S/N]')).upper().strip()
    if resp in 'Nn':
        break
if 5 in lista:
    print (f'O número 5 está na lista')
else:
    print (f'O número 5 não está na lista')

print(f'Você digitou {c} valores')
lista.sort(reverse=True)
print(lista)

