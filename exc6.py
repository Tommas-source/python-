numero = int(input("Digite um número: "))

if numero == 1:
    print("O número digitado foi 1")
elif numero == 2:
    print("Eu sei qual o número digitado, o dígito foi 2")
elif numero == 3 or numero == 4:
    print("O número digitado foi 3 ou 4")
elif numero >= 5 and numero <= 10:
    print("O número digitado está entre 5 e 10")
else:
    print("O dígito não está entre 1 e 10")


