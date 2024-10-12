dias=int(input('Quantos dias Você Alugou o Carro?'))
km=float(input('Quantos KM Você Rodou Com o Carro?'))

total=(dias*60) + (km*0.15)

print(f'O Dinheiro do Aluguel Foi:R${total:.2f}')