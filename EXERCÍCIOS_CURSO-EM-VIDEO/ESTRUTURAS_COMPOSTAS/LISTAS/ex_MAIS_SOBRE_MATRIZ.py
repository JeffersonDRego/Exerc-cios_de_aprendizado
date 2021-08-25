matriz=[[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para a posição {l,c}'))
spar= maior= scol= 0
for l in range(0,3):
    for c in range(0,3):
        print(f'|{matriz[l][c]:^3}|',end='')
        if matriz[l][c] %2==0:
            spar+=matriz[l][c]
    print()

print (f'A SOMA DE TODOS OS VALORES É IGUAL A: {sum(matriz[0]+matriz[1]+matriz[2])}')
print (f'A SOMA DE TODOS OS VALORES PARES SÃO: {spar}')

for l in range(0,3):
    scol+=matriz[l][2]

print(f'A SOMA DOS VALORES DA 3ª COLUNA É IGUAL A: {scol}')

print(f'O MAIOR VALOR DA SEGUNDA COLUNA É: {maior}')
print(f'O maior valor da 2a. linha é: {max(matriz[1])}')
