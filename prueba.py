print("Hola mundo")

print("Calculadora")

while True:
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Digite su opción: "))

    if opcion == 5:
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    elif opcion in [1, 2, 3, 4]:
        num1 = float(input("Digite el primer número: "))
        num2 = float(input("Digite el segundo número: "))

        if opcion == 1:
            resultado = num1 + num2
            print("El resultado de la suma es: ", resultado)
        elif opcion == 2:
            resultado = num1 - num2
            print("El resultado de la resta es: ", resultado)
        elif opcion == 3:
            resultado = num1 * num2
            print("El resultado de la multiplicación es: ", resultado)
        elif opcion == 4:
            if num2 != 0:
                resultado = num1 / num2
                print("El resultado de la división es: ", resultado)
            else:
                print("Error: No se puede dividir por cero.")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

