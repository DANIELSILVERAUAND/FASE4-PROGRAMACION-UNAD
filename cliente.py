from abc import ABC, abstractmethod
from excepciones import ClienteError
import re


class EntidadSistema(ABC):
    """
    Clase abstracta que representa cualquier entidad gestionada por el sistema.
    Obliga a implementar descripcion() y validar() en todas las subclases.
    """

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def validar(self):
        pass


class Cliente(EntidadSistema):
    """
    Representa un cliente de Software FJ.

    Atributos privados con propiedades para encapsulación:
        _identificacion : str  — Cédula / NIT único del cliente.
        _nombre         : str  — Nombre completo.
        _email          : str  — Correo electrónico válido.
        _telefono       : str  — Número telefónico (solo dígitos, 7-15 chars).
    """

    EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self, identificacion, nombre, email, telefono):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.validar()

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        if not isinstance(self.__identificacion, str) or not self.__identificacion.strip():
            raise ClienteError("La identificación es obligatoria")

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ClienteError("El nombre del cliente no puede estar vacío")

        if not isinstance(self.__email, str) or not Cliente.EMAIL_PATTERN.match(self.__email):
            raise ClienteError("El correo electrónico no es válido")

        if not isinstance(self.__telefono, str) or not self.__telefono.isdigit():
            raise ClienteError("El teléfono debe contener solo dígitos")

        if len(self.__telefono) < 7 or len(self.__telefono) > 15:
            raise ClienteError("El teléfono debe tener entre 7 y 15 dígitos")

        return True

    def descripcion(self):
        return f"Cliente {self.__nombre} ({self.__identificacion})"

    def mostrar_datos(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"ID: {self.__identificacion} | "
            f"Email: {self.__email} | "
            f"Tel: {self.__telefono}"
        )

    def __str__(self):
        return self.mostrar_datos()