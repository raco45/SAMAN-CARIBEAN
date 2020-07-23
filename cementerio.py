#Si de casualidad entro aqui profesor, este es cementerio de codigo en el que fui guardando pedazos de codigo que no utilice o
# que no me sirvio o que utlice para algunas pruebas.
#en cualquier caso aprovecho para agradecerle tanto a usted como al profesor luis por la manera en la que nos dieron esta materia y que apesar de la virtualidad
#supieron hacerla muy dinamica y activa, en mi caso me mantuvieron muy activo programando casi todos los dias y eso, creo que yo, que es 
# la clave para aprender a programar.
# si nada mas que agregar espero que le haya gustado mi codigo.
#pd: la ultima tarea no la entregue porque no me llego el correo de replit.
#Hasta la proxima. 



from string import ascii_letters
from string import ascii_uppercase
#from clasesM1 import Cruise
lista_letras=list(ascii_uppercase)
lista=["simple","premium","vip"]
barcos={

}
# name=["rompe","hola","mar","poseidon"]
# pisos=[]

# new={}
# pasillos=4
# hab_x_pas=10
# for x in range(pasillos):
#     new_hall={}
#     for y in range(hab_x_pas):
#         hab=lista_letras[x] + str(y+1)
#         new_hall[hab]=" "
#     pisos.append(new_hall)

# for x in lista:
#     new[x]=pisos

# for x in name:
#     barcos[x]=new


#print(pisos)
        
    


# print(barcos)

# lista_letras=list(ascii_uppercase)
# lista=["simple","premium","vip"]
# def crear_estructura(crucero,lista,lista_letras):
#     barcos={
# }
#     nombres=[]
#     for x in crucero:
#         nombres.append(x.name)
#         for nombre in nombres:
#             for tipo in lista:
#                 lista_letras=list(ascii_uppercase)
#                 pisos=[]
#                 pasillos=x.floors_info[tipo][0]
#                 hab_x_pas=x.floors_info[tipo][1]
#                 for w in range(pasillos):
#                     new_hall={}
#                     for y in range(hab_x_pas):
#                         hab=lista_letras[w] + str(y+1)
#                         new_hall[hab]=" "
#                     pisos.append(new_hall)
#                 #print(pisos)
#                 new={}
#                 new[tipo]=pisos
#             barcos[nombre]=new

#     return barcos
# lista_letras=list(ascii_uppercase)
# lista=["simple","premium","vip"]
# def crear_estructura(crucero,lista,lista_letras):
#     barcos={
#     }
#     nombres=[]
#     lista_letras=list(ascii_uppercase)
#     pisos=[]

#     new={}
#     for x in crucero:
#         for key, value in x.floors_info.items():
#                 pasillos=x.floors_info
#                 hab_x_pas=x.floors_info
#                 for x in range(pasillos[key][0]):
#                     new_hall={}
#                     for y in range(hab_x_pas[key][1]):
#                         hab=lista_letras[x] + str(y+1)
#                         new_hall[hab]=" "
#                     pisos.append(new_hall)

#     for x in lista:
#         new[x]=pisos

#     for x in crucero:
#         barcos[x.name]=new
#     return barcos


#     with open("habitaciones.txt", "r") as archivo:
#         dict_text=archivo.read()
#         barcos=json.dumps(dict_text)

       
    



#     with open("nombre_2.txt","r",encoding="utf-8") as archivo:
#         archivo.read(json.loads(str(barcos),ensure_ascii=False))
    
#     try:
#         with open("texto.txt","r") as base_datos: 
#                 for fila in base_datos: 
#                         cuenta= (fila.strip()).split(",")
#                         user_temp=Cruise(cuenta[0],cuenta[1],cuenta[2],cuenta[3],cuenta[4],cuenta[5])
#                         creuceros.append(user_temp)
#     except:


with open("nombre_2.txt","w",encoding="utf-8") as archivo:
        archivo.write(json.dumps(barcos,ensure_ascii=False))
#     archivo=open("habitaciones.txt", "w")
#     barquitod=str(barcos)
#     archivo.write(barquitod)
#     archivo.close()

    # formulario("A2",db)
    # print(db)

with open("texto.txt","w") as base_datos:                                    #se abre el archivo texto.txt para poder escribir los nuevos datos del que el usuario desea guardar.  
            for user_temp in creuceros:
                big_string="{},{},{},{},{},{}\n".format(user_temp.name,user_temp.route,user_temp.departure_date,user_temp.prize,user_temp.floors_info,user_temp.room_capacity)
                base_datos.write(big_string)

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


while True:
        try:
            print("Elija un barco")
            dic=api()
            for i, barco in enumerate(dic):
                print(f"{i+1} {dic[i]['name']} ")
            option=int(input("Ingrese el barco "))
            ship_selected=dic[option-1]["sells"]
            
            for i, lista in enumerate(ship_selected):
                print(f"{i+1} {ship_selected[i]['name']}")
            selec=int(input(">>"))
            print(ship_selected[selec-1]["price"])
        #     for i , barco in enumerate(dic):
        #         ventas.append(dic[i]["sells"])
        # #print(ventas)     
        # # for key,x in ventas.items():
        # #         print(x[0]["name"])
        # #print(ventas["El Dios de los Mares"])    
        #     for x in range(len(ventas)):
        #         print(ventas[x])
        #         for y in ventas[x]:
        #                 print(y["name"])               
            #return ship_selected["name"]
            
            
        except:
            print("Ese barco no se encuentra disponible")