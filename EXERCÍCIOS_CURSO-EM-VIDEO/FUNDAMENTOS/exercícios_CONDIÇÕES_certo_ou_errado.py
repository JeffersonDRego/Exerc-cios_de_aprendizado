import random
numeros=[1,2,3,4,5]
num_certo=random.choice(numeros)

x=int(input('Adivinhe qual número de 1 a 5 o computador escolheu.\n'))

if x==num_certo:
    print ('Parabéns, você acertou!')
else:
    print('Não foi dessa vez')
print (f'O número escolhido foi {num_certo}')

