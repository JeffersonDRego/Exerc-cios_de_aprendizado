preco_produto=float(input('Digite o preço do produto\n'))
desconto=float(input('Digite o valo do desconto\n'))
porcentagem=desconto/100
valor_final=preco_produto-(preco_produto*porcentagem)

print ('-'*40)
print (f'** O preço do produto é {preco_produto} **')
print (f'** Você ganhou o desconto de {desconto}% **')
print (f'** O valor do desconto é de R${preco_produto*porcentagem} **')
print (f'** O preço final é de R${valor_final} **')
