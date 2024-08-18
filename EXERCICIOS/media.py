print('|------ Calculadora de Media Anual ------|')

num1 =float(input('Digite a Primeira Nota'))
num2 =float(input('Digite a Segunda  Nota'))
num3 =float(input('Digite a Terceira Nota'))
num4=float(input('Digite a Quarta  Nota'))

Media = (num1+num2+num3+num4)/4

if Media >= 6:
    print(f'A Media Final do Aluno é:{Media:.1f} O Aluno Está Aprovado')#um numero apos a Virgula 
else:
    print(f'A Media Final do Aluno é: {Media:.1f}, O Aluno Está Reprovado')

print('---------------------------------')

