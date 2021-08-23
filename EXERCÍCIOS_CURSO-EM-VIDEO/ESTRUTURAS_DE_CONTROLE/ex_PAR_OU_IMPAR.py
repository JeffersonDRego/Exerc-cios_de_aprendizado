
import random
print('=-'*50)
print('\033[1;33mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('-='*50)

numeros=[1,2,3,4,5,6,7,8,9,10]
c=0

n=0
while True:    
    pc=random.choice(numeros)
    while True:
        try:
            n=int(input('\033[1;32mDIGITE UM VALOR.\033[m\n'))
            break
        except ValueError:
            print ('***DIGITE APENAS NÚMEROS***')
                        
    p_ou_i=str(input('\033[1;32mPAR OU ÍMPAR? [P/I]\033[m\n')) .upper().strip()
    while p_ou_i not in 'PpIi':
        p_ou_i=str(input('\033[1;32mPAR OU ÍMPAR? [P/I]\033[m\n')) .upper().strip()
    resultado=n+pc

    if resultado %2==0 and p_ou_i=='P':
        c+=1
        print ('Parabéns você ganhou 1 ponto.')
        print(f'O COMPUTADOR ESCOLHEU {pc},\nA SOMA DE {pc} e {n} É IGUAL A {resultado}')
        print('---'*10)
    elif resultado %2!=0 and p_ou_i=='I':
        c+=1
        print ('Parabéns você ganhou 1 ponto.')
        print(f'O COMPUTADOR ESCOLHEU {pc},\nA SOMA DE {pc} e {n} É IGUAL A {resultado}')
        print('---'*10)
    elif resultado %2==0 and p_ou_i=='I':
        print('Você perdeu\n.')
        print(f'O COMPUTADOR ESCOLHEU {pc},\nA SOMA DE {pc} e {n} É IGUAL A {resultado}')
        print(f'Sua pontuação foi {c} ')
        if c >=3:
            print('Parabéns venceu  a máquina 3 vezes ou mais!!!'.upper())
        break
        
    elif resultado %2==1 and p_ou_i=='P':
        print('Você perdeu.\n')
        print(f'O COMPUTADOR ESCOLHEU {pc},\nA SOMA DE {pc} e {n} É IGUAL A {resultado}')
        print(f'Sua pontuação foi {c} ')
        if c >3:
            print('Parabéns venceu  a máquina 3 vezes ou mais!!!'.upper())
            
        break
