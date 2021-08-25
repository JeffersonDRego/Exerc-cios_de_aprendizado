
n = int(input('DIGITE UM VALOR INTEIRO')),int(input('DIGITE UM VALOR INTEIRO')),int(input('DIGITE UM VALOR INTEIRO')),int(input('DIGITE UM VALOR INTEIRO')),int(input('DIGITE UM VALOR INTEIRO'))

print('VOCÊ DIGITOU OS VALORES:\n')
for c in n:
    print(c, end=' ')
if 9 in n:
    print(f'\n\nO valor 9 apareceu {n.count(9)} vez/vezes.')
else:
    print('O VALOR 9 NOVE NÃO FOI DIGITADO')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('OVALOR 3 NÃO FOI DIGITADO')
print('Os valores pares digitados foram:', end=' ')

for c in n:
    if c%2==0:
        print(c, end=' ')
