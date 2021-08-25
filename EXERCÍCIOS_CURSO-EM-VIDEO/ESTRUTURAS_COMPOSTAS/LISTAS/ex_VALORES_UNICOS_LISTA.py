valores=[]

while True:
    v=(int(input('Digite um valor inteiro')))
    
    
    if v not in valores:
        valores.append(v)
        print ('**valor adicionado com sucesso...')
    else:
        print ('VALOR DUPLICADO, VAI DAR NÃO')
        
    resp= (str(input('QUER CONTINUAR? [S/N]')))
    if resp in 'Nn':
        break 
#valores.sort()
print(f'VOCÊ DIGITOU OS VALORES {sorted(valores)}')