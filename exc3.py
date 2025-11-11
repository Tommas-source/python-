# Programa: Número por Extenso (usando match/case)

numero = int(input("Digite um número de 1 a 5: "))

match numero:
    case 1:
        print("Um")
    case 2:
        print("Dois")
    case 3:
        print("Três")
    case 4:
        print("Quatro")
    case 5:
        print("Cinco")
    case _:
        print("Número inválido!")

