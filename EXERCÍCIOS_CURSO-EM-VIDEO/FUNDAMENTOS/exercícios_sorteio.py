from random import choice #importando função específica de um módulo

a1=input('Digite o nome do aluno 1\n')
a2=input('Digite o nome do aluno 2\n')
a3=input('Digite o nome do aluno 3\n')
a4=input('Digite o nome do aluno 4\n')

lista=[a1,a2,a3,a4]

print (f'O aluno escolhido foi {choice(lista)}') #utilizando a função do módulo

