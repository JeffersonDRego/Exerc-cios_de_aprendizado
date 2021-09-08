from random import randint
from time import sleep
lista=list()
jogos=list()
tot=1
x=int(input('DIGITE QUANTOS JOGOS DA MEGA SENA DESEJA GERAR: '))
while tot <= x:
    cont=0 
    while True:
        n=randint(1,60)
        if  n not in lista:
            lista.append(n)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
