# 1. Receba a idade em anos e imprima em meses, dias, horas e minutos.

# numeros, textos e booleanos
# Entrada
idade = int(input("Digite a idade: "))

# processamento
idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60

# saída
print(f"Sua idade em meses é: {idadeEmMeses}")
print(f"Sua idade em Dias é: {idadeEmDias}")
print(f"Sua idade em Horas é: {idadeEmHoras}")
print(f"Sua idade em minutos é: {idadeEmMinutos}")