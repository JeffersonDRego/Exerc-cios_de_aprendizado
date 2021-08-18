num=cont=soma=0
num=int(input('Digite um valor'))
while num!=999:
    cont+=1
    soma+=num
    num=int(input('Digite um valor'))
print(f'A soma dos {cont} números é igual a {soma}')
