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
from funciones import tour_puerto
from funciones import desgutacion
from funciones import Trotar_pueblo
from funciones import lugares_historicos
from funciones import restaurante
from funciones import prom_gasto
from funciones import no_tour
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
        cupos_tours={
                        "Tour en el puerto":{"cupos":10},
                        "Degustacion de comida":{"cupos":100},
                        "Trotar por el pueblo":{"cupos":"ilimitados"},
                        "Visita a lugares historicos":{"cupos":15}
                }
        lista_letras=list(ascii_uppercase)
        lista=["simple","premium","vip"]
        ventas=[]
        for i, barco in enumerate(dic):
                nombre=dic[i]["name"]
                ruta= dic[i]["route"]
                fecha_de_salida=dic[i]["departure"]
                precio= dic[i]["cost"]
                info_pisos= dic[i]["rooms"]
                cap_habi= dic[i]["capacity"]
                creuceros.append(Cruise(nombre,ruta,fecha_de_salida,precio,info_pisos,cap_habi))
                
        

                        
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

        try:
                with open("Tours.txt", "r", encoding="utf-8") as documento:
                        cupos=documento.read()
                        cupos_tours=json.loads(cupos)

        except:
                cupos_tours={
                        "Tour en el puerto":{"cupos":10},
                        "Degustacion de comida":{"cupos":100},
                        "Trotar por el pueblo":{"cupos":"ilimitados"},
                        "Visita a lugares historicos":{"cupos":15}
                }


        restau={}
        try:
                with open("Menu.txt", "r", encoding="utf-8") as resta:
                        men=resta.read()
                        restau=json.loads(men)

        except:        
                for x in creuceros:
                        restau[x.name]={}
                
        while True:
                try:
                        color=Fore.LIGHTWHITE_EX
                        menu=input(f""" {color} Bienvendio al programa de gestion de cruceros SAMANCARIBEAN: 
                        1.Cruzeros disponibles.
                        2.Gestion de habitaciones
                        3.Descocupar habitacion
                        4.Buscar habitacion
                        5.Gestion de tours
                        6.Gestion de restaurantes
                        7.Estadisticas
                        8.Salir
                        >>> """)
                        
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
                                
                                print("Gestion de tours")
                                while True:
                                        try:
                                                ask=input("Ingrese su dni: ")
                                                if ask not in db:
                                                        print("No registrado")
                                                        break
                                                else:
                                                        print("elija un tour")
                                                tour=input("""
                                                1.Tour en el puerto 
                                                2.Degustación de comida local
                                                3.Trotar por el pueblo/ciudad
                                                4.Visita a lugares históricos
                                                5.Salir
                                                >>>""")
                                                if tour=="1":
                                                        monto_final=tour_puerto(ask,cupos_tours)
                                                        db[ask]["tour"]=monto_final
                                                        print("gracias por su compra")
                                                        break
                                                elif tour=="2":
                                                        monto_final=desgutacion(ask,cupos_tours)
                                                        db[ask]["tour"]=monto_final
                                                        print("gracias por su compra")
                                                        break
                                                elif tour=="3":
                                                        Trotar_pueblo(ask,cupos_tours)
                                                        print("Gracias por su compra")
                                                        break
                                                elif tour=="4":
                                                        monto_final=lugares_historicos(ask,cupos_tours)
                                                        db[ask]["tour"]=monto_final
                                                        print("Gracias por su compra")
                                                        break
                                                elif tour=="5":
                                                        break
                                        except:
                                                print("error")
                                
                        elif menu=="6":
                                barco=select_barco()
                                restaurante(restau,barco)
                                continue
                        elif menu=="7":
                                prom_gasto(db)
                                print("<>"*10)
                                no_tour(db)
                                continue
                        elif menu=="8":
                                with open("habitaciones.txt", "w", encoding="utf-8") as archivo:
                                        archivo.write(json.dumps(barcos,ensure_ascii=False))
                                with open("Base_de_datos.txt", "w", encoding="utf-8") as file:
                                        file.write(json.dumps(db,ensure_ascii=False))
                                with open("Tours.txt", "w", encoding="utf-8") as documento:
                                        documento.write(json.dumps(cupos_tours,ensure_ascii=False))
                                with open("Menu.txt", "w", encoding="utf-8") as resta:
                                        resta.write(json.dumps(restau,ensure_ascii=False))

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