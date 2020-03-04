miTupla= ("Juan", 13,1,1995)
miLista= list(miTupla)        # de tupla a lista
print(miLista)

miLista= ["Juan", 13,1,1995, 13 ]
miTupla=tuple(miLista)               # de lista a tupla 
print(miTupla)

print("Juan" in miTupla )            # verificar elemento en mi tupla

print(miTupla.count(13))               #contar la cantidad de un elemento en la tupla
print(len(miTupla))                     # longitud de la tupla

miTupla=("Juan",)                                 #tupla unitaria
print(len(miTupla))

miTupla= "juan", 13,1, 1995                          # empaquedado de tupla  
print(miTupla)

miTupla= ("Juan", 13,1,1995)                          #desempaqueado de tupla
nombre, dia, mes, agno = miTupla
print(nombre)
print(dia)
print(agno)
print(mes)

