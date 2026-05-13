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

        logging.info(f"Simulación {numero} completada exitosamente")
        print("✓ Operación completada correctamente")

    except ClienteError as e:

        logging.error(f"Error de Cliente en simulación {numero}: {str(e)}")
        print(f"✗ ERROR DE CLIENTE: {e}")

    except ServicioError as e:

        logging.error(f"Error de Servicio en simulación {numero}: {str(e)}")
        print(f"✗ ERROR DE SERVICIO: {e}")

    except ReservaError as e:

        logging.error(f"Error de Reserva en simulación {numero}: {str(e)}")
        print(f"✗ ERROR DE RESERVA: {e}")

    except Exception as e:

        logging.error(f"Error general en simulación {numero}: {type(e).__name__} - {str(e)}")
        print(f"✗ ERROR GENERAL: {e}")

    finally:

        print("Simulación finalizada\n")


# SIMULACIÓN 1 - Reserva exitosa con duración

def simulacion_1():

    cliente = Cliente("1001", "Daniel Silva", "daniel.silva@example.com", "3101234567")
    servicio = ReservaSala(3)
    reserva = Reserva(cliente, servicio, duracion=2)

    reserva.confirmar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 2 - Reserva editable antes de confirmar

def simulacion_2():

    cliente = Cliente("1002", "Pedro Pérez", "pedro.perez@example.com", "3109876543")
    servicio = ReservaSala(2)
    reserva = Reserva(cliente, servicio, duracion=1)

    reserva.modificar_duracion(4)
    reserva.confirmar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 3 - Nombre vacío (error esperado)

def simulacion_3():

    cliente = Cliente("1003", "", "carla@example.com", "3123456789")
    servicio = ReservaSala(1)
    reserva = Reserva(cliente, servicio, duracion=1)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 4 - Servicio no disponible (error esperado)

def simulacion_4():

    cliente = Cliente("1004", "Carlos López", "carlos.lopez@example.com", "3123456789")
    servicio = ReservaSala(2)
    servicio.disponible = False
    reserva = Reserva(cliente, servicio, duracion=1)

    reserva.confirmar()


# SIMULACIÓN 5 - Reserva de alquiler de equipo

def simulacion_5():

    cliente = Cliente("1005", "Laura Martínez", "laura.martinez@example.com", "3151234567")
    servicio = AlquilerEquipo(5)
    reserva = Reserva(cliente, servicio, duracion=3)

    reserva.confirmar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 6 - Reserva cancelada

def simulacion_6():

    cliente = Cliente("1006", "María Gómez", "maria.gomez@example.com", "3141234567")
    servicio = Asesoria(2)
    reserva = Reserva(cliente, servicio, duracion=1)

    reserva.cancelar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 7 - Servicio None (error esperado)

def simulacion_7():

    cliente = Cliente("1007", "Andrés Ruiz", "andres.ruiz@example.com", "3159876543")
    reserva = Reserva(cliente, None, duracion=1)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 8 - Servicio con duración inválida (error esperado)

def simulacion_8():

    cliente = Cliente("1008", "Carlos Álvarez", "carlos.alvarez@example.com", "3161234567")
    servicio = AlquilerEquipo(-5)
    reserva = Reserva(cliente, servicio, duracion=1)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 9 - Confirmación repetida (error esperado)

def simulacion_9():

    cliente = Cliente("1009", "Roberto Díaz", "roberto.diaz@example.com", "3171234567")
    servicio = ReservaSala(2)
    reserva = Reserva(cliente, servicio, duracion=1)

    reserva.confirmar()
    reserva.confirmar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 10 - Cálculo con impuesto y descuento

def simulacion_10():

    cliente = Cliente("1011", "Valeria Ortiz", "valeria.ortiz@example.com", "3191234567")
    servicio = Asesoria(2)
    costo = servicio.calcular_costo(impuesto=10, descuento=5)

    print(f"Costo con impuesto y descuento: ${costo:.2f}")

    reserva = Reserva(cliente, servicio, duracion=2)
    reserva.confirmar()

    clientes.append(cliente)
    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# SIMULACIÓN 11 - Reserva procesada exitosamente

def simulacion_11():

    cliente = Cliente("1010", "Andrea Rincón", "andrea.rincon@example.com", "3181234567")
    servicio = Asesoria(3)
    reserva = Reserva(cliente, servicio, duracion=2)

    reserva.procesar()

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
        print("4. Ver logs")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit() or opcion not in {"1", "2", "3", "4", "5"}:
            print("Opción inválida. Por favor ingrese un número entre 1 y 5.")
            continue

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
            ejecutar_simulacion(11, simulacion_11)

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

            print("\n===== LOGS DEL SISTEMA =====")

            try:
                with open("logs.txt", "r") as archivo:
                    contenido = archivo.read()
                    if contenido:
                        print(contenido)
                    else:
                        print("No hay registros de logs")
            except FileNotFoundError:
                print("Archivo de logs no encontrado")

        elif opcion == "5":

            print("\n===== FIN DEL SISTEMA =====")
            break

        else:

            print("Opción inválida")


if __name__ == "__main__":

    menu()