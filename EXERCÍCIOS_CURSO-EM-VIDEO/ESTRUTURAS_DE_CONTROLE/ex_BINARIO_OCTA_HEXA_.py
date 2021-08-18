num=int(input('\033[1;32mDigite um valor para converter em binario, octal ou hexadecimal.\033[m\n'))

x=int(input('\033[1;32mDIGITE 1 PARA BINÁRIO.\nDIGITE 2 PARA OCTADECIMAL.\nDIGITE 3 PARA HEXADECIMAL.\033[m\n'))

if x==1:
    print(bin(num)[2:])
elif x==2:
    print(oct(num)[2:])
elif x==3:
    print(hex(num)[2:])
else:
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
