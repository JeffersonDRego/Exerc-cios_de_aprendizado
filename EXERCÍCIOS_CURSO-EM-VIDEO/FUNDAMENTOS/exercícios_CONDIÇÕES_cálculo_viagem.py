km=float(input('Qual a distância a ser percorrida (em KM)\n'))

if km<=200:
    custo_viagem=km*0.50
    print(f'Você vai gastar R$ {custo_viagem}')
else:
    custo_viagem=km*0.45
    print (f'Você vai gastar R${custo_viagem}')
130.8