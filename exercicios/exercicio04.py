nome = input("digite seu nome: ")
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura(ex: 1.60): "))
imc = peso / (altura*2)

print(f"ola {nome}, seu IMC é: {imc}")