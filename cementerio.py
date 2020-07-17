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