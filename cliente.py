from excepciones import ClienteError


class Cliente:

    def __init__(self, nombre, edad):

        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        if not isinstance(edad, int):
            raise ClienteError("La edad debe ser numérica")

        if edad < 18:
            raise ClienteError("El cliente debe ser mayor de edad")

        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def mostrar_datos(self):
        return f"Cliente: {self.__nombre} - Edad: {self.__edad}"

    def __str__(self):
        return self.mostrar_datos()