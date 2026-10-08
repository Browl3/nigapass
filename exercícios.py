nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print(f'Daqui a 10 anos você terá {idade + 10} anos.')

print('=' * 20, '\n\n' * 5)

c = float(input('Digite a temperatura em °C: '))
f = c * 9 / 5 + 32
print(f'{c} Celsius fica {f} Fahrenheit.')

print('=' * 20, '\n\n' * 5)

base = int(input('Digite a base do retângulo em metros: '))
altura = int(input('Digite a altura do retângulo em metros: '))
area = base * altura
perimetro = base + base + altura + altura
print(f'A área do retângulo mede {area} e {perimetro} de perímetro.')

print('=' * 20, '\n\n' * 5)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print(f'Sua média é {media:.2f}.')

print('=' * 20, '\n\n' * 5)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2

if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal.')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso.')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade grau I')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')