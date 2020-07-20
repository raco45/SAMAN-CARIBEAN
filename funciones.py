import colorama
from colorama import Fore,Back,Style
from clases import Cruise
from clases import Room 
from clases import Sencilla
from clases import Premium
from clases import Vip
from clases import Traveler
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
            if lista_dicc[i][matricita[i][j]]=="Ocupada":
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
            tipo_hab=input("""Indique el tipo de habitacion:
        1.Sencilla
        2.Premium
        3.VIP
        >>> """)
            if tipo_hab=="1":
                tipo_hab="simple"
            elif tipo_hab=="2":
                tipo_hab="premium"
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
                

def formulario(dni_1,hab,tipo_hab,db,barcos,barco,cruceros,cap_hab,lista_letras,hab_ocu):
    while True:
        try:
            
            new_user={}
            new_user["Nombre"]=nombre()
            new_user["barco"]=barco
            new_user["tipo hab"]=tipo_hab
            new_user["edad"]=edad()
            if new_user["edad"] > 65 and tipo_hab=="simple":
                hab=age(barcos,barco,cruceros,cap_hab,lista_letras,hab_ocu)
                new_user["hab"]=hab
            else:
                new_user["hab"]=hab
            new_user["discapacidad"]=discapacidad()
            
            

            for x in cruceros:
                if x.name==barco:
                    precio=x.prize[tipo_hab]

                if new_user["discapacidad"]==True:
                    precio_desc=precio-(precio* 0.3)
                    new_user["precio"]=precio_desc
                elif new_user["discapacidad"]==False:
                    if abundante(int(dni_1))==True:  
                        precio_desc=precio-(precio*0.15)
                        new_user["precio"]=precio_desc
                    elif abundante(int(dni_1))==False :
                        if num_primo(int(dni_1))==True:
                            precio_desc=precio-(precio*0.1)
                            new_user["precio"]=precio_desc
                        elif num_primo(int(dni_1))==False:
                           new_user["precio"]=precio
                else:
                    new_user["precio"]=precio

                
            db[dni_1]=new_user
                
                    
            
            
            return "Exitoso"
            

            
        except:
            print("error")
            
def pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab,lista_letras,hab_ocu):
   
    
    while True:
        try:
            habitacion=" "
            hall=input("Indique el pasillo (ej: A, B, C): ").upper()
            num=int(input("Indique el numero de la habitacion:"))
            referencia=" "
            tipo=tipo_hab[0].upper()
            habitacion= tipo + hall + str(num)
            if hall in lista_letras:
                if num not in range(len(barcos[barco][tipo_hab][0])+1):
                    print("No se encontro esa habitacion")
                    continue
                indice=lista_letras.index(hall)
                if barcos[barco][tipo_hab][indice][habitacion[1::]] == " ":
                    if tipo_hab=="simple":
                        barcos[barco][tipo_hab][indice][habitacion[1::]]= "Ocupada"
                        hab_ocu.append(Sencilla(hall,num,cap_hab,referencia))
                        
                    elif tipo_hab=="premium":
                        barcos[barco][tipo_hab][indice][habitacion[1::]]="Ocupada"
                        hab_ocu.append(Premium(hall,num,cap_hab,referencia))
                        
                    elif tipo_hab=="vip":
                        barcos[barco][tipo_hab][indice][habitacion[1::]]="Ocupada"
                        hab_ocu.append(Vip(hall,num,cap_hab,referencia))
                        
                    return habitacion
                        # //ANCHOR Buscar como meter la capacidad de las habitaciones, meter la referencia
                else:
                    print("Habitacion Ocupada")
                    continue
            else:
                raise Exception
            
        except:
            print("error")
            
            
                
def pedir_formu(travelers,cap_hab,barcos,barco,tipo_hab,cruzeros,db,lista_letras,hab_ocu,lista_dni):
    while True:
        precio=0
        
        if travelers > cap_hab:
            
            cont_1=0
            
            
            hab=pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab,lista_letras,hab_ocu)
            
            while cont_1 < cap_hab:
                dni_1=dni()
                print(formulario(dni_1,hab,tipo_hab,db,barcos,barco,cruzeros,cap_hab,lista_letras,hab_ocu))
                cont_1+=1
                lista_dni.append(dni_1)
            return pedir_formu(travelers-cap_hab,cap_hab,barcos,barco,tipo_hab,cruzeros,db,lista_letras,hab_ocu,lista_dni)
        elif travelers <=cap_hab:
            cont=0
            
            hab=pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab,lista_letras,hab_ocu)
            
            while cont < travelers:
                dni_1=dni()
                print(formulario(dni_1,hab,tipo_hab,db,barcos,barco,cruzeros,cap_hab,lista_letras,hab_ocu))
                cont+=1
                lista_dni.append(dni_1)
            return  lista_dni


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
                return dni
                break
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
                return int(edad)
                break
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
               
            elif disc =="2":
                disc= False
                
            else:
                print("error")
                continue
            return disc
        except:
                print("Error")

def desocupar(db,barcos,lista_letras):
    while True:
        try:
            qb=input("Indique su documento de identificacion: ")
            if db.get(qb):
                user=db[qb]
                indice=lista_letras.index(user["hab"][0])
                if barcos[user["barco"]][user["tipo hab"]][indice][user["hab"]]== "Ocupada":
                    barcos[user["barco"]][user["tipo hab"]][indice][user["hab"]]=" "
                    print("La habitacion ha sido desocupada")
                    break
                else:
                    print("La habitacion ya se encuentra desocupada")
                    break
        except:
            print("No esta registrado")            

def buscar_hab(barcos,cruceros,lista_letras):
    while True:
        try:
            
            search=input(""" Desea buscar por:
            1. Tipo
            2. Capacidad
            3. Tipo+pasillo+numero(ej: SA9)
            4. Salir
            >>>  """)
            if search=="1":
                tipo=select_hab() 
                print(Fore.RED + "Ocupada")
                print(Fore.GREEN + "Desocupada")

                for x in cruceros:
                    print(Fore.LIGHTWHITE_EX + x.name)
                    matriz_hab(barcos,x.name,tipo)
                break
            elif search=="2":
                lista_capacitys=[]
                for x in cruceros:
                    lol=x.room_capacity
                    for key, value in lol.items():
                        lista_capacitys.append(value)
                lista=[]
                for x in set(lista_capacitys):
                    lista.append(x)
                
                for i, x in enumerate(lista):
                    print(f"{i+1}. Capacidad:{x} personas")
                capci=int(input("Indique la capacidad que esta buscando: "))
                num=lista[capci-1]
                print(Fore.RED + "Ocupada")
                print(Fore.GREEN + "Desocupada")
                for x in cruceros:
                    lol=x.room_capacity
                    for key, value in lol.items():
                        if num== value:
                            print(Fore.LIGHTWHITE_EX + x.name)
                            
                            matriz_hab(barcos,x.name,key)
            elif search =="3":
                letras_tipo=["S","P","V"]
                while True:
                    barco=select_barco()
                    hab=input(f" {Fore.LIGHTWHITE_EX}Ingrese tipo+pasillo+numero (ej:SA9): ").upper()
                    if hab[0]=="S":
                        tipo_hab="simple"
                    elif hab[0]=="P":
                        tipo_hab="premium"
                    elif hab[0]=="V":
                        tipo_hab="vip"
                    if int(hab[2]) not in range(len(barcos[barco][tipo_hab][0])+1):
                        print("No se encontro esa habitacion")
                        continue
                    if hab[0] not in letras_tipo:
                        continue
                    if hab[1] not in lista_letras[:int(hab[2])]:
                        print("No existe esa habitacion")
                        continue
                    indice=lista_letras.index(hab[1])
                    habitacion=hab[1]+hab[2]  
                    if barcos[barco][tipo_hab][indice][habitacion]== "Ocupada":
                        print(f"{Fore.RED} La habitacion {hab} se encuentra ocupada")
                        print(Fore.LIGHTWHITE_EX)
                        break
                    elif barcos[barco][tipo_hab][indice][habitacion]== " ":
                        print(f"{Fore.GREEN} La habitacion {hab} se encuentra desocupada")
                        print(Fore.LIGHTWHITE_EX)
                        break
            else:
                
                break
        except:
            print("Error")

                    
def num_primo(num):
    for x in range(2,num):
        if num%x==0:
            return False
            
        else:
            return True
            

def abundante(num):
    div=0
    for x in range(1,num):
        if num%x==0:
            div+=x
    if div > num:

        return True
    else:
        return False

def age(barcos,barco,cruzeros,cap_hab,lista_letras,hab_ocu):
    while True:
        try:
            qb=input("""Desea recibir un upgrade de habitacion sin ningun costo? 
            1. Si
            2. No
            >>>""")
            if qb =="1":
                tipo_hab="premium"
                matriz_hab(barcos,barco,tipo_hab)
                hab=pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab,lista_letras,hab_ocu)
                return hab
            else:
                break
            
        except:
            print("error")


def factura(barco,tipo_hab,travelers,lista_dni,cruceros,db):
    lista_hab=[]
    monto=0
    for x in cruceros:
        if barco==x.name:
            precio=x.prize[tipo_hab]
    for x in lista_dni:
        hab=db[str(x)]["hab"]
        lista_hab.append(hab)
        monto+=db[x]["precio"]
    
    

    monto_total=precio*travelers
    monto_con_desc=monto
    impuestos=(monto_total*0.16)
    monto_impu=monto+impuestos

    if monto_total!=monto:
        print(" <<< Factura >>> ")
        for x in lista_dni:
            print(f"""  
    Nombre:{db[x]["Nombre"]} 
    Dni:{x}
    Edad:{db[x]["edad"]}
    Discapaciad:{db[x]["discapacidad"]}""")
        print(f"""
    Habitaciones:{set(lista_hab)}
    Monto total: {monto_total}
    Monto con descuento: {monto_con_desc}
    Impuestos(16%): {impuestos}
    Total: {monto_impu}
    """)
    elif monto_total==monto:
        print(" <<< Factura >>> ")
        for x in lista_dni:
            print(f"""  
    Nombre:{db[x]["Nombre"]} 
    Dni:{x}
    Edad:{db[x]["edad"]}
    Discapaciad:{db[x]["discapacidad"]}""")
        print(f"""
    Habitaciones:{lista_hab}
    Monto total: {monto_total}
    Impuestos(16%): {impuestos}
    Total: {monto_impu}
    """)
    