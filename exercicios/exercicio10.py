preco_compra = float(input("Digite o preço de compra: R$ "))
percentual = float(input("Digite o percentual de lucro (em %): "))

preco_venda = preco_compra * (1 + (percentual / 100))
print(f"Preço de venda do produto: R$ {preco_venda:.2f}")

if percentual < 50:
    print("Atenção: O produto será vendido com uma margem muito pequena de lucro.")