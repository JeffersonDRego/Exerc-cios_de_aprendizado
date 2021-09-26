from random import randint
dado=randint(1,6)

jogadores={'JOGADOR1': randint(1,6),
            'JOGADOR2':randint(1,6),
            'JOGADOR3':randint(1,6),
            'JOGADOR4':randint(1,6)}
for v in jogadores.keys():
    if jogadores[v]>1:
        print(f'')

print (jogadores)