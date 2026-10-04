# ============================================================
#  hola_mundo.py
#  Tu primer programa en Python
# ============================================================
#
#  ¿CÓMO SE USA ESTE ARCHIVO?
#
#  1. Ejecuta el programa tal como está. Verás un solo mensaje.
#  2. Ve bajando por los ejemplos. Cada uno tiene una o varias
#     líneas que empiezan por "# print(...)".
#  3. Para "activar" una línea, borra la almohadilla (#) y el
#     espacio que va detrás. ¡OJO! No borres los espacios de la
#     izquierda: Python los necesita para saber que esa línea
#     pertenece a la función main.
#  4. Guarda el archivo, vuelve a ejecutarlo y observa qué cambia.
#
#  Las líneas que empiezan por # son COMENTARIOS: Python las
#  ignora por completo. Sirven para que las personas entiendan
#  el código.
# ============================================================


def main():
    # --------------------------------------------------------
    # EJEMPLO 0: El clásico "Hola, mundo"
    # Esta línea ya está activa. print() muestra en pantalla
    # lo que pongas entre los paréntesis.
    # El texto va siempre entre comillas.
    # --------------------------------------------------------
    print("¡Hola, mundo!")

    # --------------------------------------------------------
    # EJEMPLO 1: Escribir otro mensaje
    # Cambia el texto por tu nombre y vuelve a ejecutar.
    # --------------------------------------------------------
    # print("Me llamo Ana y estoy aprendiendo Python")

    # --------------------------------------------------------
    # EJEMPLO 2: Comillas simples o dobles
    # Python acepta las dos. El resultado es el mismo.
    # --------------------------------------------------------
    # print("Esto va entre comillas dobles")
    # print('Esto va entre comillas simples')

    # --------------------------------------------------------
    # EJEMPLO 3: Varios print seguidos
    # Cada print escribe en una línea nueva.
    # --------------------------------------------------------
    # print("Primera línea")
    # print("Segunda línea")
    # print("Tercera línea")

    # --------------------------------------------------------
    # EJEMPLO 4: Una línea en blanco
    # Un print() vacío deja una línea en blanco.
    # --------------------------------------------------------
    # print("Antes del hueco")
    # print()
    # print("Después del hueco")

    # --------------------------------------------------------
    # EJEMPLO 5: Números
    # Los números NO llevan comillas.
    # --------------------------------------------------------
    # print(42)
    # print(3.14)

    # --------------------------------------------------------
    # EJEMPLO 6: Python como calculadora
    # Compara las dos líneas: ¿por qué dan resultados distintos?
    # --------------------------------------------------------
    # print(2 + 3)
    # print("2 + 3")

    # --------------------------------------------------------
    # EJEMPLO 7: Más operaciones
    #   +  suma        -  resta
    #   *  multiplica  /  divide
    # --------------------------------------------------------
    # print(10 - 4)
    # print(6 * 7)
    # print(20 / 4)

    # --------------------------------------------------------
    # EJEMPLO 8: Varias cosas en un mismo print
    # Separa los elementos con comas. Python pone un espacio
    # entre ellos automáticamente.
    # --------------------------------------------------------
    # print("Tengo", 15, "años")
    # print("El resultado de 5 + 5 es", 5 + 5)

    # --------------------------------------------------------
    # EJEMPLO 9: Cambiar el separador (sep)
    # Con sep= decides qué se pone entre los elementos.
    # --------------------------------------------------------
    # print("uno", "dos", "tres", sep="-")
    # print("12", "05", "2026", sep="/")

    # --------------------------------------------------------
    # EJEMPLO 10: Cambiar el final de línea (end)
    # Normalmente print salta de línea al terminar.
    # Con end= puedes cambiar eso.
    # --------------------------------------------------------
    # print("Hola", end=" ")
    # print("en la misma línea")

    # --------------------------------------------------------
    # EJEMPLO 11: Saltos de línea dentro del texto (\n)
    # \n dentro de las comillas significa "salta de línea".
    # --------------------------------------------------------
    # print("Línea 1\nLínea 2\nLínea 3")

    # --------------------------------------------------------
    # EJEMPLO 12: Tabuladores (\t)
    # \t añade un espacio grande, útil para alinear columnas.
    # --------------------------------------------------------
    # print("Nombre\tEdad")
    # print("Ana\t15")
    # print("Luis\t16")

    # --------------------------------------------------------
    # EJEMPLO 13: Comillas dentro del texto
    # Si el texto lleva comillas dobles, rodéalo con simples
    # (o al revés).
    # --------------------------------------------------------
    # print('Mi profe dijo: "¡Buen trabajo!"')

    # --------------------------------------------------------
    # EJEMPLO 14: Repetir texto
    # Un texto multiplicado por un número se repite.
    # --------------------------------------------------------
    # print("ja" * 5)
    # print("=" * 30)

    # --------------------------------------------------------
    # EJEMPLO 15: Juntar textos
    # El + entre textos los une (sin añadir espacio).
    # --------------------------------------------------------
    # print("Hola" + "Mundo")
    # print("Hola" + " " + "Mundo")

    # --------------------------------------------------------
    # EJEMPLO 16: Un pequeño dibujo
    # ¡Descomenta las cuatro líneas a la vez!
    # --------------------------------------------------------
    # print("  /\\_/\\  ")
    # print(" ( o.o ) ")
    # print("  > ^ <  ")
    # print("¡Miau! Soy un gato hecho con print")

    # --------------------------------------------------------
    # EJEMPLO 17: Provoca un error (a propósito)
    # Descomenta esta línea: le falta la comilla del final.
    # Lee el mensaje de error que da Python. Aprender a leer
    # los errores es parte de programar. Después, vuelve a
    # comentarla o arréglala.
    # --------------------------------------------------------
    # print("Me falta una comilla)

    # --------------------------------------------------------
    # RETO FINAL
    # Escribe tú mismo, debajo de este comentario, varios print
    # que muestren una tarjeta de presentación: tu nombre, tu
    # curso y tu comida favorita, con una línea de "=" arriba
    # y otra abajo.
    # --------------------------------------------------------


# ============================================================
#  Esta parte le dice a Python: "cuando ejecutes este archivo,
#  empieza por la función main". De momento no hace falta que
#  la entiendas del todo; simplemente, no la borres.
# ============================================================
if __name__ == "__main__":
    main()
