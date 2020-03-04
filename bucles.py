contador=0
mi_email= input("introduce tu correo: ")

for x in mi_email:
    if (x== "@" or x== "."):                           #perfeccionar el ejercicio 
        contador+= 1 

if contador== 2:
    print("correcto")                            
else:
    print("incorrecto ")


for i in range(5,50,3):
    print(f"Valor de la variable {i}")


# valido= False
# email= input(" Introduzca su email: ")
# for i in range(len(email)):
#     if email[i]== "@":
#         valido=True
# if valido:
#     print("email correcto")
# else:
#     print(" email incorrecto ")
