sexo=str(input('Digite M para MASC. ou F PARA FEM.\n')) .upper()


while sexo not in 'MF':
    print('Você digitou um valor inválido')
    sexo=str(input('Digite M para MASC. ou F PARA FEM.\n')) .upper()
    if sexo=='M':
        print('O sexo escolhido foi Masculino')
    if sexo=='F':
        print('O sexo escolhido foi Feminino')
    sexo= sexo

print(sexo)


