resp='S'
soma=0
cont=0
maior=0
menor=0
while resp in 'Ss':
    n=int(input('Digite um valor'))
    soma+=n
    cont+=1
    
    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resp=str(input('QUER CONTINUAR? [S/N]'))
print(f'A MÉDIA É {soma/cont}')
print(f'O MAIOR VALOR FOI {maior} E O MENOR FOI {menor}')
