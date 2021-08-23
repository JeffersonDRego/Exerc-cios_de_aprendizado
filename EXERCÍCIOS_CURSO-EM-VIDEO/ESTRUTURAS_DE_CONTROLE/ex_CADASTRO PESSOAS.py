###CORRIGIR
maiores=0

homens=0
mulheres=0
menores=0
total=0

while True:
    print('*'*30)
    print('CADASTRE UMA PESSOA:')
    print('*'*30)
    nome=str(input('NOME\n'))
    idade=int(input('IDADE\n'))
    sexo=str(input('SEXO [M/F]')) .strip() .upper()
    
    if idade<18:
        menores+=1
        total+=1
    if idade >=18:
        maiores+=1
        total+=1
    if sexo in 'Mm':
        homens+=1
    if sexo in 'Ff':
        mulheres+=1
    continuar=str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    if continuar in 'Ss':
        pass
    if continuar in 'Nn':
        break

print(f'VOCE CADASTROU {total} PESSOAS\nO MAIS VELHO TEM {mais_velho} ANOS\nO MAIS NOVO TEM {mais_novo} ANOS\nSÃO {homens} HOMENS E {mulheres} MULHERES')