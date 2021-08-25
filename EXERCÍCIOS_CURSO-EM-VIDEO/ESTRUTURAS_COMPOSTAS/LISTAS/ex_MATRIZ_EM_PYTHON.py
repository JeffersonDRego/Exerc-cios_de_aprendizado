'''valores=[[],[],[],[],[],[],[],[],[]]
x=0
for c in range(1,10):
    valores[x].append(int(input('Digite um valor inteiro:')))
    x+=1

print(valores[0],valores[1],valores[2])
print(valores[3],valores[4],valores[5])
print(valores[6],valores[7],valores[8])'''

matriz=[[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para a posição {l,c}'))

for l in range(0,3):
    for c in range(0,3):
        print(f'|{matriz[l][c]:^3}|',end='')
    print()
