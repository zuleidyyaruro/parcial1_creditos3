# Defina una función eliminar repetidos donde al ingresar un nombre elimine las vocales repetidas.
# 1. INGRESAR: CAMILA
# SALIDA
# 2. CMIL “se ha eliminado la vocal A”

print("----------ELIMINACION DE VOCALES REPETIDAS------------")

def eliminarRepetidos():

    nombre=input("Ingrese el nombre: ")
    print("El nombre es: " + nombre)
    nombreLista=list(nombre)
    letrasUnicas=[]

    for i in nombreLista:
        if i not in letrasUnicas:
            letrasUnicas.append(i)
        else:
            if i==i:
                nombreLista.remove(i)
            nombreLista.remove(i)

    print("El nombre sin la vocales repetidas es: ")
    print( nombreLista)

eliminarRepetidos()

# Defina una función eliminar repetidos donde al ingresar un nombre elimine las vocales repetidas.
# 1. INGRESAR: CAMILA
# SALIDA
# 2. CMIL “se ha eliminado la vocal A”

def agreguarGusto(diccionario, persona, gusto):
    if persona not in diccionario:
        diccionario[persona] = [gusto]
    else:
        if gusto not in diccionario[persona]:
            diccionario[persona] = diccionario[persona]+[gusto]
    return diccionario



diccionarioEjemplo = {
    "zuleidy": ["leer", "videojuegos", "tecnologia"]
}
diccionarioNuevo = agreguarGusto(diccionarioEjemplo, "zuleidy", "series")
print("prueba 1:\n", diccionarioNuevo, "\n-\n")

# Definir una función denominada procedimiento() que tome una lista de números enteros e imprima un histograma
# en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******

def procedimiento():
    listaNumeros=[4, 9, 7]

    a=0

    for i in listaNumeros:
        a=i*"*"
        
        print(a)

procedimiento()