horas = int(input("Horas estacionadas: "))

tarifa = 0

if horas < 0:
    print("Horas negativas não são permitidas.")
elif horas <= 2:
    tarifa = 8
elif horas <= 5:
    tarifa = 8 + 3 * (horas - 2)
else:
    tarifa = 20 + 2 * (horas - 5)

print(f"Tarifa: {tarifa:.2f}")