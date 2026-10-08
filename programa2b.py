import random

while True:
    numero_secreto = random.randint(1, 20)
    tentativas = 0
    acertou = False

    print("\nTente adivinhar um número entre 1 e 20!")

    for tentativa in range(1, 10):
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
        restantes = 11 - tentativas

        print("Tentativas restantes:", restantes)

        if chute < numero_secreto:
            print("Errou! Tente um número maior.")

        elif chute > numero_secreto:
            print("Errou! Tente um número menor.")

        else:
            print(f"Acertou em {tentativas} tentativa(s)!")
            acertou = True
            break

    if entrada.lower() == "pare":
        break

    if not acertou:
        print(f"\nVocê não acertou! O número era {numero_secreto}.")

    jogar_novamente = input("Quer jogar novamente? (sim/não): ")

    if jogar_novamente.lower() in ["não", "nao", "n"]:
        print("Obrigado por jogar!")
        break
