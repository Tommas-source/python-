ano_atual = int(input("digite o ano atual : "))
ano_nasc = int(input("digite o ano de nascimento : "))

idade = ano_atual - ano_nasc
print("o ano atual é {} e o ano de nascimento é {} a sua idade é {} anos". format(ano_atual,ano_nasc,idade))

if idade >= 18 : 
    print("estas apto a conduzir.")
else:
    print("atencao!!! nao estas apto para conduzir.")
    