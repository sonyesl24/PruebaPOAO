class Vehiculo:
    def __init__(self, color, modelo, placa, valor, cilindraje, anio, tipo_puertas,
                 combustible, kilometraje, caja_cambios, seguro, gama, chasis,
                 pais_origen, marca, llanta_emergencia, numero_puertas):
        self.color = color
        self.modelo = modelo
        self.placa = placa
        self.valor = valor
        self.cilindraje = cilindraje
        self.anio = anio
        self.tipo_puertas = tipo_puertas
        self.combustible = combustible
        self.kilometraje = kilometraje
        self.caja_cambios = caja_cambios
        self.seguro = seguro
        self.gama = gama
        self.chasis = chasis
        self.pais_origen = pais_origen
        self.marca = marca
        self.llanta_emergencia = llanta_emergencia
        self.numero_puertas = numero_puertas

if __name__ == "__main__":
    oVehiculo1 = Vehiculo(
        color="Negro",
        modelo="2023",
        placa="XYZ-987",
        valor=25000,
        cilindraje=1800,
        anio=2023,
        tipo_puertas="SUV",
        combustible="Gasolina",
        kilometraje=5000,
        caja_cambios="Automática",
        seguro="Sí",
        gama="Alta",
        chasis="CHS45678",
        pais_origen="Alemania",
        marca="BMW",
        llanta_emergencia=True,
        numero_puertas=5
    )

    print(f"""
    Vehículo:
    Color: {oVehiculo1.color}
    Modelo: {oVehiculo1.modelo}
    Placa: {oVehiculo1.placa}
    Valor: ${oVehiculo1.valor}
    Cilindraje: {oVehiculo1.cilindraje} cc
    Año: {oVehiculo1.anio}
    Tipo de puertas: {oVehiculo1.tipo_puertas}
    Combustible: {oVehiculo1.combustible}
    Kilometraje: {oVehiculo1.kilometraje} km
    Caja de cambios: {oVehiculo1.caja_cambios}
    Seguro: {oVehiculo1.seguro}
    Gama: {oVehiculo1.gama}
    Chasis: {oVehiculo1.chasis}
    País de origen: {oVehiculo1.pais_origen}
    Marca: {oVehiculo1.marca}
    Llanta de emergencia: {"Sí" if oVehiculo1.llanta_emergencia else "No"}
    Número de puertas: {oVehiculo1.numero_puertas}
    """)
