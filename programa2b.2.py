import random

MIN_NUM = 1
MAX_NUM = 20
MAX_TENTATIVAS = 10


def pedir_palpite():
    """Pede um palpite. Retorna 'pare', um inteiro válido ou None se for inválido."""
    entrada = input("Digite seu palpite (ou 'pare' para sair): ").strip().lower()

    if entrada == "pare":
        return "pare"

    try:
        chute = int(entrada)
    except ValueError:
        print("Por favor, digite um número inteiro.")
        return None

    if not (MIN_NUM <= chute <= MAX_NUM):
        print(f"O número deve estar entre {MIN_NUM} e {MAX_NUM}.")
        return None

    return chute


def jogar_rodada():
    """Joga uma rodada. Retorna False se o jogador pediu para sair."""
    numero_secreto = random.randint(MIN_NUM, MAX_NUM)
    tentativas = 0

    print(f"\nTente adivinhar um número entre {MIN_NUM} e {MAX_NUM}!")
    print(f"Você tem {MAX_TENTATIVAS} tentativas.")

    while tentativas < MAX_TENTATIVAS:
        chute = pedir_palpite()

        if chute == "pare":
            print("Jogo encerrado!")
            return False

        if chute is None:  # entrada inválida, não gasta tentativa
            continue

        tentativas += 1

        if chute == numero_secreto:
            print(f"Acertou em {tentativas} tentativa(s)!")
            return True

        dica = "maior" if chute < numero_secreto else "menor"
        print(f"Errou! Tente um número {dica}.")
        print("Tentativas restantes:", MAX_TENTATIVAS - tentativas)

    print(f"\nVocê não acertou! O número era {numero_secreto}.")
    return True


def quer_jogar_novamente():
    while True:
        resposta = input("Quer jogar novamente? (sim/não): ").strip().lower()
        if resposta in ("sim", "s"):
            return True
        if resposta in ("não", "nao", "n"):
            return False
        print("Responda com 'sim' ou 'não'.")


def main():
    while True:
        continuar = jogar_rodada()

        if not continuar:
            break

        if not quer_jogar_novamente():
            print("Obrigado por jogar!")
            break


if __name__ == "__main__":
    main()