lista=('Pão', 1.00, 'Leite', 2.50, 'Manteiga', 5.00)
print ('=='*20)
print('{:^40}'.format('TABELA DE PREÇOS'))
print ('=='*20)
for pos in range(0,len(lista)):
    if pos %2==0:
        print (f'{lista[pos]:.<32}', end='')
    else:
        print (f'R${lista[pos]: >6.2f}') 
print('=='*20)