#Programa que calcula o IMC
print("Programa para calcular IMC".center(60))
print()
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print()
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)
print()
peso = 80
altura = 1.85
print("Nome do paciente:",nome)
print("Idade do paciente:",idade)
print("Peso do paciente:",peso)
print("Altura do paciente:",altura)
print(f"O seu peso é {peso}kg e sua altura é {altura}cm.")
print(f"IMC:{imc:.2f}")


if imc <=18.5:
    print("Cuidado. voce esta abaixo do peso")
elif 18.5 <= 24.9:
    print("peso normal.")
elif 24.9 <= 29.9:
    print("Voce esta em sobrepeso")
elif 29.9 <= 34.9:
    print("Obesidade grau I.")
elif 34.9 <= 39.9:
    print("Obesidade grau II.")
elif 39.9 <= 40.0:
    print("Obesidade grau III.")
else:
    print("Espro ter ajudado, se cuide e se alimente bem.")

