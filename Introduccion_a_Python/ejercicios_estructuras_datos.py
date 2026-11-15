# =============================================================================
#  EJERCICIOS: ESTRUCTURAS DE DATOS (LISTAS, DICCIONARIOS Y CONJUNTOS)
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
#  - Si el ejercicio trae datos ya escritos (una lista o un diccionario),
#    úsalos tal cual: tu programa debe funcionar aunque cambien.
#  - Ejecuta el archivo: aparecerá un menú para probar el ejercicio que quieras.
#  - El "Ejemplo de ejecución" muestra cómo debe verse tu programa.
#    Lo que aparece detrás de los ":" en las preguntas lo escribe el usuario.
#
#  ¡No toques la función main() del final!
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1 · Mis colores favoritos                    (lista, índices, len)
# -----------------------------------------------------------------------------
# Usando la lista "colores", muestra:
#   - la lista completa
#   - el primer color y el último (usa índices)
#   - cuántos colores hay
# Después cambia el segundo color por "violeta" y vuelve a mostrar la lista.
#
# Ejemplo de ejecución:
#     Mis colores: ['azul', 'verde', 'rojo', 'negro', 'blanco']
#     El primero es azul y el último es blanco
#     Tengo 5 colores favoritos
#     Lista cambiada: ['azul', 'violeta', 'rojo', 'negro', 'blanco']
# -----------------------------------------------------------------------------
def ejercicio1():
    colores = ["azul", "verde", "rojo", "negro", "blanco"]
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 2 · Cinco números                  (append, sum, max, min, len)
# -----------------------------------------------------------------------------
# Crea una lista vacía y pide 5 números enteros al usuario con un bucle for,
# añadiéndolos a la lista con append(). Al final muestra:
#   la lista, la suma, el mayor, el menor y la media.
#
# Ejemplo de ejecución:
#     Número 1: 4
#     Número 2: 10
#     Número 3: 7
#     Número 4: 1
#     Número 5: 8
#     Lista: [4, 10, 7, 1, 8]
#     Suma: 30
#     Mayor: 10
#     Menor: 1
#     Media: 6.0
# -----------------------------------------------------------------------------
def ejercicio2():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 3 · Lista de la compra                  (while, append, in, sort)
# -----------------------------------------------------------------------------
# Pide productos al usuario hasta que escriba "fin".
#   - Si el producto YA está en la lista, muestra "Ya lo tienes apuntado".
#   - Si no, añádelo.
# Al terminar, muestra la lista ORDENADA alfabéticamente, un producto
# por línea, y el número total de productos.
#
# Ejemplo de ejecución:
#     Producto (fin para terminar): pan
#     Producto (fin para terminar): leche
#     Producto (fin para terminar): pan
#     Ya lo tienes apuntado
#     Producto (fin para terminar): arroz
#     Producto (fin para terminar): fin
#     - arroz
#     - leche
#     - pan
#     Total: 3 productos
# -----------------------------------------------------------------------------
def ejercicio3():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 4 · Aprobados y suspensos                  (filtrar con for + if)
# -----------------------------------------------------------------------------
# A partir de la lista "notas", crea DOS listas nuevas: "aprobados"
# (nota >= 5) y "suspensos" (nota < 5). Muestra ambas listas, cuántas
# notas hay en cada una y la media de toda la clase redondeada a 2
# decimales (pista: round(numero, 2)).
#
# Ejemplo de ejecución:
#     Aprobados: [6.5, 8, 5, 9.5, 7] -> 5 notas
#     Suspensos: [3, 4.5, 2] -> 3 notas
#     Media de la clase: 5.69
# -----------------------------------------------------------------------------
def ejercicio4():
    notas = [6.5, 3, 8, 4.5, 5, 9.5, 2, 7]
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 5 · Asignaturas en común                              (conjuntos)
# -----------------------------------------------------------------------------
# Ana y Luis tienen estas listas de asignaturas (algunas están repetidas
# por error). Usando conjuntos, muestra:
#   - las asignaturas de Ana sin repetir
#   - las asignaturas que tienen en común
#   - todas las asignaturas distintas entre los dos y cuántas son
# (El orden en que aparecen puede ser distinto: es normal en los conjuntos.)
#
# Ejemplo de ejecución:
#     Ana (sin repetir): {'TIC', 'Historia', 'Inglés', 'Matemáticas'}
#     En común: {'TIC', 'Inglés'}
#     Todas: {'TIC', 'Historia', 'Inglés', 'Matemáticas', 'Biología', 'Química'}
#     Entre los dos cursan 6 asignaturas distintas
# -----------------------------------------------------------------------------
def ejercicio5():
    ana = ["Matemáticas", "TIC", "Inglés", "TIC", "Historia"]
    luis = ["Biología", "Inglés", "Química", "TIC", "Química"]
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 6 · Ficha personal                     (diccionario: crear y usar)
# -----------------------------------------------------------------------------
# Pide al usuario su nombre, su edad (entero) y su ciudad, y guárdalos
# en un diccionario con las claves "nombre", "edad" y "ciudad".
#   1. Muestra la ficha recorriendo el diccionario con items().
#   2. "Ha pasado un año": suma 1 a la edad dentro del diccionario.
#   3. Añade la clave "curso" con el valor "2º Bachillerato".
#   4. Muestra el diccionario completo.
#
# Ejemplo de ejecución:
#     Nombre: Marta
#     Edad: 17
#     Ciudad: Sevilla
#     nombre: Marta
#     edad: 17
#     ciudad: Sevilla
#     Un año después: {'nombre': 'Marta', 'edad': 18, 'ciudad': 'Sevilla', 'curso': '2º Bachillerato'}
# -----------------------------------------------------------------------------
def ejercicio6():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 7 · Mini traductor                   (diccionario, in / get, while)
# -----------------------------------------------------------------------------
# Usando el diccionario "traductor", pide palabras en español y muestra
# su traducción al inglés, hasta que el usuario escriba "salir".
#   - Si la palabra no está, muestra "No conozco esa palabra" y pregunta
#     por su traducción para AÑADIRLA al diccionario.
# Al salir, muestra cuántas palabras conoce ahora el traductor.
#
# Ejemplo de ejecución:
#     Palabra en español: casa
#     casa -> house
#     Palabra en español: libro
#     No conozco esa palabra. ¿Cómo se dice en inglés? book
#     Palabra en español: libro
#     libro -> book
#     Palabra en español: salir
#     Ahora conozco 6 palabras
# -----------------------------------------------------------------------------
def ejercicio7():
    traductor = {"casa": "house", "perro": "dog", "gato": "cat",
                 "rojo": "red", "agua": "water"}
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 8 · Caja de la tienda                (diccionario + acumulador)
# -----------------------------------------------------------------------------
# El diccionario "precios" guarda el precio de cada producto.
#   1. Muestra la carta de productos con sus precios.
#   2. Pide productos hasta que el usuario escriba "fin". Para cada uno:
#        - si existe, pide la cantidad y suma (precio x cantidad) al total
#        - si no existe, muestra "Ese producto no está a la venta"
#   3. Al final muestra el total a pagar redondeado a 2 decimales.
#
# Ejemplo de ejecución:
#     --- CARTA ---
#     café: 1.2 €
#     tostada: 1.8 €
#     zumo: 2.5 €
#     croissant: 1.5 €
#     Producto: café
#     Cantidad: 2
#     Producto: pizza
#     Ese producto no está a la venta
#     Producto: zumo
#     Cantidad: 1
#     Producto: fin
#     Total a pagar: 4.9 €
# -----------------------------------------------------------------------------
def ejercicio8():
    precios = {"café": 1.2, "tostada": 1.8, "zumo": 2.5, "croissant": 1.5}
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 9 · Contador de vocales                    (diccionario contador)
# -----------------------------------------------------------------------------
# Pide una frase al usuario. Usando un diccionario, cuenta cuántas veces
# aparece cada vocal (a, e, i, o, u). Muestra el resultado vocal a vocal
# y, al final, cuál es la vocal que más se repite.
# Pistas:
#   - Empieza con  vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
#   - frase.lower() pasa la frase a minúsculas.
#   - Recorre la frase letra a letra con un for.
#
# Ejemplo de ejecución:
#     Escribe una frase: Me gusta programar en Python
#     a: 3
#     e: 2
#     i: 0
#     o: 2
#     u: 1
#     La vocal que más se repite es la 'a'
# -----------------------------------------------------------------------------
def ejercicio9():
    # Escribe tu código aquí
    pass


# -----------------------------------------------------------------------------
# EJERCICIO 10 · Gestor de notas de la clase    (lista de diccionarios + menú)
# -----------------------------------------------------------------------------
# La lista "clase" contiene diccionarios con el nombre y la nota de cada
# alumno. Crea un menú que se repita hasta elegir 0:
#     1. Añadir alumno       -> pide nombre y nota y lo añade a la lista
#     2. Ver listado         -> muestra cada alumno con su nota
#     3. Estadísticas        -> media de la clase y alumno con la nota más alta
#     4. Ver aprobados       -> solo los alumnos con nota >= 5
#     0. Salir
#
# Ejemplo de ejecución:
#     1. Añadir alumno
#     2. Ver listado
#     3. Estadísticas
#     4. Ver aprobados
#     0. Salir
#     Opción: 3
#     Media de la clase: 6.17
#     Mejor nota: Ana con un 8.5
#     ...
#     Opción: 0
#     ¡Hasta pronto!
# -----------------------------------------------------------------------------
def ejercicio10():
    clase = [
        {"nombre": "Ana", "nota": 8.5},
        {"nombre": "Luis", "nota": 4},
        {"nombre": "Eva", "nota": 6},
    ]
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
        print("=" * 45)
        print("   EJERCICIOS DE ESTRUCTURAS DE DATOS")
        print("=" * 45)
        print(" 1. Mis colores favoritos")
        print(" 2. Cinco números")
        print(" 3. Lista de la compra")
        print(" 4. Aprobados y suspensos")
        print(" 5. Asignaturas en común")
        print(" 6. Ficha personal")
        print(" 7. Mini traductor")
        print(" 8. Caja de la tienda")
        print(" 9. Contador de vocales")
        print("10. Gestor de notas de la clase")
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
