n=int(input('Quantos termos deseja mostrar\n'))
t1=0
t2=1
print(f'{t1}→{t2}',end=' ')
cont=3
while cont<=n:
    t3=t2+t1
    print(f'→{t3}',end=' ')
    t1=t2
    t2=t3
    t3=t2+t1
    cont+=1
print('\nFIM')