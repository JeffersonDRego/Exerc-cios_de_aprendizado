alunos=list()
aluno=dict()

aluno['NOME']=str(input('DIGITE O NOME: '))
aluno['MEDIA']=float(input('DIGITE A MÉDIA: '))
alunos.append(aluno)
for k, v in alunos:
    if alunos[0]['MEDIA']<7:
        print(f'O NOME É {aluno["NOME"]}')
        print(f'A MÉDIA É {aluno["MEDIA"]}')
        print ('ALUNO REPROVADO')
    else:
        print(f'O NOME É {aluno["NOME"]}')
        print(f'A MÉDIA É {aluno["MEDIA"]}')
        print('ALUNO APROVADO') 