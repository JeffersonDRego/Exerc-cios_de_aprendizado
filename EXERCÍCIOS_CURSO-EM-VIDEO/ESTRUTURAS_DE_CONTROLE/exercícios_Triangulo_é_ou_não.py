r1=float(input('Primeiro segmento'))
r2=float(input('Segundo segmento'))
r3=float(input('Terceiro segmento'))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print ('Valores válidos para formar um triângulo.')
   
    if r1==r2==r3:
        print('Seu triângulo é EQUILÁTERO.')
    elif r1!=r2!=r3!=r1:
        print('Seu triângulo é ESCALENO.')
    else:
        print('Seu triângulo é ISÓSCELES.')

else:
    print ('Não dá pra fazer triângulo nããão')
