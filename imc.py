    massa = float8input("digite o valor da massa(kg) :")
    altura = float("digite a sua altura (m)")

    imc = massa/altura **2
    print("o seu é imc é [:.2f]" .format(imc))


    if inc <17 : 
        print("muito abaixo do peso .")
    
    elif inc >17 and imc <= 18.5 :
    print("abaixo do peso ")
    
    elif inc >18.5 and imc >25 :
        print("peso ideial")

    elif imc >25 and imc <= 30 :
        print("sobrepeso")

    elif imc >30 and imc <= 35:
        print("obesidade")

    elif imc >35 and imc <=40 :
        print("obesidade serena")

    else
    print("obsidade morfica")
