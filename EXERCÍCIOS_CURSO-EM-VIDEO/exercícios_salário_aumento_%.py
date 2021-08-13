nome=str(input('Digite o nome do trabaiadô.\n'))
salario=float(input('Digite o valor do salário.\n'))
aumento=float(input('Aumento concedido\n'))
porcentagem=aumento/100
novo_salario=salario+(salario*porcentagem)

print (f'{nome} recebeu um aumento de {salario*porcentagem}% resultanddo no total de R${round(novo_salario,2)}.')


