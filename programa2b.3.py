import random

while True:
    numero_secreto = random.randint(1, 20)
    tentativas = 0
    acertou = False
    sair = False

    print("\nTente adivinhar um número entre 1 e 20!")

    while tentativas < 10 and not acertou:
        entrada = input("Digite seu palpite (ou 'pare' para sair): ")

        if entrada.lower() == "pare":
            print("Jogo encerrado!")
            sair = True
            break

        try:
            chute = int(entrada)
        except ValueError:
            print("Por favor, digite um número inteiro.")
            continue

        tentativas += 1
        print("Tentativas restantes:", 10 - tentativas)

        if chute < numero_secreto:
            print("Errou! Tente um número maior.")
        elif chute > numero_secreto:
            print("Errou! Tente um número menor.")
        else:
            print(f"Acertou em {tentativas} tentativa(s)!")
            acertou = True

    if sair:
        break

    if not acertou:
        print(f"\nVocê não acertou! O número era {numero_secreto}.")

    jogar_novamente = input("Quer jogar novamente? (sim/não): ")

    if jogar_novamente.lower() in ["não", "nao", "n"]:
        print("Obrigado por jogar!")
        break