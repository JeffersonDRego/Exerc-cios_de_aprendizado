print('*'*50)
print('PROGRAMA DE TABUADA TABAJARArinha CORPORATION')
print('*'*50)
'''while True:
    n=int(input('DIGITE UM VALOR PARA SABER A TABUADA.\n(negativo para parar).\n'))
    if n<0:
        break
    a=0
    while a<10:
        a+=1
        m=n*a
        total=m
        print(f'{n} * {a} = {total}')


print('PROGRAMA ENCERRADO VOLTE SEMPRE')'''

while True:
    n=int(input('Digite um valor.\n'))
    if n<0:
        print('acabou')
        break
    a=0
    for c in range(1,11):
        a+=1
        print(f'{n} * {a} = {n*a}')