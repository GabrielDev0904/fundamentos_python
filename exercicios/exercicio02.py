anoNascimento = int(input("Ano de Nascimento: "))
anoAtual = int(input("Ano de Atual: "))

idade = anoAtual - anoNascimento
semanas = idade * 52

print(f"você tem {idade} anos")
print(f"você tem {semanas} semanas")