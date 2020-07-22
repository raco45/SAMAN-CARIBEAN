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
    """ Esta funcion se encarga de llamar la api en donde se encuentra la informacion de los barcos.

    Returns:
        diccionario: Diccionario que contiene la informacion de los barcos
    """
    url= "https://saman-caribbean.vercel.app/api/cruise-ships"
    response= requests.request("GET",url)
    dic=response.json()
    return dic


def matrixPrinter(matricita,lista_dicc):
    """Esta funcion se encarga de crear la matriz donde se muestran las habitaciones

    Args:
        matricita lista: Lista que contiene la lista donde se enceuntran las habitaciones.
        lista_dicc : lista con informacionde de las habitaciones

    Returns:
        String : Retorna un string en forma de matriz que muestra de color rojo las habitaciones ocupadas y de color verde las descoupadas
    """
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
    """Funcion que imprime  el string generado por la funcion matrixPrinter.

    Args:
        barcos diccionario: contiene la informacion de las habitaciones dividida por barco
        barco string: nombre del barco que solicitado
        tipo_hab string: indica el tipo de habitacion
    """
    matriz=[]
    for x in range(len(barcos[barco][tipo_hab])):
        matriz.append(list(barcos[barco][tipo_hab][x].keys()))

    print(matrixPrinter(matriz,barcos[barco][tipo_hab]))


def mostrar_barcos(cruzeros):
    """Funcion que se encarga de imprimir la informacion de los barcos dependiendo del barco o del destino.

    Args:
        cruzeros lista de objetos: Lista que contiene la clase de cada barco
    """    
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
    """Esta funcion se encarga de pedir el nombre del barco.

    Returns:
        String: Retorna el nombre del barco que se eligio.
    """
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
    """Esta funcion se encarga de imprimir la capacidad por tipo de habitacion dependiendo del barco.

    Args:
        cruzeros lista de objetos: Lista que contiene la clase de cada barco
        barco string: nombre del barco que solicitado
    """
    print("Capacidad por tipo de habitacion: ")
    for crucero in cruzeros:
        if barco==crucero.name:
            for key, value in crucero.room_capacity.items():
                print(f"{key}: {value} personas")

def select_hab():
    """Esta funcion se encarga de pedir al usuario el tipo de habitacion que esta buscando.

    

    Returns:
        String: retorna un string con el tipo de habitacion que se eligio.
    """    
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
    """Esta funcion dependiendo de la cantidad de personas que se ingrese impreme cuantas habitaciones debera comprar.

    Args:
        cruzeros lista de objetos: Lista que contiene la clase de cada barco
        barco string: nombre del barco que solicitado
        tipo_hab string: tipo de habitacion solicidata
        travelers int: cantidad de personas ingresadas

    Returns:
        int: retorna la capacidad de la habitacion solicitada
    """
    for x in cruzeros:
        if x.name == barco:
            if travelers > x.room_capacity[tipo_hab]:
                print("Debera comprar 2 o mas habitaciones")
                return x.room_capacity[tipo_hab]
            elif travelers <= x.room_capacity[tipo_hab]:
                print("Debara comprar 1 habitacion")
                return x.room_capacity[tipo_hab]
                

def formulario(dni_1,hab,tipo_hab,db,barcos,barco,cruceros):
    """Esta funcion se encarga de pedir los datos al usurio y verificar si cumple las condiciones para otorgarle un descuento; 
       y guardar toda esta informacion en un diccionario.

    Args:
        dni_1 int: dni de la persona
        hab string: string con el nombre de la habitacion
        tipo_hab string: tipo de habitacion solicidata
        db diccionario: Contiene la informacion de los pasajeros
        barcos diccionario: contiene la informacion de las habitaciones dividida por barco
        barco string: nombre del barco que solicitado
        cruceros lista de objetos: Lista que contiene la clase de cada barco
        

    Returns:
        string: Retorna la palabra exitoso """
    while True:
        try:
            
            new_user={}
            new_user["Nombre"]=nombre()
            new_user["barco"]=barco
            new_user["tipo hab"]=tipo_hab
            new_user["edad"]=edad()
            
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
    """Esta funcion se encargad e pedir al usuario la habitacion que desea ocupar>

    Args:
        barcos diccionario: contiene la informacion de las habitaciones dividida por barco
        barco string: nombre del barco que solicitado
        tipo_hab string: tipo de habitacion solicidata
        cruzeros lista de objetos: Lista que contiene la clase de cada barco
        cap_hab int: capacidad del tipo de habitacion
        lista_letras list: contiene todas las letras del abecedario en mayusculo.
        hab_ocu lista: que contiene el objeto habitacion
        

    Returns:
        string: retorna un string con el la inicial del tipo de habitacion, la letra del pasillo y el numero de la habitacion.
    """

    
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
    """Esta funcion recursiva se encarga de pedir al usuario su dni y de pedir al usuario sus datos mediante la funcion formulario, 
       segun la cantidad de travelers que se ingrese

    Args:
        travelers int: cantidad de personas ingresadas.
        cap_hab int: capacidad del tipo de habitacion.
        barcos diccionario: contiene la informacion de las habitaciones dividida por barco.
        barco string: nombre del barco que solicitado.
        tipo_hab string: tipo de habitacion solicidata.
        cruzeros lista de objetos: Lista que contiene la clase de cada barco.
        db diccionario: Contiene la informacion de los pasajeros.
        lista_letras list: contiene todas las letras del abecedario en mayusculo.
        hab_ocu lista: que contiene el objeto habitacion.
        lista_dni lista: lista en donde se guarda el dni de los pasajeros segun van ingresando.

    Returns:
        lista: Retorna la lista donde se guarda el dni de los pasajeros segun van ingresando.
    """
    while True:
        precio=0
        
        if travelers > cap_hab:
            
            cont_1=0
            
            
            hab=pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab,lista_letras,hab_ocu)
            
            while cont_1 < cap_hab:
                dni_1=dni()
                print(formulario(dni_1,hab,tipo_hab,db,barcos,barco,cruzeros))
                cont_1+=1
                lista_dni.append(dni_1)
            return pedir_formu(travelers-cap_hab,cap_hab,barcos,barco,tipo_hab,cruzeros,db,lista_letras,hab_ocu,lista_dni)
        elif travelers <=cap_hab:
            cont=0
            
            hab=pedir_habitacion(barcos,barco,tipo_hab,cruzeros,cap_hab,lista_letras,hab_ocu)
            
            while cont < travelers:
                dni_1=dni()
                print(formulario(dni_1,hab,tipo_hab,db,barcos,barco,cruzeros))
                cont+=1
                lista_dni.append(dni_1)
            return  lista_dni


def nombre():
    """ Esta funcion se encarga de pedir el nombre completo del usuario.
    
    Returns:
        String -- Nombre completo ingresedo por el usuario.
    """
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
    """Esta funcion se encarga de pedir al usuario el numero de su documento de indentidad.

    Returns:
        string: numero del dni
    """
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
    """Esta funcion se encarga de pedir la edad al usuario.
    
    Returns:
        String -- Edad ingresada por el usuario.
    """
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
    """Esta funcion se encarga de preguntar al usuario si sufre de alguna discapacidad.

    Returns:
        bool: retorna True en caso de ser cierto y False en caso de no serlo.
    """    
            
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
    """Esta funcion se encarga de desocupar una habitacion de uno de los tripulantes del barco.

    Args:
        db diccionario: Contiene la informacion de los pasajeros.
        barcos diccionario: contiene la informacion de las habitaciones dividida por barco.
        lista_letras list: contiene todas las letras del abecedario en mayusculo.
    """
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
    """Esta funcion se encarga de buscar y verificar la disponibilidad de una o varias habitaciones, 
       se puede realizar la busqueda por tipo, por capacidad o por nombre de la habitacion.

    Args:
        barcos diccionario: contiene la informacion de las habitaciones dividida por barco.
        cruceros lista de objetos: Lista que contiene la clase de cada barco.
        lista_letras list: contiene todas las letras del abecedario en mayusculo.
    """    
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
    """Esta funcion se encarga de verificar si un numero es primo.

    Args:
        num (int): Numero a verificar.

    Returns:
        bool: Retorna true si cumple la condicion y false si no la cumple
    """
    for x in range(2,num):
        if num%x==0:
            return False
            
        else:
            return True
            

def abundante(num):
    """ Esta funcion se encarga de verificar si un numero es abundante.

    Args:
        num (int): Numero a verificar.

    Returns:
        bool: Retorna true si cumple la condicion y false si no la cumple.
    """
    div=0
    for x in range(1,num):
        if num%x==0:
            div+=x
    if div > num:

        return True
    else:
        return False



def factura(barco,tipo_hab,travelers,lista_dni,cruceros,db):
    """Esta funcion se encarga de generar e imprimir la factura del usuario .

    Args:
        barco string: nombre del barco que solicitado.
        tipo_hab string: tipo de habitacion solicidata.
        travelers int: cantidad de personas ingresadas.
        lista_dni lista: lista en donde se guarda el dni de los pasajeros segun van ingresando.
        cruceros lista de objetos: Lista que contiene la clase de cada barco.
        db diccionario: Contiene la informacion de los pasajeros.
    """    
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
    

#modulo 3 

def tour_puerto(d_ni,cupos_tours):
    """Esta funcion se encarga de reservar cupos para el tour por el puerto y en caso de que los cupos se acaben imprime un mensaje
       de aviso; otorga un descuento del 10% al tercer y al cuarto comprador.

    Args:
        d_ni (int): el dni de la persona que va a comprar
        cupos_tours (diccionario): diccionario que contiene la informacion de los tours
    """    
    lista_compradores=[]
    precio=30
    for key,x in cupos_tours["Tour en el puerto"].items():
        lista_compradores.append(x)
    lista_compradores.append(d_ni)
    indice=lista_compradores.index(d_ni)
    if indice==3 or indice==4:
        desc=precio*0.1
    else:
        desc=0
    if lista_compradores[0]==0:
        print("se acabaron los cupos")
    else:
        while True:
            try:
                personas=input("indique la cantidad de personas (max 4 personas): ")
                if int(personas)<=lista_compradores[0]:
                    if int(personas)>4:
                        print("No puede llevar a mas de 4 personas")
                        continue
                    else:
                        cupos_tours["Tour en el puerto"][d_ni]=f" cupos:{personas} "
                        cupos=cupos_tours["Tour en el puerto"]["cupos"]
                        cupos_tours["Tour en el puerto"]["cupos"]=cupos-int(personas)
                        monto=precio-desc
                        monto_final=monto*int(personas)
                        if desc!=0:
                            print(f""" Resumen de compra 
                            Actividad: Tour en el puerto
                            Hora: 7:00 am
                            Costo de la entrada: ${precio}
                            Personas:{personas}
                            Monto total(10% descuento):${monto_final} 
                            """)
                        else:
                            print(f""" Resumen de compra 
                            Actividad: Tour en el puerto
                            Hora: 7:00 am
                            Costo de la entrada: ${precio}
                            Personas:{personas}
                            Monto total:${monto_final} 
                            """)
                            break
                else:
                    print(f"Quedan {lista_compradores[0]} cupos ")
                    break
            except:
                print("error")

def desgutacion(d_ni,cupos_tours):
    """Esta funcion se encarga de reservar cupos para la desgustacion de comida local y en caso de que los cupos se acaben imprime un mensaje
       de aviso.

    Args:
        d_ni (int): el dni de la persona que va a comprar
        cupos_tours (diccionario): diccionario que contiene la informacion de los tours
    """    
    lista_compradores=[]
    precio=100
    for key,x in cupos_tours["Degustacion de comida"].items():
        lista_compradores.append(x)
    lista_compradores.append(d_ni)
    if lista_compradores[0]==0:
        print("se acabaron los cupos")
    else:
        while True:
            try:
                personas=input("indique la cantidad de personas (max 2 personas): ")
                if int(personas)<lista_compradores[0]:
                    if int(personas)>2:
                        print("No puede llevar a mas de 2 personas")
                        continue
                    else:
                        cupos_tours["Degustacion de comida"][d_ni]=f" cupos:{personas} "
                        cupos=cupos_tours["Degustacion de comida"]["cupos"]
                        cupos_tours["Degustacion de comida"]["cupos"]=cupos-int(personas)
                        monto=precio
                        monto_final=monto*int(personas)
                        print(f""" Resumen de compra 
                        Actividad: Degustación de comida local
                        Hora: 12:00 pm
                        Costo de la entrada: ${precio}
                        Personas:{personas}
                        Monto total:${monto_final} 
                        """)
                else:
                    print(f"Quedan {lista_compradores[0]} cupos ")
                    break
            except:
                print("error")
                        
def Trotar_pueblo(d_ni,cupos_tours): 
    """Esta funcion ter permite anotarte para ir a trotar por el pueblo o ciudad, sus cupos son ilimitados.

    Args:
        Esta funcion se encarga de reservar cupos para el tour por el puerto y en caso de que los cupos se acaben imprime un mensaje
       de aviso.
    """    
    while True:
            try:
                personas=input("indique la cantidad de personas (No hay limite): ")
        
                cupos_tours["Trotar por el pueblo"][d_ni]=f" cupos:{personas} "
                
                
                print(f""" Resumen de compra 
                Actividad: trotar por el pueblo/ciudad
                Hora: 6:00 am
                Personas:{personas}
                """)
                break
                
            except:
                print("error")
                break     

def lugares_historicos(d_ni,cupos_tours):
    """Esta funcion se encarga de reservar cupos para el tour por lugares historicos y en caso de que los cupos se acaben imprime un mensaje
       de aviso; otorga un descuento del 10% del tercer comprador en adelante.

    Args:
        Esta funcion se encarga de reservar cupos para el tour por el puerto y en caso de que los cupos se acaben imprime un mensaje
       de aviso.
    """    
    lista_compradores=[]
    precio=40
    for key,x in cupos_tours["Visita a lugares historicos"].items():
        lista_compradores.append(x)
    lista_compradores.append(d_ni)
    indice=lista_compradores.index(d_ni)
    if indice>=3 :
        desc=precio*0.1
    else:
        desc=0
    if lista_compradores[0]==0:
        print("se acabaron los cupos")
    else:
        while True:
            try:
                personas=input("indique la cantidad de personas (max 4 personas): ")
                if int(personas)<=lista_compradores[0]:
                    if int(personas)>4:
                        print("No puede llevar a mas de 4 personas")
                        continue
                    else:
                        cupos_tours["Visita a lugares historicos"][d_ni]=f" cupos:{personas} "
                        cupos=cupos_tours["Visita a lugares historicos"]["cupos"]
                        cupos_tours["Visita a lugares historicos"]["cupos"]=cupos-int(personas)
                        monto=precio-desc
                        monto_final=monto*int(personas)
                        if desc!=0:
                            print(f""" Resumen de compra 
                            Actividad: Visita a lugares historicos
                            Hora: 10:00 am
                            Costo de la entrada: ${precio}
                            Personas:{personas}
                            Monto total(10% descuento):${monto_final} 
                            """)
                        else:
                            print(f""" Resumen de compra 
                            Actividad: Visita a lugares historicos
                            Hora: 10:00 am
                            Costo de la entrada: ${precio}
                            Personas:{personas}
                            Monto total:${monto_final} 
                            """)
                            break
                else:
                    print(f"Quedan {lista_compradores[0]} cupos ")
                    break
            except:
                print("error")                 

#modulo 4
def restaurante(menu,barco):
    """Esta funcion se encarga de administrar las acciones que se pueden realizar para gestionar el menu del restaurante de cada barco.

    Args:
        menu (lista): Lista que contiene la informacion del menu de cada restaurante
        barco (string): String del nombre del barco que estamos gestionando
    """    
    while True:
        try:
            inter=input("""Bienvenido a la gestion de restaurantes
            1.Agregar Platos al menu
            2.Eliminar productos del menu
            3.Modificar producto
            4.Agregar combos al menu de combos
            5.Eliminar combo
            6.Buscar productos por nombre o rango de precio
            7.Buscar combos por nombre o rango de precio
            8.Salir
            >>>>""")
            if inter=="1":
               agregar_producto(menu,barco)
               continue
            elif inter=="2":
                eliminar_producto(menu,barco)
                
                continue
            elif inter=="3":
                modificar(menu,barco)
                continue
            elif inter=="4":
                agregar_combo(menu,barco)
                continue
            elif inter=="5":
                eliminar_combo(menu,barco)
                continue
            elif inter=="6":
                buscar_productos(menu,barco)
            elif inter=="7":
                buscar(menu,barco,tipo_producto="Combos")
            else:
                break
        except:
            print("error")
    
def agregar_producto(menu,barco):
    """Esta funcion se encarga de agregar productos al menu del crucero dividiendolos en bebidas o alimento.

    Args:
        menu (lista): Lista que contiene la informacion del menu de cada restaurante
        barco (string): String del nombre del barco que estamos gestionando

    

    Returns:
        [lista]:  Lista que contiene la informacion del menu de cada restaurante
    """    
    while True:
        try:
            tipo=input("""Indique si es 
                1.alimento 
                2.bebida 
                >>>""")
            nombre_pro=input("indique el nombre del producto: ").lower()
            if not nombre_pro.isalpha():
                print("No valido")
                continue
            if tipo=="1":
                menu[barco]["alimentos"][nombre_pro]={}
                alimento=input("""Indique si es 
                1.Empaque
                2.Preparacion
                >>>""")
                if alimento=="1":
                    
                    menu[barco]["alimentos"][nombre_pro]["tipo"]="empaque"
                    
                elif alimento=="2":
                    menu[barco]["alimentos"][nombre_pro]["tipo"]="preparacion"
                   
                else:
                    print("No tenemos tantas opciones")
                    raise Exception
                while True:
                    precio=input("Ingrese el nuevo precio: ")
                    if precio.isalpha():
                        continue
                    precio_def=float(precio)+(float(precio)*0.16)
                    menu[barco]["alimentos"][nombre_pro]["precio"]=precio_def
                    break
                print("Se guardo el producto con exito")        
                return menu
                    
            elif tipo=="2":
                menu[barco]["bebidas"][nombre_pro]={}
                bebida=input("""Indique el tamaño de la bebida
                1.Pequeño
                2.Mediana
                3.Grande 
                >>""")
                if bebida=="1":
                    menu[barco]["bebidas"][nombre_pro]["tamaño"]="Pequeño"
                    
                elif bebida=="2":
                    menu[barco]["bebidas"][nombre_pro]["tamaño"]="Mediana"
                    
                elif bebida=="3":
                    menu[barco]["bebidas"][nombre_pro]["tamaño"]="Grande"
                    
                else:
                    print("No tenemos ese tamaño")
                    raise Exception
                while True:
                    precio=input("Ingrese el nuevo precio: ")
                    if precio.isalpha():
                        continue
                    precio_def=float(precio)+(float(precio)*0.16)
                    menu[barco]["bebidas"][nombre_pro]["precio"]=precio_def
                    break
                print("Se guardo el producto con exito")        
                return menu
            else:
                raise Exception
        except:
            print("Error")

def eliminar_producto(menu,barco):
    """Esta funcion se encarga de eliminar un producto del menu del crucero.

    Args:
        menu (lista): Lista que contiene la informacion del menu de cada restaurante
        barco (string): String del nombre del barco que estamos gestionando

    
    """    
    while True:
        try:
            tipo=input("""Indique si es 
                1.alimento 
                2.bebida 
                >>>""")
            if tipo=="1":
                lista_productos=[]
                print("Alimentos")
                for x in menu[barco]["alimentos"]:
                    lista_productos.append(x)
                    print(x)
                nombre_pro=input("Escriba el nombre del producto que desea eliminar ").lower()
                if nombre_pro in lista_productos:
                    menu[barco]["alimentos"].pop(nombre_pro)
                    print("Se elimino el producto con exito")
                    break
                else:
                    print("No se encontro el producto")
                    raise Exception
            elif tipo=="2":
                lista_productos=[]
                print("Bebidas")
                for x in menu[barco]["bebidas"]:
                    lista_productos.append(x)
                    print(x)

                nombre_pro=input("Escriba el nombre del producto que desea eliminar ").lower()
                if nombre_pro in lista_productos:
                    menu[barco]["bebidas"].pop(nombre_pro)
                    print("Se elimino el producto con exito")
                    break
                else:
                    print("No se encontro el producto")
                    raise Exception
            else:
                print("No exite")
                raise Exception
        except:
            print("error")

def modificar(menu,barco):
    """Esta funcion se encarga de modificar la informacion de uno o varios productos del menu del crucero.

    Args:
        menu (lista): Lista que contiene la informacion del menu de cada restaurante
        barco (string): String del nombre del barco que estamos gestionando

    
    """    
    while True:
        try:
            tipo=input("""Indique si es 
                1.alimento 
                2.bebida 
                >>>""")
            nombre_pro=input("indique el nombre del producto: ").lower()
            lista_productos=[]
            if not nombre_pro.isalpha():
                print("No valido")
                continue
            if tipo=="1":
                for x in menu[barco]["alimentos"]:
                    lista_productos.append(x)
                if nombre_pro not in lista_productos:
                    print("No se encuentra en el menu")
                    raise Exception
                change=input("""Desea cambiar 
                1.Tipo
                2.Precio
                >>""")
                if change=="1":
                    alimento=input("""Indique si es 
                1.Empaque
                2.Preparacion
                >>>""")
                    if alimento=="1":
                        menu[barco]["alimentos"][nombre_pro]["tipo"]="empaque"
                    elif alimento=="2":
                        menu[barco]["alimentos"][nombre_pro]["tipo"]="preparacion"
                    else:
                        print("No tenemos tantas opciones")
                        raise Exception
                    print("cambio exitoso")
                    break
                elif change=="2":
                    while True:
                        precio=input("Ingrese el nuevo precio: ")
                        if precio.isalpha():
                            continue
                        precio_def=float(precio)+(float(precio)*0.16)
                        menu[barco]["alimentos"][nombre_pro]["precio"]=precio_def
                        break
                
                    print("Se realizo el cambio con exito")
                    break
                else:
                    raise Exception
            elif tipo=="2":
                for x in menu[barco]["bebidas"]:
                    lista_productos.append(x)
                if nombre_pro not in lista_productos:
                    print("No se encuentra en el menu")
                    raise Exception
                change=input("""Desea cambiar 
                1.Tamaño
                2.Precio
                >>""")
                if change=="1":
                    bebida=input("""Indique el tamaño de la bebida
                1.Pequeño
                2.Mediana
                3.Grande 
                >>""")
                    if bebida=="1":
                        menu[barco]["bebidas"][nombre_pro]["tamaño"]="Pequeño"
                        
                    elif bebida=="2":
                        menu[barco]["bebidas"][nombre_pro]["tamaño"]="Mediana"
                        
                    elif bebida=="3":
                        menu[barco]["bebidas"][nombre_pro]["tamaño"]="Grande"
                    else:
                        raise Exception
                elif change=="2":
                    while True:
                        precio=input("Ingrese el nuevo precio: ")
                        if precio.isalpha():
                            continue
                        precio_def=float(precio)+(float(precio)*0.16)
                        menu[barco]["bebidas"][nombre_pro]["precio"]=precio_def
                        break
                    print("Se realizo el cambio con exito")
                    break
                else:
                    raise Exception
            else:
                print("No exite")
                raise Exception
        except:
            print("error")


def agregar_combo(menu,barco):
    """Esta funcion se encarga de crear y agrar un combo al menu del crucero.

    Args:
        menu (lista): Lista que contiene la informacion del menu de cada restaurante
        barco (string): String del nombre del barco que estamos gestionando
    """    
    
    while True:
        try:
            combo=input("Ingrese el nombre del combo: ").lower()
            
            productos=[]
            cont=0
            while True:
                seguir=True
                products=input("Ingrese el nombre del producto que desea tener en el combo: ").lower()
                cont+=1
                productos.append(products)
                if cont>=2:
                    while True:
                        ask=input("""Desea agregar mas productos al combo?: 
                        1.Si
                        2.No
                        >>""")
                        if ask=="1":
                            seguir=True
                            break
                        elif ask=="2":
                            seguir=False
                            break
                        else:
                            continue
                if seguir:
                    continue
                elif seguir==False:
                    break
            menu[barco]["Combos"][combo]={}
            menu[barco]["Combos"][combo]["productos"]=productos
            while True:
                precio=input("Ingrese el nuevo precio: ")
                if precio.isalpha():
                    continue
                precio_def=float(precio)+(float(precio)*0.16)
                menu[barco]["Combos"][combo]["precio"]=precio_def 
                break
            print("Exitoso")
            break
        except:
            print("error")
def eliminar_combo(menu,barco):
    """Esta funcion se encarga de eliminar un combo del menu del crucero.

    Args:
        menu (lista): Lista que contiene la informacion del menu de cada restaurante
        barco (string): String del nombre del barco que estamos gestionando

    
    """    
    while True:
        try:
            lista_productos=[]
            print("Combos")
            for x in menu[barco]["Combos"]:
                lista_productos.append(x)
                print(x)
                
            nombre_pro=input("Escriba el nombre del combo que desea eliminar: ").lower()
            if nombre_pro in lista_productos:
                menu[barco]["Combos"].pop(nombre_pro)
                print("Se elimino con exito el combo")
                break
            else:
                print("No se encontro el producto")
                raise Exception
        except:
            print("error")

def buscar_productos(menu,barco):
    """Esta funcion se encarga de llamar a la funcion buscar dependiendo del tipo de producto que se quiera buscar.

    Args:
        menu (lista): Lista que contiene la informacion del menu de cada restaurante
        barco (string): String del nombre del barco que estamos gestionando
    """    
    while True:
        try:
            tipo=input("""Indique si es 
                1.alimento 
                2.bebida 
                >>>""")
            if tipo=="1":
                tipo_producto= "alimentos"
                buscar(menu,barco,tipo_producto)
                break
            elif tipo=="2":
                tipo_producto="bebidas"
                buscar(menu,barco,tipo_producto)
                break
            else:
                continue
        except:
            print("error")



def buscar(menu,barco,tipo_producto):
    """Esta funcion se encarga de buscar productos o combos dependiendo del precio o nombre del producto.

    Args:
        menu (lista): Lista que contiene la informacion del menu de cada restaurante
        barco (string): String del nombre del barco que estamos gestionando
        tipo_producto (string): string que indica si el tipo de producto o combo.

    
    """    
    while True:
        try:
            search=input(""" Desea buscar por nombre o precio 
            1.Nombre
            2.Precio
            >>>""")

            if search=="1":
                ali=input("Ingrese el nombre de lo que desea buscar: ").lower()
                lista_pro=[]
                for x in menu[barco][tipo_producto]:
                    lista_pro.append(x)
                if ali in lista_pro:
                    for key, value in menu[barco][tipo_producto][ali].items():
                        if key=="precio":
                            print(f"{key}: ${value}")
                    break
                elif ali not in lista_pro:
                    print("No se encuentra ese producto")
                    continue
            elif search=="2":
                rango=input("""Indique el rango de precio 
                1. Entre $1 y $50
                2. Entre $50 y $100
                3. Entre $100 y $200 
                >>> """)
                if rango=="1":
                    for x in menu[barco][tipo_producto]:
                        precios=menu[barco][tipo_producto][x]["precio"]
                        if precios>0 and precios<50:
                            print(f"{x} precio: ${precios}")
                elif rango=="2":
                    for x in menu[barco][tipo_producto]:
                        precios=menu[barco][tipo_producto][x]["precio"]
                        if precios>50 and precios<100:
                            print(f"{x} precio: ${precios}")
                elif rango=="3":
                    for x in menu[barco][tipo_producto]:
                        precios=menu[barco][tipo_producto][x]["precio"]
                        if precios>100 and precios<200:
                            print(f"{x} precio: ${precios}")
                else:
                    continue      
            else:
                raise Exception  
            break
        except:
            print("error")

