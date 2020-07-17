import colorama
from colorama import Fore,Back,Style
from clasesM1 import Cruise
from clasesM2 import Room 
from clasesM2 import Sencilla
from clasesM2 import Premium
from clasesM2 import Vip
from clasesM2 import Traveler
import requests 
from string import ascii_letters
from string import ascii_uppercase


def api():
    url= "https://saman-caribbean.vercel.app/api/cruise-ships"
    response= requests.request("GET",url)
    dic=response.json()
    return dic

def api_nombre():
    while True:
        dic=api()

        for i, barco in enumerate(dic):
            print(f"{i+1} {dic[i]['name']} ")

        option=int(input("Ingrese el barco "))

        ship_selected=dic[option-1]

        
        print(f""" Nombre:{ship_selected['name']}
        Ruta:{ship_selected['route']} 
        Salida: {ship_selected['departure']}
        Habitaciones: {ship_selected['rooms']}
        Capacidad: {ship_selected['capacity']}
        """)
#print(api_nombre())       
#def repre_cruzero():
    

def matrixPrinter(matricita,lista_dicc):
    coolString= ""
    for i in range(len(matricita)):
        coolString+="["
        for j in range(len(matricita[i])):
            if lista_dicc[i][matricita[i][j]]!=" ":
                coolString+= Fore.RED + matricita[i][j]
            else:
                coolString+= Fore.GREEN + matricita[i][j]
            if j!= len(matricita[i])-1:
                coolString+= Fore.WHITE + ","
        coolString+=Fore.WHITE + "]\n"
    return coolString

def matriz_hab(barcos,barco,tipo_hab):
    matriz=[]
    for x in range(len(barcos[barco][tipo_hab])):
        matriz.append(list(barcos[barco][tipo_hab][x].keys()))

    print(matrixPrinter(matriz,barcos[barco][tipo_hab]))


def mostrar_barcos(cruzeros):
    while True:
        try:
            menu=input("""Desea comprar su boleto en base a: 
            1. Barco
            2. Destino
            >>>> """)
            if menu =="1": 
                cont=0
                for x in cruzeros:
                    cont+=1
                    print(f"Barco nro {cont}")
                    print(x.show_info())

            elif menu=="2":
                dest=input("Indique el destino: ").title()
                for x in cruzeros:
                    if dest in x.route: 
                        print(x.show_info())
            #// ANCHOR # Completar para cuando no encuentre destino
            break  
                    
        except:
            print("error")


def select_barco():
    while True:
        try:
            print("Elija un barco")
            dic=api()
            for i, barco in enumerate(dic):
                print(f"{i+1} {dic[i]['name']} ")
            option=int(input("Ingrese el barco "))
            ship_selected=dic[option-1]
            return ship_selected["name"]
            
            
        except:
            print("Ese barco no se encuentra disponible")

def cap_tip_hab(cruzeros,barco):
    print("Capacidad por tipo de habitacion: ")
    for crucero in cruzeros:
        if barco==crucero.name:
            for key, value in crucero.room_capacity.items():
                print(f"{key}: {value} personas")

def select_hab():
    while True:
        try:
            tipo_hab=input("""Indique la habitacion que desea:
        1.Sencilla
        2.Premium
        3.VIP
        >>> """)
            if tipo_hab=="1":
                tipo_hab="simple"
            elif tipo_hab=="2":
                tipo_hab="premiun"
            elif tipo_hab=="3":
                tipo_hab="vip"
            else:
                raise Exception
            return tipo_hab
        except:
            print("No disponemos de otro tipo de habitacion")

def cant_personas(cruzeros,barco,tipo_hab,travelers):
    for x in cruzeros:
        if x.name == barco:
            if travelers > x.room_capacity[tipo_hab]:
                print("Debera comprar 2 o mas habitaciones")
                return x.room_capacity[tipo_hab]
            elif travelers <= x.room_capacity[tipo_hab]:
                print("Debara comprar 1 habitacion")
                return x.room_capacity[tipo_hab]
                #// ANCHOR  terminar la funcion preguntar por los formularios 

def formulario(hab,db):
    while True:
        try:
            
            new_user={}
            new_user["Nombre"]=nombre()
            new_user["Dni"]=dni()
            new_user["edad"]=edad()
            new_user["Status"]="On Board"
            db[hab]=new_user
            return "Registro exitoso"
            #return Traveler(Full_name,dni,edad,disc,hab,status)

            
        except:
            print("error")
            
def pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab):
   
    lista_letras=["A","B","C"]
    while True:
        try:
            habitacion=" "
            hall=input("Indique el pasillo (ej: A, B, C): ").upper()
            num=int(input("Indique el numero de la habitacion:"))
            referencia=" "
            habitacion= hall + str(num)
            if hall in lista_letras:
                if num not in range(len(barcos[barco][tipo_hab][0])+1):
                    print("No se encontro esa habitacion")
                    continue
                indice=lista_letras.index(hall)
                if barcos[barco][tipo_hab][indice][habitacion] == " ":
                    if tipo_hab=="simple":
                        barcos[barco][tipo_hab][indice][habitacion]=Sencilla(hall,num,cap_hab,referencia)
                    elif tipo_hab=="premium":
                        barcos[barco][tipo_hab][indice][habitacion]=Premium(hall,num,cap_hab,referencia)
                    elif tipo_hab=="vip":
                        barcos[barco][tipo_hab][indice][habitacion]=Vip(hall,num,cap_hab,referencia)
                    return habitacion
                        # //ANCHOR Buscar como meter la capacidad de las habitaciones, meter la referencia
                else:
                    print("Habitacion Ocupada")
                    continue
            else:
                raise Exception
            
        except:
            print("error")
            
            
                
def pedir_formu(travelers,cap_hab,barcos,barco,tipo_hab,cruzeros,db):
    while True:
        
        if travelers > cap_hab:
            cont_1=0
            hab=pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab)
            while cont_1 < cap_hab:
                formulario(hab,db)
                cont_1+=1
            return pedir_formu(travelers-cap_hab,cap_hab,barcos,barco,tipo_hab,cruzeros,db)
        elif travelers <=cap_hab:
            cont=0
            hab=pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab)
            while cont < travelers:
                print(formulario(hab,db))
                cont+=1
            return "Exitoso"


def nombre():
    while True:
        try:
            while True:
                nombre= (input(" por favor ingrese su nombre: ")).strip()
                if nombre.isalpha():
                    break
                if len(nombre) < 2 or nombre.isdigit() or " " in nombre:
                    print("no valido")
                    continue
                
            while True:    
                nombre2=(input(" ingrese su segundo nombre (si tiene): ")).strip()
                if nombre2=="":
                    break
                if nombre2.isalpha():
                    break
                if len(nombre2) < 2 or nombre2.isdigit() or " " in nombre2:
                    print("no valido")
                    continue

                
            while True:
                apellido= (input(" ingrese su apellido: ")).strip()
                if len(apellido) < 2 or apellido.isdigit() or " " in apellido:
                    print("No valido")
                    continue
                if apellido.isalpha():
                    break
        
            while True:
                apellido2= (input(" ingrese su segundo apellido (opcional): ")).strip()
                if apellido2=="":
                    break
                if len(apellido2) < 2 or apellido2.isdigit() or " " in apellido2:
                    print('No valido')
                    continue
                if apellido2.isalpha():
                    break
            Full_name=(" {} {} {} {}".format(nombre.title(),nombre2.title(),apellido.title(),apellido2.title()))
            
            return Full_name
        except:
            print("Error")


def dni():
    while True:
        try:
        
            dni=input("Ingrese su documento de identidad: ").strip()
            if len(dni) < 3 or len(dni)>8 or dni.isalpha(): 
                print("No valido")
                continue
            else:
                break
            return dni
        except:
            print("Error")

def edad():
    while True:
        try:
            
            edad= input(" Ingrese su edad: ").strip()
            if not edad.isdigit():
                print("Por favor ingresa tu edad")
            elif  int(edad)>150:
                print("intenta otra vez ")
            else: 
                break
            return edad
        except:
            print("Error")

def discapacidad():
            
    while True:
        try:
            disc=input("""Sufre de algun tipo de discapacidad:  
                1.Si
                2.No
                >>> """)
            if disc =="1":
                disc=True 
                break
            elif disc =="2":
                disc= False
                break
            else:
                print("error")
                continue
            return disc
        except:
                print("Error")

             


