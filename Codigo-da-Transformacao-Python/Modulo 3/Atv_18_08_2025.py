def maior_menor():
    numeros = []
    qtd = int(input("Quantos números deseja informar? "))
    for i in range(qtd):
        num = int(input(f"Digite o número {i+1}: "))
        numeros.append(num)

    print("Maior:", max(numeros))
    print("Menor:", min(numeros))

maior_menor()
