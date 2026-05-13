class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass


class ReservaYaConfirmadaError(ReservaError):
    pass


class ReservaYaCanceladaError(ReservaError):
    pass


class ServicioNoDisponibleError(ReservaError):
    pass


class CalculoCostoError(ReservaError):
    pass