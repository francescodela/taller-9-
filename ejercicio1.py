class Vehiculo:
    def __init__(self, tipo, marca, modelo, año):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"Vehículo {self.modelo} está encendido.")

    def apagar(self):
        self.encendido = False
        print(f"Vehículo {self.modelo} está apagado.")

    def informacion(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

class Auto(Vehiculo):
    def __init__(self, modelo, marca, año):
        super().__init__('auto', marca, modelo, año)

    def tocar_bocina(self):
        if self.encendido:
            print("¡Pip pip!")
        else:
            print("El auto está apagado.")

class Motocicleta(Vehiculo):
    def __init__(self, gama, marca, modelo, año):
        super().__init__('motocicleta', marca, modelo, año)
        self.gama = gama

    def hacer_caballito(self):
        if self.encendido:
            print("¡Haciendo caballito!")
        else:
            print("La motocicleta está apagada.")

class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def listar_vehiculos(self):
        for vehiculo in self.vehiculos:
            estado = "encendido" if vehiculo.encendido else "apagado"
            print(f"{vehiculo.informacion()}, Estado: {estado}")

flota = Flota()

auto1 = Auto('Modelo M', 'Ford', 2022)
moto1 = Motocicleta(600, 'Yamaha', 'RZ', 2021)
flota.agregar_vehiculo(auto1)
flota.agregar_vehiculo(moto1)
flota.listar_vehiculos()
auto1.encender()
auto1.tocar_bocina()
moto1.encender()
moto1.hacer_caballito()
flota.listar_vehiculos()
