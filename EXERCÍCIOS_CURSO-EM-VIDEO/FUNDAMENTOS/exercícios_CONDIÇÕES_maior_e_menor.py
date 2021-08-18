num=int(input('Digite um numero de três digitos.\n'))
u=(num//1)%10
d=(num//10)%10
c=(num//100)%10

menor=u

if d<u and d<c:
    menor=d
if c<u and c<d:
    menor=c

maior=u

if d>u and d>c:
    maior=d
if c>u and c>d:
    maior=c

print(f'{menor} é o menor.')
print(f'{maior} é o maior.')
