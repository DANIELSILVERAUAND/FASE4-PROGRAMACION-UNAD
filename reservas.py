from excepciones import (
    ReservaError,
    ReservaYaConfirmadaError,
    ReservaYaCanceladaError,
    ServicioNoDisponibleError,
    CalculoCostoError,
)
from datetime import datetime
from enum import Enum
import uuid


class EstadoReserva(str, Enum):
    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    PROCESADA = "PROCESADA"


class Reserva:
    """
    Representa una reserva de un servicio por parte de un cliente.

    Attributes:
        id_reserva      : Identificador único generado automáticamente.
        cliente         : Objeto Cliente asociado.
        servicio        : Objeto Servicio asociado.
        duracion        : Duración (horas o días según el servicio).
        estado          : EstadoReserva actual.
        fecha_creacion  : Fecha/hora de creación.
        costo_total     : Costo calculado al confirmar.
    """

    contador_reservas = 0

    def __init__(self, cliente, servicio, duracion=1):
        if cliente is None:
            raise ReservaError("Debe existir un cliente para crear una reserva")

        if servicio is None:
            raise ReservaError("Debe existir un servicio para crear una reserva")

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        self.id_reserva = str(uuid.uuid4())[:8]
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = EstadoReserva.PENDIENTE
        self.fecha_creacion = datetime.now()
        self.fecha_procesamiento = None
        self.costo_total = None

        Reserva.contador_reservas += 1

    def validar_reserva(self):
        if self.cliente is None:
            raise ReservaError("Cliente no válido")

        if self.servicio is None:
            raise ReservaError("Servicio no válido")

        if self.duracion <= 0:
            raise ReservaError("Duración no válida")

        return True

    def confirmar(self):
        try:
            self.validar_reserva()

            if self.estado == EstadoReserva.CONFIRMADA:
                raise ReservaYaConfirmadaError("La reserva ya fue confirmada")

            if self.estado == EstadoReserva.CANCELADA:
                raise ReservaYaCanceladaError("No se puede confirmar una reserva cancelada")

            if not getattr(self.servicio, "esta_disponible", lambda: True)():
                raise ServicioNoDisponibleError("El servicio no está disponible")

            self.costo_total = self.calcular_costo_total()
            self.estado = EstadoReserva.CONFIRMADA

        except (ReservaYaConfirmadaError, ReservaYaCanceladaError, ServicioNoDisponibleError, ReservaError):
            raise
        except Exception as e:
            raise ReservaError("Error inesperado al confirmar reserva") from e
        else:
            return self.costo_total
        finally:
            self.fecha_procesamiento = datetime.now()

    def cancelar(self):
        try:
            if self.estado == EstadoReserva.CANCELADA:
                raise ReservaYaCanceladaError("La reserva ya fue cancelada")

            self.estado = EstadoReserva.CANCELADA
            self.costo_total = 0

        except ReservaYaCanceladaError:
            raise
        except Exception as e:
            raise ReservaError("Error inesperado al cancelar reserva") from e

    def calcular_costo_total(self):
        try:
            costo_base = self.servicio.calcular_costo()
            return costo_base * self.duracion
        except Exception as e:
            raise CalculoCostoError("Error al calcular el costo total") from e

    def procesar(self):
        try:
            if self.estado == EstadoReserva.CANCELADA:
                raise ReservaYaCanceladaError("No se puede procesar una reserva cancelada")

            if self.estado == EstadoReserva.PROCESADA:
                return self.costo_total

            self.confirmar()
            self.estado = EstadoReserva.PROCESADA

        except ReservaError:
            raise
        except Exception as e:
            raise ReservaError("Error inesperado al procesar reserva") from e
        else:
            return self.costo_total
        finally:
            self.fecha_procesamiento = datetime.now()

    def obtener_estado(self):
        return self.estado

    def obtener_id(self):
        return self.id_reserva

    def get_cliente(self):
        return self.cliente

    def get_servicio(self):
        return self.servicio

    def modificar_duracion(self, nueva_duracion):
        if self.estado != EstadoReserva.PENDIENTE:
            raise ReservaError(f"No se puede modificar una reserva {self.estado.value.lower()}")

        if nueva_duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        self.duracion = nueva_duracion

    def modificar_servicio(self, nuevo_servicio):
        if self.estado != EstadoReserva.PENDIENTE:
            raise ReservaError(f"No se puede modificar una reserva {self.estado.value.lower()}")

        if nuevo_servicio is None:
            raise ReservaError("El servicio no puede ser None")

        self.servicio = nuevo_servicio

    def mostrar_reserva(self):
        try:
            costo_display = f"${self.costo_total}" if self.costo_total is not None else "No calculado"
            return (
                f"[ID: {self.id_reserva}] "
                f"{self.cliente.mostrar_datos()} | "
                f"Servicio: {self.servicio.nombre} | "
                f"Descripción: {self.servicio.descripcion()} | "
                f"Duración: {self.duracion} | "
                f"Estado: {self.estado.value} | "
                f"Costo Total: {costo_display} | "
                f"Fecha creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        except Exception as e:
            raise ReservaError("Error al mostrar reserva") from e