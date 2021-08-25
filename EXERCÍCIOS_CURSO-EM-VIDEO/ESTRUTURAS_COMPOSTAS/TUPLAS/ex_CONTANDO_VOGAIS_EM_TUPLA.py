palavras=('aprendendo','programar','futuro','desenvolvedor','python','xyz')

for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print (letra, end=' ')
   

   