
def mostrar_mensaje_despedida():
    print("\n👋 Gracias por trabajar con nosotros\n")
    print("Ahi te ves")


while True:

    print("== MENU ==")
    print("1. Ingresar datos empleade")
    print("2. Calcular bono")
    print("3. Mostrar Resumen")
    print("4. Salir")

    opcion = (input("Ingrese opcion: "))

    if opcion == 1:
        ingresar_datos()
    elif opcion == 2:
        calcular_bono()
    elif opcion == 3:
        mostrar_resumen()
    elif opcion == 4:
        mostrar_mensaje_despedida()
    else:
        print("Ingrese una opcion valida")
