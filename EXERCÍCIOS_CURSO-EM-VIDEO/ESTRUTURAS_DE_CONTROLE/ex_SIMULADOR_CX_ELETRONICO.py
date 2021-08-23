print('='*30)
print('{:^30}'.format('BANCO JERSO'))
print('='*30)
print('\n')


valor=int(input('Que valor você deseja sacar?\nR$ '))
print('\n')
total=valor
cedula=50
tot_ced=0

while True:
    if total>=cedula:
        total-=cedula
        tot_ced+=1
    else:
        if tot_ced>0:
            print(f'Total de {tot_ced} cédulas de R$ {cedula}')
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        tot_ced=0
        if total==0:
            break 
        end='\n'
print('\n{:=^31}'.format('Volte sempre ao BANCO JERSO'))