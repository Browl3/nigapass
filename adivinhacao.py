import random as r

numero_secreto = 7
chute = int(input('Escolha um número de 1 a 10: '))
print(f'Você escolheu o número {chute}.')

if chute == numero_secreto:
    print('Você acertou!')
elif chute > numero_secreto:
    print(f'Você errou!\nTente um número menor.')
else:
    print(f'Você errou!\nTente um número maior.')