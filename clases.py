import colorama
from colorama import Fore,Style, Back
#modulo 1 
class Cruise:
    def __init__(self,name,route,departure_date,prize,floors_info,room_capacity):

        self.name=name
        self.route=route
        self.departure_date=departure_date
        self.prize=prize
        self.floors_info=floors_info
        self.room_capacity=room_capacity



    def show_info(self):
        """Esten metodo imprime la informacion del crucero.
        """        
        color= Fore.WHITE
        print(f""" {color}      
Nombre: {self.name} 
Ruta: {self.route }
Fecha de salida: {self.departure_date}""")
        print("<"*8, ">"*8)
        print("El precio por habitacion es:")
        for key, value in self.prize.items():
            color_value= (Fore.GREEN + str(value))
            color_key= Fore.WHITE + "Habitacion" + " " + key
            print(f"""  {color_key} : {color_value}$ """)
        
        print(Fore.WHITE + "<"*8, ">"*8)
        for floor, info in self.floors_info.items():
            piso=(Fore.WHITE + floor)
            print(f" {piso}:{info} ")
            
                
        print("<"*8, ">"*8)
        print("Capacidad por tipo de habitacion: ")
        for key, value in self.room_capacity.items():
            print(f"Habitacion {key}: {value} personas ","\t")
        return ""

#modulo 2 

class Room:
    def __init__(self,letra,numero,capacidad,referencia):

        self.letra=letra
        self.numero=numero
        self.capacidad=capacidad
        self.referencia=referencia

class Sencilla(Room):
    def __init__(self, letra, numero, capacidad, referencia):
        super().__init__(letra, numero, capacidad, referencia)

        def room_service(self):
            print("Servicio a la habitacion")

class Premium(Room):
    def __init__(self, letra, numero, capacidad, referencia):
        super().__init__(letra, numero, capacidad, referencia)

        def sea_view(self):
            print("Tiene vista al mar")

class Vip(Room):
    def __init__(self, letra, numero, capacidad, referencia):
        super().__init__(letra, numero, capacidad, referencia)

        def private_partys(self):
            print("Puede hacer fiestas privadas")

class Traveler:
    def __init__(self,nombre,dni,edad,discapacidad,tipo_hab,habitacion,status):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        self.discapacidad=discapacidad
        self.tipo_hab=tipo_hab
        self.habitacion=habitacion
        self.status=status
    def change_stauts(self):
        self.status="off"