soma=0
a=0
for c in range(1,501,1):
    if c%3==0:
        a+=1 #igual a >>>a=a+1
        soma+=c # igual a >>>soma=soma+c
print(f'A soma de todos os {a} valores é igual a {soma}')