'''numeros=(1,2,3,4,5,6,7,8,9,10)
while True:
        try:
            escolha=int(input('Digite um número de 1 a 10'))
            if escolha in numeros:
                break
            else:
                pass
        except ValueError:
            print('\n***ERRO***Digite um número de 1 a 10\n')

for pos, c in enumerate(numeros):
    print (numeros[2])
    '''

numeros=(1,2,3,4,5,6,7,8,9,10)
numeros_ext=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')




while True:
    while True:
        try:
            n=int(input('\033[1;32mDigite um número de 0 a 10.\n\033[m'))
            break
        except ValueError:
            print ('***DIGITE APENAS UM NÚMERO DE 1 A 10***')
    if 0<=n<=10:
        print(f'Você digitou {n} que se escreve {numeros_ext[n]}')
        continuar=str(input('Quer continuar? [S/N]\n')) .upper() .strip()
        if continuar in 'Nn':
            break

