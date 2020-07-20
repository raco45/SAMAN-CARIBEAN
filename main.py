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
from funciones import desocupar
from funciones import buscar_hab
from funciones import factura
import requests
from funciones import api
from string import ascii_letters
from string import ascii_uppercase
import pickle
import json
import ast
def main():
        creuceros=[]
        db={}
        hab_ocu=[]

        dic=api()
        barcos={}
        lista_letras=list(ascii_uppercase)
        lista=["simple","premium","vip"]
        
        for i, barco in enumerate(dic):
                nombre=dic[i]["name"]
                ruta= dic[i]["route"]
                fecha_de_salida=dic[i]["departure"]
                precio= dic[i]["cost"]
                info_pisos= dic[i]["rooms"]
                cap_habi= dic[i]["capacity"]
                creuceros.append(Cruise(nombre,ruta,fecha_de_salida,precio,info_pisos,cap_habi))

        # try:
        #         with open("texto.txt","r") as base_datos: 
        #                 for fila in base_datos: 
        #                         hab= (fila.strip()).split(",")
        #                         hab_temp=Room(hab[0],hab[1],hab[2],hab[3])
        #                         hab_ocu.append(user_temp)

        # except:
        #         hab_ocu=[]

        try:
                with open("Base_de_datos.txt", "r", encoding="utf-8") as file:
                        text=file.read()
                        db=json.loads(text)
        except:
                db={}

        
        
        
        try:
                with open("habitaciones.txt", "r", encoding="utf-8") as archivo:
                        texto=archivo.read()
                        barcos=json.loads(texto)
        except:
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

        



        
        while True:
                try:
                        color=Fore.LIGHTWHITE_EX
                        menu=input(f""" {color} Bienvendio al programa de gestion de cruceros SAMANCARIBEAN: 
                        1.Cruzeros disponibles.
                        2.Gestion de habitaciones
                        3.Descocupar habitacion
                        4.Buscar habitacion
                        5.Salir
                        >>>""")
                        if menu=="1":
                                print("Informacion del barco")
                                
                                mostrar_barcos(creuceros)
                        elif menu=="2":
                                barco=select_barco()
                                cap_tip_hab(creuceros,barco)
                                tipo_hab=select_hab()
                                travelers=int(input("Indique la cantidad de personas en el viaje (incluyendose): "))
                                cap_hab=cant_personas(creuceros,barco,tipo_hab,travelers)

                                print(cap_hab)
                                matriz_hab(barcos,barco,tipo_hab)
                                habitaciones=[]

                                lista_dni=[]
                                pedir_formu(travelers,cap_hab,barcos,barco,tipo_hab,creuceros,db,lista_letras,hab_ocu,lista_dni)
                                print(lista_dni)
                                matriz_hab(barcos,barco,tipo_hab)
                                factura(barco,tipo_hab,travelers,lista_dni,creuceros,db)
                        elif menu=="3":
                                desocupar(db,barcos,lista_letras)
                                continue     


                        elif menu=="4":
                                buscar_hab(barcos,creuceros,lista_letras)
                                continue
                        elif menu=="5":
                                with open("habitaciones.txt", "w", encoding="utf-8") as archivo:
                                        archivo.write(json.dumps(barcos,ensure_ascii=False))
                                with open("Base_de_datos.txt", "w", encoding="utf-8") as file:
                                        file.write(json.dumps(db,ensure_ascii=False))
                                
                                # with open("texto.txt","w") as base_datos:                                    #se abre el archivo texto.txt para poder escribir los nuevos datos del que el usuario desea guardar.  
                                #         for hab_temp in hab_ocu:
                                #                 big_string=(f"{hab_temp.letra},{hab_temp.numero},{hab_temp.capacidad},{hab_temp.referencia}\n")
                                #                 base_datos.write(big_string)
                                break

                        else:
                                raise Exception
                except:
                        print("Error")














    








main()