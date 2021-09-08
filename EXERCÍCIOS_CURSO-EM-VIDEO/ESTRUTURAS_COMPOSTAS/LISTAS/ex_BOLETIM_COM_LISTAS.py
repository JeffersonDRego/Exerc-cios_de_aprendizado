alunos=[]
dados=[]
media_nota=[]
while True:
    dados.append(str(input('NOME: ')))
    dados.append(float(input('NOTA 1: ')))
    dados.append(float(input('NOTA 2: ')))
    alunos.append(dados[:])
    dados.clear()
    resp=str(input('***QUER CONTINUAR?'))
    if resp in 'Nn':
        break
print (alunos)
print()
for i, a in enumerate(alunos):
    media=(alunos[i][1]+alunos[i][2])/2
    print(f'{i+1}|{alunos[i][0]:^10}|{media:^5}|')

for i in alunos:
    resp=str(input('DESEJA VER ALGUM ALUNO DA LISTA? [S/N]'))
    if resp in 'Nn':
        break
    qual=int(input('QUAL O NÚMERO DO ALUNO NA LISTA?'))
    
    print(f'{qual}|{alunos[qual-1][0]:^10}|{media:^5}|')
