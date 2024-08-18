n = input('Digite algo:')
print(f'é do Tipo?{type(n)}')#tipo
print(f' Só contem Espaços?{n.isspace()}')#totalmente space
print(f'é um Numero?{n.isnumeric()}')#verifica se é numero
print(f'é alfabetico?{n.isalpha()}')#verifica se tem letras 
print(f'é alfanumérico?{n.isalnum()}')#Verifica se é alfanumerico
print(f'esta em maiusculo?{n.isupper()}')#Verifica se esta totalmente em maiusculo
print(f'esta em minusculo?{n.islower()}')#Verifica se esta totalmente em Minusculo
print(f'é alfabetico?{n.istitle()}')#Verifica se esta em Capitalize
