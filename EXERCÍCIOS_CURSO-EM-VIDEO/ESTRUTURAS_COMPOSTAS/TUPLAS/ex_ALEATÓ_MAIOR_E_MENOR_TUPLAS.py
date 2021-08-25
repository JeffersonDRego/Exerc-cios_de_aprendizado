from random import randint
n=(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10))

print('OS VALORES SORTEADOS FORAM:\n')
for c in n:
    print(c,end=' ')
    
print('\n')
print(f'O MAIOR FOI {max(n)}')
print(f'OMENOR FOI {min(n)}')