nome=str(input('Digite seu nome\n')) .strip()
nome=nome.split()

print (f'O seu primeiro nome é {nome[0]}')
print (f'O seu(s) nome(s) do meio é(são) {nome[1:-1]}')
print (f'O seu último nome é {nome[len(nome)-1]}')

