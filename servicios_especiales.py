from servicios import Servicio
from excepciones import ServicioError


class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__("Reserva de Sala")

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50000

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__("Alquiler de Equipos")

        if dias <= 0:
            raise ServicioError("Los días deben ser mayores a 0")

        self.dias = dias

    def calcular_costo(self):
        return self.dias * 80000

    def descripcion(self):
        return f"Alquiler de equipos por {self.dias} días"


class Asesoria(Servicio):

    def __init__(self, sesiones):

        super().__init__("Asesoría Especializada")

        if sesiones <= 0:
            raise ServicioError("Las sesiones deben ser mayores a 0")

        self.sesiones = sesiones

    def calcular_costo(self):
        return self.sesiones * 120000

    def descripcion(self):
        return f"Asesoría con {self.sesiones} sesiones"