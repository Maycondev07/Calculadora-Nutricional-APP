def imc():
    print ("Para calcularmos seu IMC precisamos da sua altura e peso.")
    height = int(input("Sua altura é?"))
    weight = int(input("Seu peso é?"))
    ask = str(input(f"Sua altura: {height}, seu peso: {weight}, estão corretos? s/n"))
    if ask != "n":
        result = str((weight / (height * height)) *10000)
        i = result[:4]
        result = float((weight / (height * height)) *10000)
        print (f"seu imc é {i}")
        if result <= 18.5:
            print ("Abaixo do peso")
        elif result <= 24.9:
            print ("Peso ideal")
        elif result <= 29.9:
            print ("Sobrepeso")
        elif result <= 34.9:
            print ("Obesidade 1°Grau")
        elif result <= 39.9:
            print ("Obesidade 2°Grau")
        else:
            print ("Obesidade 3°Grau")
    else:
        print ("informe novamente")
        imc()

def tmb():
    print ("Para calcularmos seu TMB precisamos saber seu sexo, idade, altura e peso.")
    height = int(input("Sua altura é?"))
    weight = int(input("Seu peso é?"))
    sex = str(input("você é homem ou mulher? male/female"))
    age = int(input("quantos anos tem?"))
    ask = str(input(f"Altura: {height}, Peso: {weight}, Sexo: {sex}, Idade: {age}, estão corretos? s/n"))
    if ask != "n":
        if sex.lower() == "male":
            result = (6.25*height)+(10*weight)-(5*age)+5
            print (f"Sua tmb é {result} kcal/dia")
        else:
            result = (6.25*height)+(10*weight)-(5*age)-161
            print (f"Sua tmb é {result} kcal/dia")
    else:
        print ("informe novamente")
        tmb()


def get():
    print ("Para calcularmos seu GET, vamos primeiro precisamos calcular sua TMB, precisamos saber seu sexo, idade, altura e peso.")
    height = int(input("Sua altura é?"))
    weight = int(input("Seu peso é?"))
    sex = str(input("você é homem ou mulher? male/female"))
    age = int(input("quantos anos tem?"))
    fa = int(input("Qual o nivel de atividade que pratica diariamente? 1 - leve / 2 - moderada / 3 - alta"))
    ask = str(input(f"Altura: {height}, Peso: {weight}, Sexo: {sex}, Idade: {age}, Nivel do fator de atividade:{fa}, estão corretos? s/n"))
    if ask != "n":
        if sex.lower() == "male":
            result = ((6.25*height)+(10*weight)-(5*age)+5)
        else:
            result = (6.25*height)+(10*weight)-(5*age)-161
        if fa == 1:
            result *= 1.3
            print (f"Seu GET é {result} kcal/dia")
        elif fa == 2:
            result *= 1.5
            print (f"Seu GET é {result} kcal/dia")
        elif fa == 3:
            result *= 1.7
            print (f"Seu GET é {result} kcal/dia")
        
    else:
        print ("informe novamente")
        get()

def home():
    print ("Bem-vindo a calculadora nutricional em python")
    print ("qual das funções gostaria de usar?")
    choice = int(input("1 - IMC / 2 - TMB / 3 - GET "))
    if choice == 1:
        imc()
    if choice == 2:
        tmb()
    if choice == 3:
        get()
    if choice == 4:
        cdp()
    else:
        print("opção invalida")
        home()
def start ():
    home()
start()