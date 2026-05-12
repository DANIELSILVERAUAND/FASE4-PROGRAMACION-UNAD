from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio):

        if cliente is None:
            raise ReservaError("Debe existir un cliente")

        if servicio is None:
            raise ReservaError("Debe existir un servicio")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return (
            f"{self.cliente.mostrar_datos()} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Descripción: {self.servicio.descripcion()} | "
            f"Estado: {self.estado} | "
            f"Costo: ${self.servicio.calcular_costo()}"
        )