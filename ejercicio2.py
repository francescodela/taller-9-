class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero  
        self.tipo = tipo      
        self.ocupada = False  

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            return True
        return False

    def esta_ocupada(self):
        return self.ocupada

    def info(self):
        estado = "Ocupada" if self.esta_ocupada() else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}): {estado}"


class Hotel:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, numero, tipo):
        habitacion = Habitacion(numero, tipo)
        self.habitaciones.append(habitacion)

    def reservar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if habitacion.reservar():
                    print(f"Habitación {numero} reservada con éxito.")
                    return
                else:
                    print(f" la habitación {numero} ya está ocupada.")
                    return
        print(f"la habitación {numero} no encontrada.")

    def liberar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if habitacion.liberar():
                    print(f"Habitación {numero} liberada con éxito.")
                    return
                else:
                    print(f"Habitación {numero} no estaba ocupada.")
                    return
        print(f"Habitación {numero} no encontrada.")

    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            print(habitacion.info())



hotel = Hotel()
hotel.agregar_habitacion(101, "Individual")
hotel.agregar_habitacion(102, "Doble")
hotel.agregar_habitacion(103, "Individual")
hotel.mostrar_habitaciones()
hotel.reservar_habitacion(101)
hotel.mostrar_habitaciones()
hotel.liberar_habitacion(101)
hotel.mostrar_habitaciones()
