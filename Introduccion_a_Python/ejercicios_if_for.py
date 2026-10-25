# =============================================================================
#  EJERCICIOS: CONDICIONALES Y BUCLES
#  TIC - 2º Bachillerato
#
#  Nombre y apellidos: ______________________________
# =============================================================================
#
#  INSTRUCCIONES
#  -------------
#  - Hay 10 ejercicios ordenados de MENOS a MÁS difícil.
#  - Cada ejercicio está dentro de su propia función (def ejercicio1(): ...).
#  - Escribe tu solución debajo del comentario "# Escribe tu código aquí"
#    y borra la línea "pass".
#  - Solo necesitas: input(), print(), int(), float(), if/elif/else, for y while.
#  - Ejecuta el archivo: aparecerá un menú para probar el ejercicio que quieras.
#  - El "Ejemplo de ejecución" muestra cómo debe verse tu programa.
#    Lo que aparece detrás de los ":" en las preguntas lo escribe el usuario.
#
#  ¡No toques la función main() del final!
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1 · ¿Mayor de edad?                                   (if - else)
# -----------------------------------------------------------------------------
# Pide al usuario su edad. Si tiene 18 años o más, muestra
# "Eres mayor de edad". Si no, muestra "Eres menor de edad".
#
# Ejemplo de ejecución:
#     ¿Cuántos años tienes? 16
#     Eres menor de edad
# -----------------------------------------------------------------------------
def ejercicio1():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 2 · Par o impar                                        (if - else)
# -----------------------------------------------------------------------------
# Pide un número entero y di si es par o impar.
# Pista: un número es par si el resto de dividirlo entre 2 es 0  (numero % 2)
#
# Ejemplo de ejecución:
#     Escribe un número: 7
#     7 es impar
# -----------------------------------------------------------------------------
def ejercicio2():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 3 · ¿Cuál es mayor?                              (if - elif - else)
# -----------------------------------------------------------------------------
# Pide dos números y muestra cuál es el mayor.
# Si los dos son iguales, muestra "Los dos números son iguales".
#
# Ejemplo de ejecución:
#     Primer número: 12
#     Segundo número: 30
#     El mayor es 30
# -----------------------------------------------------------------------------
def ejercicio3():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 4 · Calificación                                 (if - elif - else)
# -----------------------------------------------------------------------------
# Pide una nota (puede tener decimales) y muestra su calificación:
#     menos de 5       -> Insuficiente
#     de 5 a menos de 6 -> Suficiente
#     de 6 a menos de 7 -> Bien
#     de 7 a menos de 9 -> Notable
#     de 9 a 10        -> Sobresaliente
# Si la nota es menor que 0 o mayor que 10, muestra "Nota no válida".
# Pista: usa float() y los operadores "or" / "and".
#
# Ejemplo de ejecución:
#     Introduce la nota: 7.5
#     Notable
# -----------------------------------------------------------------------------
def ejercicio4():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 5 · Contar del 1 al 10                                (for + range)
# -----------------------------------------------------------------------------
# Muestra en pantalla los números del 1 al 10, uno en cada línea.
# Pista: range(inicio, fin, paso). Recuerda que "fin" no se incluye.
#
# Ejemplo de ejecución:
#     1
#     2
#     ...
#     10
# -----------------------------------------------------------------------------
def ejercicio5():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 6 · Tabla de multiplicar                              (for + range)
# -----------------------------------------------------------------------------
# Pide un número y muestra su tabla de multiplicar del 1 al 10.
#
# Ejemplo de ejecución:
#     ¿Qué tabla quieres? 7
#     7 x 1 = 7
#     7 x 2 = 14
#     ...
#     7 x 10 = 70
# -----------------------------------------------------------------------------
def ejercicio6():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 7 · Suma de 1 a N                                  (for + acumulador)
# -----------------------------------------------------------------------------
# Pide un número entero positivo N y calcula la suma 1 + 2 + 3 + ... + N.
# Pista: crea una variable suma = 0 ANTES del bucle y ve sumando en cada vuelta.
#
# Ejemplo de ejecución:
#     Escribe un número: 5
#     La suma de 1 a 5 es 15
# -----------------------------------------------------------------------------
def ejercicio7():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 8 · Números pares hasta N                     (for + if + contador)
# -----------------------------------------------------------------------------
# Pide un número N. Muestra todos los números pares entre 1 y N
# y, al final, cuántos pares has encontrado.
# Pista: necesitas un for, un if dentro, y un contador que empiece en 0.
#
# Ejemplo de ejecución:
#     Escribe un número: 9
#     2
#     4
#     6
#     8
#     Hay 4 números pares entre 1 y 9
# -----------------------------------------------------------------------------
def ejercicio8():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 9 · Contraseña con 3 intentos                          (while + if)
# -----------------------------------------------------------------------------
# La contraseña correcta es "python2bach".
# Pide la contraseña al usuario. Si falla, vuelve a pedírsela, pero como
# MÁXIMO 3 intentos en total. Muestra cuántos intentos le quedan cada vez.
#  - Si acierta: "Acceso concedido"
#  - Si gasta los 3 intentos sin acertar: "Cuenta bloqueada"
# Pista: usa un contador de intentos y una condición con "and" en el while.
#
# Ejemplo de ejecución:
#     Contraseña: hola
#     Incorrecta. Te quedan 2 intentos
#     Contraseña: python
#     Incorrecta. Te quedan 1 intentos
#     Contraseña: python2bach
#     Acceso concedido
# -----------------------------------------------------------------------------
def ejercicio9():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 10 · Calculadora con menú                   (while + if-elif-else)
# -----------------------------------------------------------------------------
# Crea una calculadora que muestre este menú y se repita hasta elegir 0:
#     1. Sumar
#     2. Restar
#     3. Multiplicar
#     4. Dividir
#     0. Salir
# Si la opción es 1, 2, 3 o 4: pide dos números y muestra el resultado.
# Si es 0: muestra "¡Hasta pronto!" y termina.
# Cualquier otra opción: "Opción no válida".
# RETO: si se intenta dividir entre 0, muestra "No se puede dividir entre 0".
#
# Ejemplo de ejecución:
#     1. Sumar
#     2. Restar
#     3. Multiplicar
#     4. Dividir
#     0. Salir
#     Elige una opción: 3
#     Primer número: 4
#     Segundo número: 5
#     Resultado: 20.0
#     1. Sumar
#     ...
#     Elige una opción: 0
#     ¡Hasta pronto!
# -----------------------------------------------------------------------------
def ejercicio10():
    # Escribe tu código aquí
    pass


# =============================================================================
#  PROGRAMA PRINCIPAL (no hace falta modificarlo)
#  Muestra un menú para elegir qué ejercicio ejecutar.
# =============================================================================
def main():
    opcion = ""
    while opcion != "0":
        print()
        print("=" * 40)
        print("   EJERCICIOS DE CONDICIONALES Y BUCLES")
        print("=" * 40)
        print(" 1. ¿Mayor de edad?")
        print(" 2. Par o impar")
        print(" 3. ¿Cuál es mayor?")
        print(" 4. Calificación")
        print(" 5. Contar del 1 al 10")
        print(" 6. Tabla de multiplicar")
        print(" 7. Suma de 1 a N")
        print(" 8. Números pares hasta N")
        print(" 9. Contraseña con 3 intentos")
        print("10. Calculadora con menú")
        print(" 0. Salir")
        opcion = input("¿Qué ejercicio quieres ejecutar? ")
        print()

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            ejercicio10()
        elif opcion == "0":
            print("¡Hasta la próxima!")
        else:
            print("Opción no válida. Escribe un número del 0 al 10.")


main()
