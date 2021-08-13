print('-'*40)
x=int(input('Digite um numero para saber a tabuada:\n'))

print('*'*20)
print(f'TABUADA DE {x}')
print('*'*20)

a=0

while a<=10:
    print (f'{x} X {a} = {x*a}')
    a=a+1
