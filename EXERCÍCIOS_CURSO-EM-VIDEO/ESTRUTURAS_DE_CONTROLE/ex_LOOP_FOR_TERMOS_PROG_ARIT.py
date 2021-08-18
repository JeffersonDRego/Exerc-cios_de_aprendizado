#USANDO O LOOP FOR PARA PROGRESSÃO ARITMÉTICA
'''primeiro=int(input('Digite o termo'))
razao=int(input('Digite a razão.'))
decimo=primeiro+(10-1)*razao

for c in range(primeiro,decimo+razao,razao):
    print(c)
'''
### USANDO WHILE PARA PROGRESSÃO ARITMÉTICA

primeiro=int(input('Digite um termo.'))
razao=int(input('Digite a razão'))
termo=primeiro
cont=1

while cont <=10:
    print(f'{termo} →',end=' ')
    termo+=razao
    cont+=1 
print('FIM')