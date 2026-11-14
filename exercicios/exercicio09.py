nome = input("Seu nome: ")
cargo = input("Seu cargo: ")
salario = float(input("Seu salário: "))
salario_ac = salario * 1.30

if salario <= 500 :
    salario_ac
    print(f"ola {nome}, como {cargo} você recebe ajustado {salario_ac}")
else :
    print(f"ola {nome}, ganhando {salario} você não pode receber ajuste")