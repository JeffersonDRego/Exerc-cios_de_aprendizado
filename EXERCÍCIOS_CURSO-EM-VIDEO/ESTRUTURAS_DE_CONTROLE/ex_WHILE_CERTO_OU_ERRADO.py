import random
numeros=[1,2,3,4,5,6,7,8,9,10]
num_certo=random.choice(numeros)

tentativas=0

x=int(input('Adivinhe qual número de 1 a 10 o computador escolheu.\n'))

while x != num_certo:
    print('ERROU')
    x=int(input('TENTE NOVAMENTE:\n'))
    tentativas+=1
    if x==num_certo:
        print (f'Parabéns você acertou depois de {tentativas} tentativas.')
        