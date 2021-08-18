###FATORANDO USANDO WHILE
num=int(input('Digite um valor para saber o fatorial.'))
c=num
f=1
while c>0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f*=c
    c-=1
print(f,end=' ''\n\n\n')

###FATORANDO COM LOOP FOR

num2=int(input('Digite um valor novamente para fatorá-lo.'))

a=num2
fac=1
for i in range(1,a+1):
    print(i,end=' ')
    fac*=i
    print ('x' if a>1 else '=',end=' ')
    a-=1
print(fac)