valores=[]
maior=0
menor=0
for c in range(0,5):
    valores.append(int(input('Digite um valor')))
    if c==0:
        maior=menor= valores[c]
    else:
        if valores[c] > maior:
            maior=valores[c]
        if valores[c] < menor:
            menor=valores[c]
print (valores)
print (f'O maior valor foi {maior} nas posições ',end='.. ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}', end=' ')

print (f'\nO menor valor foi {menor} nas posições ', end='.. ')
for i, v in enumerate(valores):
    if v==menor:
        print(f'{i+1}', end=' ')
        