from excepciones import ReservaError
from datetime import datetime
import uuid

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
        """
        Inicializa una nueva reserva.

        Args:
            cliente: Objeto Cliente
            servicio: Objeto Servicio
            duracion: Duración de la reserva (default: 1)

        Raises:
            ReservaError: Si cliente o servicio son None
        """
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
        self.estado = "Pendiente"
        self.fecha_creacion = datetime.now()
        self.costo_total = None

        Reserva.contador_reservas += 1

    def validar_reserva(self):
        """
        Valida que la reserva tenga todos los datos necesarios.

        Raises:
            ReservaError: Si la reserva no es válida
        """
        if self.cliente is None:
            raise ReservaError("Cliente no válido")

        if self.servicio is None:
            raise ReservaError("Servicio no válido")

        if self.duracion <= 0:
            raise ReservaError("Duración no válida")

        return True

    def confirmar(self):
        """
        Confirma la reserva y calcula el costo total.

        Raises:
            ReservaError: Si no se puede confirmar la reserva
        """
        try:
            self.validar_reserva()
            self.estado = "Confirmada"
            self.costo_total = self.calcular_costo_total()
        except ReservaError as e:
            raise ReservaError(f"Error al confirmar reserva: {str(e)}")

    def cancelar(self):
        """
        Cancela la reserva.

        Raises:
            ReservaError: Si la reserva ya estaba cancelada
        """
        if self.estado == "Cancelada":
            raise ReservaError("La reserva ya fue cancelada")

        self.estado = "Cancelada"
        self.costo_total = 0

    def calcular_costo_total(self):
        """
        Calcula el costo total de la reserva.

        Returns:
            float: Costo total de la reserva
        """
        try:
            costo_base = self.servicio.calcular_costo()
            return costo_base * self.duracion
        except Exception as e:
            raise ReservaError(f"Error al calcular costo: {str(e)}")

    def obtener_estado(self):
        """Obtiene el estado actual de la reserva"""
        return self.estado

    def obtener_id(self):
        """Obtiene el ID de la reserva"""
        return self.id_reserva

    def mostrar_reserva(self):
        """
        Muestra la información completa de la reserva.

        Returns:
            str: Información formateada de la reserva
        """
        try:
            costo_display = f"${self.costo_total}" if self.costo_total is not None else "No calculado"

            return (
                f"[ID: {self.id_reserva}] "
                f"{self.cliente.mostrar_datos()} | "
                f"Servicio: {self.servicio.nombre} | "
                f"Descripción: {self.servicio.descripcion()} | "
                f"Duración: {self.duracion} | "
                f"Estado: {self.estado} | "
                f"Costo Total: {costo_display} | "
                f"Fecha: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        except Exception as e:
            raise ReservaError(f"Error al mostrar reserva: {str(e)}")