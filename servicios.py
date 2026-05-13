from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True

    @abstractmethod
    def calcular_costo(self, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def get_duracion_base(self):
        pass

    def calcular_costo_con_impuesto(self, impuesto_porcentaje):
        base = self.calcular_costo()
        return base * (1 + impuesto_porcentaje / 100)

    def calcular_costo_con_descuento(self, descuento_porcentaje):
        base = self.calcular_costo()
        return base * (1 - descuento_porcentaje / 100)

    def esta_disponible(self):
        return bool(self.disponible)