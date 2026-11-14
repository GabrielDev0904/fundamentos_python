nome = input("Seu nome: ")
cargo = input("Seu cargo: ")
salario = float(input("Seu salário: "))
salario_ac = salario * 1.10

if salario <= 1000 :
    salario_ac
    print(f"ola {nome}, como {cargo} você recebe ajustado {salario_ac}")
else :
    print(f"ola {nome}, como {cargo} você recebe ajustado {salario}")