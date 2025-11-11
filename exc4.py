viagem = 300
alojamento = 500
alimentacao = 200
museus = 150

print("----- Menu -----")
print("1 - Viagem a Paris")
print("2 - Viagem a Paris / Alojamento")
print("3 - Viagem a Paris / Alojamento / Alimentação")
print("4 - Viagem a Paris / Alojamento / Museus")

opcao = int(input("Escolha uma opção (1-4): "))

if opcao == 1:
    total = viagem
elif opcao == 2:
    total = viagem + alojamento
elif opcao == 3:
    total = viagem + alojamento + alimentacao
elif opcao == 4:
    total = viagem + alojamento + museus
else:
    total = 0
    print("Opção inválida!")

if total > 0:
    print("Valor a pagar:", total, "euros")

