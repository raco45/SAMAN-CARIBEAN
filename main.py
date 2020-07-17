from clases import Cruise
from clases import Room
from clases import Sencilla
from clases import Premium
from clases import Vip
from clases import Traveler
import colorama 
from colorama import Fore,Back,Style
from funciones import matrixPrinter
from funciones import matriz_hab
from funciones import select_hab
from funciones import select_barco
from funciones import mostrar_barcos
from funciones import cant_personas
from funciones import pedir_habitacion
from funciones import cap_tip_hab
from funciones import formulario
from funciones import pedir_formu
import requests
from funciones import api
from string import ascii_letters
from string import ascii_uppercase









def main():
    creuceros=[]
    db={

}

    lista_letras=list(ascii_uppercase)
    lista=["simple","premium","vip"]

    dic=api()
    for i, barco in enumerate(dic):
            nombre=dic[i]["name"]
            ruta= dic[i]["route"]
            fecha_de_salida=dic[i]["departure"]
            precio= dic[i]["cost"]
            info_pisos= dic[i]["rooms"]
            cap_habi= dic[i]["capacity"]
            creuceros.append(Cruise(nombre,ruta,fecha_de_salida,precio,info_pisos,cap_habi))

    # print(crear_estructura(creuceros,lista,lista_letras))
    barcos={

    }
    for barco in creuceros:
            nombre=barco.name
            pisos= barco.floors_info
            barcos[nombre]={}
            for tipo_habitacion in pisos.keys():
                    barcos[nombre][tipo_habitacion]=[]
                    dim_piso=pisos[tipo_habitacion]
                    for i in range(dim_piso[0]):
                            barcos[nombre][tipo_habitacion].append({})

                            for j in range(dim_piso[1]):
                                    stringcito=lista_letras[i]+str(j+1)
                                    barcos[nombre][tipo_habitacion][i][stringcito]=" "


   










    print("Informacion del barco")
    mostrar_barcos(creuceros)
    barco=select_barco()

    cap_tip_hab(creuceros,barco)
    tipo_hab=select_hab()
    travelers=int(input("Indique la cantidad de personas en el viaje (incluyendose): "))

    cap_hab=cant_personas(creuceros,barco,tipo_hab,travelers)
    print(cap_hab)
    matriz_hab(barcos,barco,tipo_hab)
    habitaciones=[]

    pedir_formu(travelers,cap_hab,barcos,barco,tipo_hab,creuceros,db)
    matriz_hab(barcos,barco,tipo_hab)

    

    # formulario("A2",db)
    # print(db)











main()