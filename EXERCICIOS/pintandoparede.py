larg = float(input('Digite a Largura da Parede'))
alt = float(input('Digite a Altura da Parede'))

area = larg*alt

quant_tinta = area / 2

print(f'Sua parede tem a Dimensão {larg} x {alt} e sua Área é {area}, então serão nescessário {quant_tinta} L de tinta')