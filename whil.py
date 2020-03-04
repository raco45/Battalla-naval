# i= 1
# while i<=10:
#     print(" Ejecucion " + str(i) )
#     i= i +1 
# print(" termino la ejecucion ")

# edad=int(input(" introduce la edad "))
# while edad< 5 or edad>100:
#     print(" has introducido una edad negativa. vuelve a intentarlo")
#     edad= int(input("Introduce tu edad por favor: "))

# print("Gracias por colaborar. Puedes pasar")
# print(" Edad del aspirante "+ str(edad))
import math
print(" Programa de calculo de raiz cuadrad")
numero= int(input(" Introduce un numero por favor: "))

intentos= 0

while numero<0:
    print(" no se puede hallar la raiz de un numero negativo")

    if intentos ==2:
        print("  Has consumido demasidos intentos. El programa ha finalizado")
        break

    numero= int(input(" Introduce un numero por favor: "))
    if numero<0:
        intentos= intentos+1 

if intentos < 2: 
    solucion= math.sqrt(numero)
    print("la raiz cuadrad de "+ str(numero)+ " es "+ str(solucion))