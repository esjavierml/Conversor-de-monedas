menu = """
Bienvenido al conversor de monedas 💰
1 - Pesos colombianos
2 - Pesos mexicanos
3 - Pesos argentinos

Elige una opción: """
opcion = input(menu)

if opcion == "1":
    pesos = input("¿cuantos pesos colombianos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 3674 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

elif opcion == "2":
    pesos = input("¿cuantos pesos mexicanos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 19.78 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

elif opcion == "3":
    pesos = input("¿cuantos pesos argentinos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 94.04
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

else:
    print("ingresa una opción coreecta")
