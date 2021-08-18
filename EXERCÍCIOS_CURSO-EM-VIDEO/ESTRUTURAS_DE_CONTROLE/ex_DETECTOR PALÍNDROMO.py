frase=str(input('Digite uma frase')) .strip() .upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=''

for letra in range(len(junto)-1,-1,-1): #OU inverso=junto[::-1] NO LUGAR DO LOOP
    inverso+= junto[letra]

if inverso==junto:
    print('temos um palíndromo.')
else:
    print ('a palavra não é um palíndromo')