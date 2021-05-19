def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿cuantos pesos "+ tipo_pesos +" tiene?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💰
1 - Pesos colombianos
2 - Pesos mexicanos
3 - Pesos argentinos

Elige una opción: """
opcion = input(menu)

if opcion == "1":
    conversor("colombianos", 3678)

elif opcion == "2":
    conversor("argentinos",19.78)

elif opcion == "3":
    conversor("mexicanos",94.04)

else:
    print("ingresa una opción coreecta")
