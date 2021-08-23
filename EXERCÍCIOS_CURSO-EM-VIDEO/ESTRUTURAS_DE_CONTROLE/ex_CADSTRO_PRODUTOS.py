total= totmil= menor= cont= 0
barato=''
while True:
    produto=str(input('Nome do produto\n'))
    preco=float(input('Preço: R$ '))
    cont+=1
    total+=preco

    if preco>1000:
        totmil+=1
    if cont==1:
        menor=preco
        barato=produto
    if preco<menor:
        menor=preco
        barato=produto
    resp=' '
    while resp not in 'SN':
        resp=str(input('QUER CONTINUAR? [S/N]')).upper().strip()
    if resp=='N':
        break
print(f'FIM DO PROGRAMA')
print(f'O TOTAL DA COMPRA FOI R${round(total,2)}')    
print(f'TEMOS {totmil} PRODUTOS CUSTANDO MAIS DE R$1.000,00')
print (f'O PRODUTO MAIS BARATO FOI {barato} E CUSTA R$ {round(menor,2)}')        
    

