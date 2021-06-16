
import numpy as np
import sys
# Desarrollado por: Jeremy León
print("\t\t\tPROGRAMA PARA MULTIPLICAR MATRICES CON NUMPY\n")
r1 = int(input("Ingrese el numero de filas de la primera matriz: "))
c1 = int(input("Ingrese el numero de columnas de la primera matriz: "))
r2 = int(input("Ingrese el numero de filas de la segunda matriz: "))
c2 = int(input("Ingrese el numero de columnas de la segunda matriz: "))

if c1 != r2:
    print("\t------No se puede hacer la multiplicación de matrices-------")
    sys.exit()
matriz1 = np.zeros((r1, c1))
matriz2 = np.zeros((r2, c2))
matrizr = np.zeros((r1, c2))
print("Ingrese los elementos de la primera matriz")
for r in range(0, r1):
    for c in range(0, c1):
        matriz1[(r, c)] = input("Elemento a["+str(r+1)+"]["+str(c+1)+"]: ")
print("Valores ingresados de la primera matriz: \na="+str(matriz1))
print("Ingrese los elementos de la segunda matriz")
for r in range(0, r2):
    for c in range(0, c2):
        matriz2[(r, c)] = input("Elemento b["+str(r+1)+"]["+str(c+1)+"]: ")
# Multiplicación
for r in range(0, r1):
    for c in range(0, c2):
        for k in range(0, r2):
            matrizr[r, c] += matriz1[r, k]*matriz2[k, c]
print("Valores ingresados de la segunda matriz:\nb="+str(matriz2))
print("\nLa matriz de resultado tienes las dimenciones: "+str("c=["+str(r1)+"]["+str(c2)+"]"))
print("c=")
print(matrizr)
