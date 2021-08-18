from time import sleep
import timer
valor_casa=float(200000.00)
parcela_min=800.00
salario=float(input('Digite seu salário\n'))

anos=int(input('Por quantos anos deseja pagar?\n'))
anos=anos*12
sal_per=salario*(30/100)

if sal_per*anos<valor_casa:
    print ('\033[1;31mVocê não pode comprar essa casa.\033[m')
else:
    print('\033[1;32mANALISANDO RESULTADOS\033[m')
sleep(2)

print('\033[1;32mVOCÊ FOI APROVADO...CALCULANDO VALORES\033[m')
sleep(2)

parcela=round(valor_casa/anos)

print (f'O VALOR DE CADA PARCELA SERÁ \033[1;32mR${parcela}\033[m')
