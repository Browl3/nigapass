import random

while True:
    numero_secreto = random.randint(1, 20)
    tentativas = 0

    print("\nTente adivinhar um número entre 1 e 20!")

    while True:
        entrada = input("Digite seu palpite (ou 'pare' para sair): ")

        if entrada.lower() == "pare":
            print("Jogo encerrado!")
            break

        try:
            chute = int(entrada)
        except ValueError:
            print("Por favor, digite um número inteiro.")
            continue

        tentativas += 1

        if chute < numero_secreto:
            print("Errou! Tente um número maior.")
        elif chute > numero_secreto:
            print("Errou! Tente um número menor.")
        else:
            print(f"Acertou em {tentativas} tentativa(s)!")
            break

    if entrada.lower() == "pare":
        break

    jogar_novamente = input("Quer jogar novamente? (sim/não): ")

    if jogar_novamente.lower() == "não" or jogar_novamente.lower() == "nao" or jogar_novamente.lower() == "n" or jogar_novamente.lower() == "N":
        print("Obrigado por jogar!")
        break