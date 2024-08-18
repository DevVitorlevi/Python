num = float(input('Digite a Medida em Metros:'))
dm = num*10
cm = num*100
mm = num*1000
km = num / 1000
hec = num / 100
dam = num / 10


print(f'em Kilometros: {km:.0f}KM')
print('---------------------')
print(f'em Hectometro: {hec:.0f}HEC')
print('---------------------')
print(f'em Decametro: {dam:.0f}DAM')
print('---------------------')
print(f'em Metros: {num:.0f}M')
print('---------------------')
print(f'em Decimetro: {dm:.0f}DM')
print('---------------------')
print(f'em Centimetros: {cm:.0f}CM')
print('---------------------')
print(f'em Milimetros: {mm:.0f} MM')

