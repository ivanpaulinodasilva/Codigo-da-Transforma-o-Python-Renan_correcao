def calcular_media():
    notas = []
    qtd = int(input("Quantas notas deseja informar? "))
    for i in range(qtd):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média: {media:.2f} - Aprovado")
    else:
        print(f"Média: {media:.2f} - Reprovado")

calcular_media()
