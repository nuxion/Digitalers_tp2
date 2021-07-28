import random
import time

inicio = time.time()

#Mensaje de vienvenida
print("**************************")
print("Bienvenido a Casino Royale")
print("**************************")

#Variables globales
# No es una buena practica usar variables globales.
# Hace dificil ademas razonar sobre el codigo.
ganaste = 0       #fichas
perdiste = 0      #fichas
_ganaste = 0      #noches
_perdiste = 0     #noches
total_jugadas = 0 #apuestas totales


#Funcion
def apuestas(fichas , probabilidad , maximo_jugado):
    tmp = 0
    # cuidado tambien con la combinacion ingles/español para la nomemclatura.
    # idealmente uno u otro.
    winrate = 0
    lossrate = 0
    # cuidado con el nombre de variables:
    # maximo_jugado podria entenderse como la
    # cantidad de veces que ya se juegom en cambio es un
    # cantidad_de_veces_a_jugar, o simplemente "a_jugar" o "maximo_juegos",
    # "max_juegos"
    while fichas > 0 and tmp < maximo_jugado:
        lista = [0,1]
        resultado = random.choices(lista,weights=[1-probabilidad,probabilidad])
        borrame = resultado.pop(0)
        if borrame == 1:
            fichas += 1
            winrate += 1
            #print("Ganaste")
        elif borrame == 0:
            fichas -= 1
            lossrate += 1
            #print("Perdiste")
        tmp += 1
    if fichas == 0:
        contador =- 1
        # Puede ser complicado trabajar con resultados de listas:
        # a largo plazo requiere volver sobre la funcion para entender
        # en que orden se mandaron ciertas variables. 
        return(f"Perdiste, te quedan {fichas} fichas y apostaste {tmp} veces", contador , winrate , lossrate)
    if fichas > 0:
        contador = 1
        return(f"Ganaste, te quedan {fichas} fichas y apostaste {tmp} veces", contador , winrate , lossrate)


#Llamar 20 veces la funcion
for _ in range(1,21):
    
    print(f"\nResultado de la noche numero {_}:")
    
    #Llama la funcion y crea una tupla con todos los datos a utilizar
    datos = apuestas(50 , 0.4 , 300)#fichas, probabilidad, maximo jugado
    print(f"{datos[0]}")

    
    #Calculo de "apuestas" ganadas por "noche"
    # Esta logica podria estar dentro de la funcion apuestas ,
    # y que el for ... range() sea simplemente para iterar las simulaciones/jugadas.
    ganaste = datos[2]
    perdiste = datos[3]
    jugadas = ganaste + perdiste
    total_jugadas += jugadas
    print(f"Tu porcentaje de victoria fue de: {(ganaste*100/jugadas):.2f}%")
    
    

    #Calculo de "noches" ganadas/perdidas
    if datos[1] == 1:
        _ganaste += 1
    elif datos[1] == -1:
        _perdiste += 1
       

print("\n******************************************")
print(f"* Ganaste {_ganaste} noches y perdiste {_perdiste} noches. *")
print(f"* Apostaste {total_jugadas} veces.                  *")
# Bien la funcion de redondeo.
print(f"* Un promedio de {total_jugadas/20:.2f} por noche.       *")
print("******************************************\n")
    

    
    
#Tiempo empleado en correr el programa
fin = time.time()
diferencia = fin - inicio
print(f"\nDemoramos {diferencia} en correr todo el programa")
