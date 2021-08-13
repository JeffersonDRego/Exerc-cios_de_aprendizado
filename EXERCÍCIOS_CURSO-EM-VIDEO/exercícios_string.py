from typing import Counter


frase=str(input('Digite uma frase')) .upper().strip()
#a1=frase.count('A')
a2=frase.find('A')+1
a3=frase.rfind('A')+1
print (f'A letra A aparece {a1} vezes')
print (f'A primeira vez que ela aparece é na casa {a2}')
print (f'A última vez que ela aprece é na casa {a3}')

print (f'a letra aprece {frase.count('A')}')