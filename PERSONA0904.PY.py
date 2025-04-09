class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

if __name__ == "__main__":
    oPersona1= Persona ("Luis", "Perez", edad=20)
    print(oPersona1._nombre)
    print(oPersona1._apellido)
    print(oPersona1._edad)