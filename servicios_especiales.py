from servicios import Servicio
from excepciones import ServicioError


class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__("Reserva de Sala")

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        self.horas = horas

    def calcular_costo(self, impuesto=0, descuento=0):
        costo_base = self.horas * 50000
        costo_final = costo_base * (1 + impuesto / 100)
        costo_final -= costo_final * (descuento / 100)
        return costo_final

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"

    def get_horas(self):
        """Obtiene la cantidad de horas de la sala"""
        return self.horas

    def get_duracion_base(self):
        """Obtiene la duración base del servicio"""
        return self.horas


class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__("Alquiler de Equipos")

        if dias <= 0:
            raise ServicioError("Los días deben ser mayores a 0")

        self.dias = dias

    def calcular_costo(self, impuesto=0, descuento=0):
        costo_base = self.dias * 80000
        costo_final = costo_base * (1 + impuesto / 100)
        costo_final -= costo_final * (descuento / 100)
        return costo_final

    def descripcion(self):
        return f"Alquiler de equipos por {self.dias} días"

    def get_dias(self):
        """Obtiene la cantidad de días para alquilar equipos"""
        return self.dias

    def get_duracion_base(self):
        """Obtiene la duración base del servicio"""
        return self.dias


class Asesoria(Servicio):

    def __init__(self, sesiones):

        super().__init__("Asesoría Especializada")

        if sesiones <= 0:
            raise ServicioError("Las sesiones deben ser mayores a 0")

        self.sesiones = sesiones

    def calcular_costo(self, impuesto=0, descuento=0):
        costo_base = self.sesiones * 120000
        costo_final = costo_base * (1 + impuesto / 100)
        costo_final -= costo_final * (descuento / 100)
        return costo_final

    def descripcion(self):
        return f"Asesoría con {self.sesiones} sesiones"

    def get_sesiones(self):
        """Obtiene la cantidad de sesiones de asesoría"""
        return self.sesiones

    def get_duracion_base(self):
        """Obtiene la duración base del servicio"""
        return self.sesiones