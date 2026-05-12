from cliente import Cliente
from reservas import Reserva
from servicios_especiales import ReservaSala, AlquilerEquipo, Asesoria
from excepciones import ClienteError, ServicioError, ReservaError

import logging
import logger_config

clientes = []
reservas = []

print("===== SISTEMA SOFTWARE FJ =====")


def ejecutar_simulacion(numero, funcion):

    print(f"\n--- SIMULACIÓN {numero} ---")

    try:

        funcion()

    except (ClienteError, ServicioError, ReservaError) as e:

        logging.error(e)

        print("ERROR CONTROLADO:", e)

    except Exception as e:

        logging.error(e)

        print("ERROR GENERAL:", e)

    else:

        print("Operación completada correctamente")

    finally:

        print("Simulación finalizada")


# SIMULACIÓN 1

def simulacion_1():

    cliente = Cliente("Daniel", 25)

    servicio = ReservaSala(3)

    reserva = Reserva(cliente, servicio)

    reserva.confirmar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 2

def simulacion_2():

    cliente = Cliente("Pedro", 15)


# SIMULACIÓN 3

def simulacion_3():

    cliente = Cliente("", 20)


# SIMULACIÓN 4

def simulacion_4():

    servicio = ReservaSala(0)


# SIMULACIÓN 5

def simulacion_5():

    cliente = Cliente("Laura", 30)

    servicio = AlquilerEquipo(5)

    reserva = Reserva(cliente, servicio)

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 6

def simulacion_6():

    cliente = Cliente("Maria", 28)

    servicio = Asesoria(2)

    reserva = Reserva(cliente, servicio)

    reserva.cancelar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 7

def simulacion_7():

    servicio = ReservaSala(2)

    reserva = Reserva(None, servicio)


# SIMULACIÓN 8

def simulacion_8():

    cliente = Cliente("Carlos", "veinte")


# SIMULACIÓN 9

def simulacion_9():

    servicio = AlquilerEquipo(-5)


# SIMULACIÓN 10

def simulacion_10():

    cliente = Cliente("Andrea", 40)

    servicio = ReservaSala(10)

    reserva = Reserva(cliente, servicio)

    reserva.confirmar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# MENÚ PRINCIPAL

def menu():

    while True:

        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ejecutar simulaciones")
        print("2. Ver clientes registrados")
        print("3. Ver reservas registradas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            # EVITA DUPLICADOS
            clientes.clear()
            reservas.clear()

            ejecutar_simulacion(1, simulacion_1)
            ejecutar_simulacion(2, simulacion_2)
            ejecutar_simulacion(3, simulacion_3)
            ejecutar_simulacion(4, simulacion_4)
            ejecutar_simulacion(5, simulacion_5)
            ejecutar_simulacion(6, simulacion_6)
            ejecutar_simulacion(7, simulacion_7)
            ejecutar_simulacion(8, simulacion_8)
            ejecutar_simulacion(9, simulacion_9)
            ejecutar_simulacion(10, simulacion_10)

        elif opcion == "2":

            print("\n===== CLIENTES REGISTRADOS =====")

            if len(clientes) == 0:

                print("No hay clientes registrados")

            else:

                for cliente in clientes:

                    print(cliente.mostrar_datos())

        elif opcion == "3":

            print("\n===== RESERVAS REGISTRADAS =====")

            if len(reservas) == 0:

                print("No hay reservas registradas")

            else:

                for reserva in reservas:

                    print(reserva.mostrar_reserva())

        elif opcion == "4":

            print("\n===== FIN DEL SISTEMA =====")
            break

        else:

            print("Opción inválida")


if __name__ == "__main__":

    menu()