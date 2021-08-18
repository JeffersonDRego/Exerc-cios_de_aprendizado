
num1=float(input('Digite um valor\n'))
num2=float(input('Digite um valor\n'))

escolha=0
while escolha!=5:
    print ('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\n')
    escolha=int(input('DIGITE UMA OPÇÃO.\n'))
    if escolha==1:
        soma=num1+num2
        print(f'A soma dos valores é igual a {soma}\n')
    elif escolha == 2:
        mult=num1*num2
        print(f'A multiplicação dos valores é igual a {mult}\n')
    elif escolha == 3:
        if num1>num2:
            print (f'{num1} é o maior.\n')
        elif num1==num2:
            print('Os valore são iguais.\n')
        else:
            print (f'{num2} é o maior.\n')
    elif escolha == 4:
        num1=float(input('Digite um valor\n'))
        num2=float(input('Digite um valor\n'))
    elif escolha==5:
        print('OBRIGADO E ATÉ LOGO.')
        exit()
    else:
        print('TENTE NOVAMENTE')
