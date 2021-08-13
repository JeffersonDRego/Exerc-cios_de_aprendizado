ano=int(input('Digite o ano para verificar se é bissexto\n'))

if ano%4==0:
    print (f'{ano} é um ano bissexto')
else:
    print (f'{ano} não é um ano bissexto')
