# Palavra a ser adivinhada
palavra = "wellington"
palavra_array = list(palavra)

# Lista para armazenar letras descobertas
descobertas = ['_' for _ in palavra_array]

# Lista para armazenar tentativas erradas
erros = []

# Número máximo de tentativas erradas
tentativas_max = 6

print("=== Jogo da Forca ===")
print("Adivinhe a palavra:")
print(" ".join(descobertas))

# Loop do jogo
while '_' in descobertas and len(erros) < tentativas_max:
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_array:
        for i, l in enumerate(palavra_array):
            if l == letra:
                descobertas[i] = letra
        print("Boa! Letra correta.")
    else:
        if letra not in erros:
            erros.append(letra)
        print("Letra incorreta.")

    print("\nPalavra: ", " ".join(descobertas))
    print("Erros:", ", ".join(erros))
    print(f"Tentativas restantes: {tentativas_max - len(erros)}\n")

# Verifica resultado final
if '_' not in descobertas:
    print("Parabéns! Você acertou a palavra:", palavra)
else:
    print("Você perdeu! A palavra era:", palavra)
