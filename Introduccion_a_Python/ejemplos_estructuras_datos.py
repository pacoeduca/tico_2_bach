# =============================================================================
#  EJEMPLOS: ESTRUCTURAS DE DATOS EN PYTHON
#  Listas, diccionarios y conjuntos
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
#  PARTE 1. LISTAS
# =============================================================================

# -----------------------------------------------------------------------------
# Ejemplo 1. Crear una lista y ver cuántos elementos tiene
# -----------------------------------------------------------------------------
## Una lista se escribe entre corchetes [ ] con los elementos separados por comas.
## Puede contener textos, números, booleanos... ¡o una mezcla!

# frutas = ["manzana", "pera", "uva"]
# notas = [7, 9.5, 5]
# mezcla = ["Ana", 17, True]
# vacia = []
#
# print(frutas)
# print(notas)
# print(mezcla)
# print(vacia)
# print("La lista frutas tiene", len(frutas), "elementos")


# -----------------------------------------------------------------------------
# Ejemplo 2. Acceder a un elemento por su índice
# -----------------------------------------------------------------------------
## Cada elemento tiene una posición (índice). ¡La primera es la 0!
## Los índices negativos cuentan desde el final: -1 es el último.

# dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
# print(dias[0])     # primer elemento
# print(dias[2])     # tercer elemento
# print(dias[-1])    # último elemento
# print(dias[-2])    # penúltimo
#
# ## Descomenta la siguiente línea para ver el error IndexError:
# # print(dias[5])


# -----------------------------------------------------------------------------
# Ejemplo 3. Modificar elementos
# -----------------------------------------------------------------------------
## A diferencia de los textos, las listas SÍ se pueden cambiar.

# notas = [4, 7, 9]
# print("Antes:", notas)
# notas[0] = 5        # cambiamos el primer elemento
# notas[-1] = 10      # cambiamos el último
# print("Después:", notas)


# -----------------------------------------------------------------------------
# Ejemplo 4. Trocear una lista (slicing)
# -----------------------------------------------------------------------------
## lista[inicio:fin] devuelve un trozo. Como en range(), "fin" NO se incluye.

# numeros = [10, 20, 30, 40, 50, 60]
# print(numeros[1:4])    # posiciones 1, 2 y 3
# print(numeros[:3])     # los 3 primeros
# print(numeros[3:])     # desde la posición 3 hasta el final
# print(numeros[-2:])    # los 2 últimos


# -----------------------------------------------------------------------------
# Ejemplo 5. Recorrer una lista con for
# -----------------------------------------------------------------------------
## En cada vuelta, la variable "producto" toma el siguiente elemento.

# compra = ["leche", "pan", "huevos", "tomates"]
# for producto in compra:
#     print("- Tengo que comprar", producto)


# -----------------------------------------------------------------------------
# Ejemplo 6. Recorrer con índice y elemento a la vez
# -----------------------------------------------------------------------------
## range(len(lista)) genera las posiciones 0, 1, 2...

# podio = ["Laura", "Mario", "Sofía"]
# for i in range(len(podio)):
#     print("Puesto", i + 1, ":", podio[i])


# -----------------------------------------------------------------------------
# Ejemplo 7. ¿Está un elemento en la lista? (in)
# -----------------------------------------------------------------------------

# invitados = ["Ana", "Luis", "Eva"]
# nombre = input("¿Cómo te llamas? ")
# if nombre in invitados:
#     print("Adelante,", nombre)
# else:
#     print("Lo siento, no estás en la lista")


# -----------------------------------------------------------------------------
# Ejemplo 8. Añadir elementos: append() e insert()
# -----------------------------------------------------------------------------
## append(x) añade al FINAL.  insert(posición, x) añade donde le digamos.

# compra = []
# compra.append("pan")
# compra.append("leche")
# print(compra)
# compra.insert(0, "fruta")      # lo coloca en la posición 0
# print(compra)


# -----------------------------------------------------------------------------
# Ejemplo 9. Rellenar una lista pidiendo datos al usuario
# -----------------------------------------------------------------------------
## Patrón muy habitual: empezar con una lista vacía y añadir con append().

# amigos = []
# for i in range(3):
#     nombre = input("Nombre de un amigo: ")
#     amigos.append(nombre)
# print("Tus amigos son:", amigos)


# -----------------------------------------------------------------------------
# Ejemplo 10. Eliminar elementos: remove() y pop()
# -----------------------------------------------------------------------------
## remove(x) borra el elemento x (la primera vez que aparece).
## pop() quita el último y lo DEVUELVE; pop(i) quita el de la posición i.

# colores = ["rojo", "verde", "azul", "amarillo"]
# colores.remove("verde")
# print(colores)
#
# ultimo = colores.pop()
# print("He sacado:", ultimo)
# print(colores)
#
# primero = colores.pop(0)
# print("He sacado:", primero)
# print(colores)


# -----------------------------------------------------------------------------
# Ejemplo 11. Ordenar e invertir: sort(), reverse() y sorted()
# -----------------------------------------------------------------------------
## sort() ordena la lista ORIGINAL. sorted() crea una lista NUEVA ordenada.

# numeros = [5, 2, 9, 1, 7]
# print(sorted(numeros))     # nueva lista ordenada
# print(numeros)             # la original no ha cambiado
#
# numeros.sort()             # ahora sí cambia la original
# print(numeros)
#
# numeros.sort(reverse=True) # de mayor a menor
# print(numeros)
#
# nombres = ["Pablo", "Ana", "Zoe", "Carlos"]
# nombres.reverse()          # invierte el orden
# print(nombres)


# -----------------------------------------------------------------------------
# Ejemplo 12. Buscar y contar: index() y count()
# -----------------------------------------------------------------------------

# letras = ["a", "b", "c", "b", "b"]
# print("La 'c' está en la posición", letras.index("c"))
# print("La 'b' aparece", letras.count("b"), "veces")


# -----------------------------------------------------------------------------
# Ejemplo 13. Funciones útiles: len, sum, max, min
# -----------------------------------------------------------------------------

# notas = [6.5, 8, 4, 9, 7.5]
# print("Número de notas:", len(notas))
# print("Suma:", sum(notas))
# print("Nota máxima:", max(notas))
# print("Nota mínima:", min(notas))
# print("Media:", sum(notas) / len(notas))


# -----------------------------------------------------------------------------
# Ejemplo 14. Filtrar una lista con for + if + append
# -----------------------------------------------------------------------------
## Creamos una lista nueva solo con los elementos que cumplen una condición.

# notas = [6.5, 8, 4, 9, 3, 7.5]
# aprobados = []
# for n in notas:
#     if n >= 5:
#         aprobados.append(n)
# print("Aprobados:", aprobados)
# print("Han aprobado", len(aprobados), "de", len(notas))


# =============================================================================
#  PARTE 2. DICCIONARIOS
# =============================================================================

# -----------------------------------------------------------------------------
# Ejemplo 15. Crear un diccionario y acceder por clave
# -----------------------------------------------------------------------------
## Un diccionario guarda pares  clave: valor  entre llaves { }.
## No se accede por posición, sino por la CLAVE.

# alumno = {"nombre": "Lucía", "edad": 17, "curso": "2º Bach"}
# print(alumno)
# print(alumno["nombre"])
# print(alumno["edad"])
# print("El diccionario tiene", len(alumno), "pares")


# -----------------------------------------------------------------------------
# Ejemplo 16. Añadir, modificar y borrar
# -----------------------------------------------------------------------------
## Si la clave NO existe, se añade. Si YA existe, se modifica su valor.

# precios = {"pan": 1.2, "leche": 0.9}
# precios["huevos"] = 2.5     # añade una clave nueva
# precios["pan"] = 1.3        # modifica una clave existente
# print(precios)
#
# del precios["leche"]        # borra una clave
# print(precios)


# -----------------------------------------------------------------------------
# Ejemplo 17. Claves que no existen: KeyError, in y get()
# -----------------------------------------------------------------------------
## Pedir una clave que no existe produce un error (KeyError).
## Para evitarlo: comprobamos con "in" o usamos get(clave, valor_por_defecto).

# capitales = {"España": "Madrid", "Francia": "París", "Italia": "Roma"}
#
# pais = input("Escribe un país: ")
# if pais in capitales:
#     print("Su capital es", capitales[pais])
# else:
#     print("No conozco ese país")
#
# print(capitales.get("Portugal", "Desconocida"))
#
# ## Descomenta la siguiente línea para ver el error KeyError:
# # print(capitales["Portugal"])


# -----------------------------------------------------------------------------
# Ejemplo 18. Recorrer un diccionario: keys(), values() e items()
# -----------------------------------------------------------------------------

# stock = {"lápices": 30, "gomas": 12, "reglas": 5}
#
# print("Claves:")
# for producto in stock.keys():      # también vale:  for producto in stock:
#     print(producto)
#
# print("Valores:")
# for cantidad in stock.values():
#     print(cantidad)
#
# print("Claves y valores:")
# for producto, cantidad in stock.items():
#     print(producto, "->", cantidad)


# -----------------------------------------------------------------------------
# Ejemplo 19. Otros métodos: pop() y update()
# -----------------------------------------------------------------------------

# coche = {"marca": "Seat", "modelo": "Ibiza", "año": 2018}
#
# anio = coche.pop("año")             # quita la clave y devuelve su valor
# print("He quitado el año:", anio)
# print(coche)
#
# coche.update({"color": "rojo", "modelo": "León"})   # añade y modifica a la vez
# print(coche)


# -----------------------------------------------------------------------------
# Ejemplo 20. Rellenar un diccionario con datos del usuario
# -----------------------------------------------------------------------------

# agenda = {}
# for i in range(3):
#     nombre = input("Nombre: ")
#     telefono = input("Teléfono: ")
#     agenda[nombre] = telefono
# print(agenda)
#
# buscar = input("¿De quién quieres el teléfono? ")
# print(agenda.get(buscar, "No está en la agenda"))


# -----------------------------------------------------------------------------
# Ejemplo 21. Contar con un diccionario
# -----------------------------------------------------------------------------
## Si el elemento ya está en el diccionario, sumamos 1; si no, lo creamos con 1.

# votos = ["rojo", "azul", "rojo", "verde", "rojo", "azul"]
# recuento = {}
# for color in votos:
#     if color in recuento:
#         recuento[color] = recuento[color] + 1
#     else:
#         recuento[color] = 1
# print(recuento)


# -----------------------------------------------------------------------------
# Ejemplo 22. Contar letras de una palabra
# -----------------------------------------------------------------------------
## Lo mismo que el ejemplo anterior, pero en versión corta con get().

# palabra = input("Escribe una palabra: ")
# letras = {}
# for letra in palabra:
#     letras[letra] = letras.get(letra, 0) + 1
# for letra, veces in letras.items():
#     print(letra, "aparece", veces, "veces")


# -----------------------------------------------------------------------------
# Ejemplo 23. Diccionario con listas como valores
# -----------------------------------------------------------------------------
## Los valores pueden ser cualquier cosa, también listas.

# notas = {"Ana": [7, 8, 9], "Luis": [4, 5, 6]}
# notas["Ana"].append(10)            # añadimos una nota a Ana
# for nombre, lista in notas.items():
#     media = sum(lista) / len(lista)
#     print(nombre, "tiene de media", media)


# -----------------------------------------------------------------------------
# Ejemplo 24. Lista de diccionarios (una pequeña base de datos)
# -----------------------------------------------------------------------------
## Cada elemento de la lista es un diccionario con la "ficha" de un alumno.

# clase = [
#     {"nombre": "Ana", "nota": 8},
#     {"nombre": "Luis", "nota": 4},
#     {"nombre": "Eva", "nota": 6.5},
# ]
#
# for alumno in clase:
#     if alumno["nota"] >= 5:
#         print(alumno["nombre"], "aprueba con un", alumno["nota"])
#     else:
#         print(alumno["nombre"], "suspende con un", alumno["nota"])
#
# clase.append({"nombre": "Pablo", "nota": 9})
# print("Ahora hay", len(clase), "alumnos")


# =============================================================================
#  PARTE 3. CONJUNTOS (de un vistazo)
# =============================================================================

# -----------------------------------------------------------------------------
# Ejemplo 25. Un conjunto no guarda repetidos ni tiene orden
# -----------------------------------------------------------------------------
## Fíjate en que "rojo" solo aparece una vez y el orden puede cambiar.
## Ojo: {} crea un DICCIONARIO vacío. Un conjunto vacío se crea con set().

# colores = {"rojo", "azul", "rojo", "verde"}
# print(colores)
# colores.add("negro")
# colores.remove("azul")
# print(colores)
# print("rojo" in colores)


# -----------------------------------------------------------------------------
# Ejemplo 26. Quitar duplicados de una lista (el uso más típico)
# -----------------------------------------------------------------------------

# numeros = [1, 2, 2, 3, 3, 3, 4]
# sin_repetir = list(set(numeros))
# print(sin_repetir)
# print("Hay", len(sin_repetir), "valores distintos")


# -----------------------------------------------------------------------------
# Ejemplo 27. Operaciones entre conjuntos
# -----------------------------------------------------------------------------
## |  unión (todos)        &  intersección (los comunes)
## -  diferencia (los de a que no están en b)

# futbol = {"Ana", "Luis", "Eva"}
# baloncesto = {"Eva", "Pablo", "Ana"}
# print("Hacen algún deporte:", futbol | baloncesto)
# print("Hacen los dos:", futbol & baloncesto)
# print("Solo fútbol:", futbol - baloncesto)


# =============================================================================
#  ¡Fin de los ejemplos! Ahora ve a ejercicios_estructuras_datos.py
# =============================================================================
