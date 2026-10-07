# ============================================================
#  entrada_salida_condicionales.py
#  Pedir datos al usuario y tomar decisiones
# ============================================================
#
#  ¿CÓMO SE USA ESTE ARCHIVO?
#
#  Igual que en hola_mundo.py:
#  1. Ejecuta el programa tal como está.
#  2. Ve bajando y descomenta los ejemplos de uno en uno.
#     Para descomentar, borra la almohadilla (#) y el espacio
#     que va detrás. NO borres los espacios de la izquierda.
#  3. Guarda, ejecuta y observa.
#
#  CONSEJO: descomenta UN ejemplo cada vez y vuelve a comentarlo
#  antes de pasar al siguiente. Si no, el programa te hará
#  muchas preguntas seguidas.
#
#  Cuando el programa te pida algo, escribe tu respuesta en la
#  consola y pulsa Intro.
# ============================================================


def main():
    print("=== Entrada, salida y condicionales ===")

    # ########################################################
    #  PARTE 1: ENTRADA DE DATOS CON input()
    # ########################################################

    # --------------------------------------------------------
    # EJEMPLO 1: Tu primer input()
    # input() detiene el programa y espera a que escribas algo.
    # Lo que escribes se guarda en una VARIABLE (aquí, "nombre").
    # Una variable es como una caja con una etiqueta donde
    # guardamos un dato para usarlo después.
    # --------------------------------------------------------
    # nombre = input("¿Cómo te llamas? ")
    # print("¡Hola,", nombre + "!")

    # --------------------------------------------------------
    # EJEMPLO 2: Usar la variable varias veces
    # Una vez guardado el dato, puedes usarlo todas las veces
    # que quieras.
    # --------------------------------------------------------
    # comida = input("¿Cuál es tu comida favorita? ")
    # print("Así que te gusta", comida)
    # print("Yo también quiero", comida, "para cenar")

    # --------------------------------------------------------
    # EJEMPLO 3: Pedir varios datos
    # --------------------------------------------------------
    # nombre = input("Nombre: ")
    # ciudad = input("Ciudad: ")
    # print(nombre, "vive en", ciudad)

    # --------------------------------------------------------
    # EJEMPLO 4: ¡CUIDADO! input() siempre devuelve TEXTO
    # Escribe 5 y luego 3. ¿El resultado es el que esperabas?
    # Recuerda lo que pasaba con "ja" * 5 en hola_mundo.py...
    # --------------------------------------------------------
    # a = input("Escribe un número: ")
    # b = input("Escribe otro número: ")
    # print("La suma es:", a + b)

    # --------------------------------------------------------
    # EJEMPLO 5: Convertir texto a número entero con int()
    # int() transforma el texto "5" en el número 5.
    # Ahora sí, 5 + 3 da 8.
    # --------------------------------------------------------
    # a = int(input("Escribe un número: "))
    # b = int(input("Escribe otro número: "))
    # print("La suma es:", a + b)

    # --------------------------------------------------------
    # EJEMPLO 6: Números con decimales con float()
    # Para decimales usa float(). En Python el decimal se
    # escribe con PUNTO, no con coma: 1.75, no 1,75.
    # --------------------------------------------------------
    # altura = float(input("¿Cuánto mides en metros? (ej: 1.65) "))
    # print("Mides", altura * 100, "centímetros")

    # --------------------------------------------------------
    # EJEMPLO 7: Una pequeña calculadora
    # --------------------------------------------------------
    # x = float(input("Primer número: "))
    # y = float(input("Segundo número: "))
    # print("Suma:", x + y)
    # print("Resta:", x - y)
    # print("Multiplicación:", x * y)
    # print("División:", x / y)

    # --------------------------------------------------------
    # EJEMPLO 8: Provoca un error (a propósito)
    # Descomenta y, cuando te pida la edad, escribe una
    # PALABRA (por ejemplo: "quince"). Lee el error.
    # ¿Por qué crees que int() no puede convertirla?
    # --------------------------------------------------------
    # edad = int(input("¿Cuántos años tienes? "))
    # print("El año que viene tendrás", edad + 1)

    # ########################################################
    #  PARTE 2: CONDICIONALES (if, elif, else)
    # ########################################################
    #
    #  Un condicional permite que el programa tome decisiones:
    #  "SI pasa esto, haz aquello".
    #
    #  Para comparar usamos:
    #    ==  igual que          !=  distinto de
    #    >   mayor que          <   menor que
    #    >=  mayor o igual      <=  menor o igual
    #
    #  ¡OJO! = guarda un valor en una variable.
    #         == compara dos valores. No son lo mismo.
    #
    #  MUY IMPORTANTE:
    #   - La línea del if termina con dos puntos (:)
    #   - Lo que va "dentro" del if lleva espacios a la
    #     izquierda (sangría). Así Python sabe qué instrucciones
    #     dependen de la condición.
    # ########################################################

    # --------------------------------------------------------
    # EJEMPLO 9: if simple
    # El mensaje solo aparece si la condición se cumple.
    # Prueba con 20 y luego con 10.
    # --------------------------------------------------------
    # edad = int(input("¿Cuántos años tienes? "))
    # if edad >= 18:
    #     print("Eres mayor de edad")
    # print("Esta línea se muestra siempre")

    # --------------------------------------------------------
    # EJEMPLO 10: if ... else
    # else es el "si no": lo que pasa cuando la condición
    # NO se cumple.
    # --------------------------------------------------------
    # edad = int(input("¿Cuántos años tienes? "))
    # if edad >= 18:
    #     print("Eres mayor de edad")
    # else:
    #     print("Eres menor de edad")

    # --------------------------------------------------------
    # EJEMPLO 11: if ... elif ... else
    # elif significa "si no, pero si...". Sirve para tener
    # más de dos caminos. Python comprueba las condiciones
    # de arriba abajo y se queda con la PRIMERA que se cumple.
    # --------------------------------------------------------
    # nota = float(input("¿Qué nota has sacado? (0 a 10) "))
    # if nota >= 9:
    #     print("Sobresaliente")
    # elif nota >= 7:
    #     print("Notable")
    # elif nota >= 6:
    #     print("Bien")
    # elif nota >= 5:
    #     print("Suficiente")
    # else:
    #     print("Insuficiente")

    # --------------------------------------------------------
    # EJEMPLO 12: Comparar textos
    # Prueba a escribir "python" y luego "Python".
    # ¿Pasa lo mismo? Python distingue mayúsculas y minúsculas.
    # --------------------------------------------------------
    # respuesta = input("¿Qué lenguaje estamos aprendiendo? ")
    # if respuesta == "Python":
    #     print("¡Correcto!")
    # else:
    #     print("Mmm... no es ese")

    # --------------------------------------------------------
    # EJEMPLO 13: Una contraseña
    # != significa "distinto de".
    # --------------------------------------------------------
    # clave = input("Introduce la contraseña: ")
    # if clave != "1234":
    #     print("Acceso denegado")
    # else:
    #     print("Bienvenido al sistema")

    # --------------------------------------------------------
    # EJEMPLO 14: ¿Par o impar?
    # El operador % da el RESTO de una división.
    # Si al dividir entre 2 el resto es 0, el número es par.
    # --------------------------------------------------------
    # numero = int(input("Escribe un número entero: "))
    # if numero % 2 == 0:
    #     print(numero, "es par")
    # else:
    #     print(numero, "es impar")

    # --------------------------------------------------------
    # EJEMPLO 15: ¿Cuál es mayor?
    # --------------------------------------------------------
    # a = int(input("Primer número: "))
    # b = int(input("Segundo número: "))
    # if a > b:
    #     print("El mayor es", a)
    # elif b > a:
    #     print("El mayor es", b)
    # else:
    #     print("Los dos son iguales")

    # --------------------------------------------------------
    # EJEMPLO 16: Combinar condiciones con "and"
    # and: se tienen que cumplir LAS DOS condiciones.
    # --------------------------------------------------------
    # edad = int(input("¿Cuántos años tienes? "))
    # if edad >= 12 and edad <= 17:
    #     print("Eres adolescente")
    # else:
    #     print("No eres adolescente")

    # --------------------------------------------------------
    # EJEMPLO 17: Combinar condiciones con "or"
    # or: basta con que se cumpla UNA de las condiciones.
    # --------------------------------------------------------
    # dia = input("¿Qué día de la semana es hoy? ")
    # if dia == "sábado" or dia == "domingo":
    #     print("¡Es fin de semana!")
    # else:
    #     print("Toca ir a clase")

    # --------------------------------------------------------
    # EJEMPLO 18: Varias instrucciones dentro del if
    # Todas las líneas con la misma sangría van "dentro".
    # --------------------------------------------------------
    # temperatura = float(input("¿Qué temperatura hace? "))
    # if temperatura > 30:
    #     print("Hace mucho calor")
    #     print("Bebe agua")
    #     print("Ponte crema solar")
    # else:
    #     print("La temperatura es agradable")

    # --------------------------------------------------------
    # EJEMPLO 19: Provoca un error (a propósito)
    # A este if le faltan los dos puntos (:) al final.
    # Descomenta las dos líneas, ejecuta y lee el error.
    # Luego arréglalo.
    # --------------------------------------------------------
    # if 5 > 3
    #     print("Cinco es mayor que tres")

    # --------------------------------------------------------
    # EJEMPLO 20: Provoca otro error (a propósito)
    # Aquí el print NO tiene sangría: está a la misma altura
    # que el if. Descomenta las dos líneas, ejecuta y lee el
    # error. Luego arréglalo añadiendo 4 espacios delante
    # del print.
    # --------------------------------------------------------
    # if 5 > 3:
    # print("Cinco es mayor que tres")

    # --------------------------------------------------------


# ============================================================
#  No borres esto: le dice a Python que empiece por main().
# ============================================================
if __name__ == "__main__":
    main()
