#Levando em consideração que o pintor 
# saiba quantos m² sua tinta rende por Litro

largura_parede=float(input('Digite a largura da parede:\n'))
altura_parede=float(input('Digite a altura da parede\n'))

area_parede=largura_parede*altura_parede

print (f'A área total da parede é {area_parede}')

rendimento_tinta=float(input('Quantos m² sua tinta rende?\n'))

l=area_parede/rendimento_tinta

print (f'Você precisa de {l} litros de tinta para pintar sua parede')

