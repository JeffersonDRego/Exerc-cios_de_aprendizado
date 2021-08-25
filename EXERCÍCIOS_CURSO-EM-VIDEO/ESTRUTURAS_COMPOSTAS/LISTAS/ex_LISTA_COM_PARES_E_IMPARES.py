numeros=[[],[]]

for c in range(0,7):
    n=(int(input('Digite um valor inteiro: ')))
    if n%2==0:
        numeros[0].append(n)
        
    else:
        numeros[1].append(n)

print (f' os ímpares são {numeros[1]}')

print (f' os pares são {numeros[0]}')

print (sorted(numeros))