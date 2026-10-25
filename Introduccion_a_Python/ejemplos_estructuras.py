# =============================================================================
#  EJEMPLOS: ESTRUCTURAS DE CONTROL EN PYTHON
#  Condicionales (if, elif, else) y bucles (for, while)
#  TIC - 2º Bachillerato
# =============================================================================
#
#  CÓMO USAR ESTE ARCHIVO
#  ----------------------
#  Todos los ejemplos están comentados (cada línea empieza por #).
#  1. Busca un ejemplo.
#  2. Selecciona SOLO las líneas de código de ese ejemplo y descoméntalas
#     (atajo: Ctrl + /  en Windows/Linux  ·  Cmd + /  en Mac).
#  3. Ejecuta el archivo y observa lo que aparece en pantalla.
#  4. Vuelve a comentar el ejemplo antes de pasar al siguiente.
#
#  Las líneas que empiezan por "##" son explicaciones: déjalas comentadas.
#  Consejo: antes de ejecutar, intenta adivinar qué va a salir en pantalla.
# =============================================================================


# =============================================================================
#  PARTE 1. CONDICIONALES
# =============================================================================

# -----------------------------------------------------------------------------
# Ejemplo 1. Comparaciones: el resultado siempre es True o False
# -----------------------------------------------------------------------------
## Una condición es una "pregunta" que Python responde con True (verdadero)
## o False (falso). Fíjate: == compara, mientras que = guarda un valor.

print(5 == 5)      # ¿5 es igual a 5?          -> True
print(5 != 3)      # ¿5 es distinto de 3?      -> True
print(2 > 7)       # ¿2 es mayor que 7?        -> False
print(18 >= 18)    # ¿18 es mayor o igual?     -> True
print("hola" == "Hola")   # Mayúsculas y minúsculas cuentan -> False


# -----------------------------------------------------------------------------
# Ejemplo 2. if simple
# -----------------------------------------------------------------------------
## El bloque con sangría (4 espacios) solo se ejecuta si la condición es True.
## La última línea no tiene sangría: se ejecuta SIEMPRE.
## Prueba a escribir 20 y después 15.

# edad = int(input("¿Cuántos años tienes? "))   # int() convierte el texto a número
# if edad >= 18:
#     print("Ya puedes votar.")
# print("Gracias por usar el programa.")


# -----------------------------------------------------------------------------
# Ejemplo 3. if - else (dos caminos)
# -----------------------------------------------------------------------------
## El operador % da el RESTO de una división: 7 % 2 = 1, 8 % 2 = 0.
## Si el resto de dividir entre 2 es 0, el número es par.

# numero = int(input("Escribe un número entero: "))
# if numero % 2 == 0:
#     print(numero, "es PAR")
# else:
#     print(numero, "es IMPAR")


# -----------------------------------------------------------------------------
# Ejemplo 4. if - elif - else (varios caminos)
# -----------------------------------------------------------------------------
## Python comprueba las condiciones de arriba abajo y ejecuta SOLO la primera
## que sea verdadera. El else recoge "todo lo demás".
## float() permite escribir decimales, como 6.5

# nota = float(input("¿Qué nota has sacado? "))
# if nota < 5:
#     print("Suspenso")
# elif nota < 7:
#     print("Aprobado")
# elif nota < 9:
#     print("Notable")
# else:
#     print("Sobresaliente")


# -----------------------------------------------------------------------------
# Ejemplo 5. Comparar textos
# -----------------------------------------------------------------------------
## También podemos comparar cadenas de texto. Prueba con "rojo", "verde" y "azul".

# color = input("¿De qué color está el semáforo? ")
# if color == "verde":
#     print("Puedes pasar")
# elif color == "amarillo":
#     print("Precaución")
# elif color == "rojo":
#     print("¡Para!")
# else:
#     print("Ese color no existe en un semáforo")


# -----------------------------------------------------------------------------
# Ejemplo 6. Operadores lógicos: and, or, not
# -----------------------------------------------------------------------------
## and -> se tienen que cumplir LAS DOS condiciones
## or  -> basta con que se cumpla UNA
## not -> invierte el resultado (True pasa a False y al revés)

# edad = int(input("Edad: "))
# if edad >= 12 and edad <= 17:
#     print("Eres adolescente")
#
# dia = input("¿Qué día es hoy? ")
# if dia == "sábado" or dia == "domingo":
#     print("¡Es fin de semana!")
# else:
#     print("Toca ir a clase")


# -----------------------------------------------------------------------------
# Ejemplo 7. if dentro de otro if (anidados)
# -----------------------------------------------------------------------------
## Fíjate en que el segundo if lleva 4 espacios y su print lleva 8.

# numero = int(input("Escribe un número: "))
# if numero > 0:
#     print("Es positivo")
#     if numero > 100:
#         print("¡Y además es mayor que 100!")
# elif numero < 0:
#     print("Es negativo")
# else:
#     print("Es cero")


# =============================================================================
#  PARTE 2. BUCLES
# =============================================================================

# -----------------------------------------------------------------------------
# Ejemplo 8. Bucle for con range(): repetir N veces
# -----------------------------------------------------------------------------
## range(5) genera 0, 1, 2, 3, 4  (empieza en 0 y NO incluye el 5).
## En cada vuelta, la variable i toma el siguiente valor.

# for i in range(5):
#     print("Vuelta número", i)
# print("Bucle terminado")


# -----------------------------------------------------------------------------
# Ejemplo 9. Las distintas formas de range()
# -----------------------------------------------------------------------------
## range(inicio, fin, paso)  -> el valor "fin" nunca se incluye.
## end=" " hace que print no salte de línea y deje un espacio.

# print("Del 1 al 5:")
# for i in range(1, 6):
#     print(i, end=" ")
# print()   # salto de línea
#
# print("Pares del 2 al 10:")
# for i in range(2, 11, 2):
#     print(i, end=" ")
# print()
#
# print("Cuenta atrás:")
# for i in range(10, 0, -1):
#     print(i, end=" ")
# print("¡Despegue!")


# -----------------------------------------------------------------------------
# Ejemplo 10. for recorriendo un texto
# -----------------------------------------------------------------------------
## Un for también puede recorrer las letras de una palabra, una a una.

# palabra = input("Escribe una palabra: ")
# for letra in palabra:
#     print(letra)


# -----------------------------------------------------------------------------
# Ejemplo 11. Tabla de multiplicar
# -----------------------------------------------------------------------------
## El número de vueltas lo conocemos (10): por eso usamos for.

# n = int(input("¿Qué tabla quieres ver? "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# -----------------------------------------------------------------------------
# Ejemplo 12. Acumulador: sumar números
# -----------------------------------------------------------------------------
## 1) Creamos la variable ANTES del bucle con valor 0.
## 2) En cada vuelta le sumamos algo.
## 3) Mostramos el resultado DESPUÉS del bucle (sin sangría).

# suma = 0
# for n in range(1, 6):
#     suma = suma + n          # también se puede escribir: suma += n
#     print("Sumo", n, "-> la suma va por", suma)
# print("Resultado final:", suma)


# -----------------------------------------------------------------------------
# Ejemplo 13. Contador + if dentro de un for
# -----------------------------------------------------------------------------
## Un contador es un acumulador que suma 1 cada vez que pasa algo.

# contador = 0
# for n in range(1, 21):
#     if n % 3 == 0:
#         print(n, "es múltiplo de 3")
#         contador = contador + 1
# print("Hay", contador, "múltiplos de 3 entre 1 y 20")


# -----------------------------------------------------------------------------
# Ejemplo 14. Pedir varios datos con un for
# -----------------------------------------------------------------------------
## Pedimos 3 notas y calculamos la media.

# total = 0
# for i in range(1, 4):
#     nota = float(input("Nota " + str(i) + ": "))
#     total = total + nota
# media = total / 3
# print("Tu media es", media)


# -----------------------------------------------------------------------------
# Ejemplo 15. Bucle while: repetir MIENTRAS se cumpla una condición
# -----------------------------------------------------------------------------
## Antes de cada vuelta, while comprueba la condición.
## IMPORTANTE: algo debe cambiar dentro del bucle (aquí, contador),
## si no, el bucle no termina nunca. Para pararlo: Ctrl + C.

# contador = 1
# while contador <= 5:
#     print("Contador vale", contador)
#     contador = contador + 1
# print("Fin del while")


# -----------------------------------------------------------------------------
# Ejemplo 16. while para repetir hasta que el usuario acierte
# -----------------------------------------------------------------------------
## No sabemos cuántas veces se equivocará el usuario: por eso usamos while.

# clave = input("Introduce la contraseña: ")
# while clave != "python":
#     print("Contraseña incorrecta. Inténtalo de nuevo.")
#     clave = input("Introduce la contraseña: ")
# print("¡Acceso concedido!")


# -----------------------------------------------------------------------------
# Ejemplo 17. while para validar un dato
# -----------------------------------------------------------------------------
## Seguimos pidiendo la nota hasta que esté entre 0 y 10.

# nota = float(input("Nota (0-10): "))
# while nota < 0 or nota > 10:
#     print("Esa nota no es válida.")
#     nota = float(input("Nota (0-10): "))
# print("Nota guardada:", nota)


# -----------------------------------------------------------------------------
# Ejemplo 18. Menú que se repite hasta elegir "salir"
# -----------------------------------------------------------------------------
## Combinamos while (repetir) con if-elif-else (decidir).

# opcion = ""
# while opcion != "0":
#     print("--- MENÚ ---")
#     print("1. Saludar")
#     print("2. Despedirse")
#     print("0. Salir")
#     opcion = input("Elige una opción: ")
#     if opcion == "1":
#         print("¡Hola!")
#     elif opcion == "2":
#         print("¡Hasta luego!")
#     elif opcion == "0":
#         print("Saliendo del programa...")
#     else:
#         print("Opción no válida")

# =============================================================================
#  ¡Fin de los ejemplos! Ahora ve a ejercicios_if_for.py
# =============================================================================
