lista=[]
dados=[]
obeso=[]
leves=[]
while True:
    dados.append(str(input('NOME:\n')))
    dados.append(float(input('PESO:\n')))
    lista.append(dados[:])
    dados.clear()
    resp=str(input('CONTINUAR? [S/N]\n'))
    if resp in 'Nn':
        break
print(f'VOCÊ CADASTROU {len(lista)} PESSOAS')


for pos, p in enumerate(lista):
    if p[1]>100.00:
        if pos>=0:
           obeso.append(p)
        elif p[1]>obeso[1] or p[1]==obeso[1]:
            obeso.append(p)
    elif p[1]<70:
        if pos>=0:
            leves.append(p)
        
print (f'Os mais pesados são:')
for p in obeso:
    print (f'{p[0]}, com peso de {p[1]}')

print (f'Os mais leves são {leves}')