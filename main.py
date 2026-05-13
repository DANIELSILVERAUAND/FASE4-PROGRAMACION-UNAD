from cliente import Cliente
from reservas import Reserva
from servicios_especiales import ReservaSala, AlquilerEquipo, Asesoria
from excepciones import ClienteError, ServicioError, ReservaError

import logging
import os
import logger_config
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import io
import contextlib

LOG_FILE = logger_config.LOG_FILE

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


def run_with_output(func, output_func):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        try:
            func()
        except Exception as e:
            print(f"✗ ERROR: {type(e).__name__} - {e}")
    output_func(buffer.getvalue())


def format_text(text_widget, text):
    text_widget.config(state="normal")
    text_widget.insert(tk.END, text)
    text_widget.see(tk.END)
    text_widget.config(state="disabled")


class ReservaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservas - Software FJ")
        self.root.geometry("880x560")
        self.root.minsize(820, 520)
        self.root.configure(bg="#eaf0f7")

        self.style = ttk.Style(root)
        try:
            self.style.theme_use("clam")
        except tk.TclError:
            pass

        self.style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), background="#eaf0f7")
        self.style.configure("Sidebar.TFrame", background="#f0f4f8")
        self.style.configure("Card.TLabelframe", background="#ffffff", borderwidth=1, relief="solid")
        self.style.configure("Card.TLabelframe.Label", font=("Segoe UI", 11, "bold"))
        self.style.configure("TButton", font=("Segoe UI", 10), padding=8)
        self.style.configure("TLabel", background="#eaf0f7")

        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        sidebar = ttk.Frame(root, width=220, style="Sidebar.TFrame")
        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_propagate(False)
        sidebar.columnconfigure(0, weight=1)

        header = ttk.Label(root, text="Sistema de Reservas - Software FJ", style="Header.TLabel")
        header.grid(row=0, column=1, sticky="nw", padx=(10, 10), pady=(10, 0))

        content_frame = ttk.Frame(root)
        content_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 10), pady=(55, 10))
        content_frame.columnconfigure(0, weight=1)
        content_frame.rowconfigure(0, weight=1)

        action_frame = ttk.Labelframe(sidebar, text="Acciones", padding=12, style="Card.TLabelframe")
        action_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Button(action_frame, text="Ejecutar simulaciones", command=self.execute_simulations).grid(row=0, column=0, sticky="ew", padx=5, pady=(0, 5))
        ttk.Button(action_frame, text="Ver clientes", command=self.show_clients).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        ttk.Button(action_frame, text="Ver reservas", command=self.show_reservations).grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        ttk.Button(action_frame, text="Ver logs", command=self.show_logs).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        ttk.Button(action_frame, text="Borrar logs", command=self.clear_logs).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        ttk.Button(action_frame, text="Salir", command=self.root.quit).grid(row=5, column=0, sticky="ew", padx=5, pady=5)

        self.output_frame = ttk.Labelframe(content_frame, text="Salida del sistema", padding=12, style="Card.TLabelframe")
        self.output_frame.grid(row=0, column=0, sticky="nsew")
        self.output_frame.columnconfigure(0, weight=1)
        self.output_frame.rowconfigure(0, weight=1)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, state="disabled", font=("Consolas", 10), bg="#fafbfc", relief="flat")
        self.output_text.grid(row=0, column=0, sticky="nsew")

        self.footer_frame = ttk.Frame(root)
        self.footer_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        self.footer_frame.columnconfigure(0, weight=1)
        self.footer_frame.columnconfigure(1, weight=1)

        self.counts_label = ttk.Label(self.footer_frame, text="Clientes: 0 | Reservas: 0 | Logs: 0")
        self.counts_label.grid(row=0, column=0, sticky="w")
        self.status_label = ttk.Label(self.footer_frame, text="Listo", anchor="e")
        self.status_label.grid(row=0, column=1, sticky="e")

        self.root.bind("<Unmap>", self.on_window_state_change)
        self.root.bind("<Map>", self.on_window_state_change)
        self.update_counts()

    def update_status(self, message):
        self.status_label.config(text=message)

    def clear_output(self):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state="disabled")

    def append_output(self, message):
        format_text(self.output_text, message)

    def get_log_count(self):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as archivo:
                return len(archivo.readlines())
        except (UnicodeDecodeError, FileNotFoundError):
            try:
                with open(LOG_FILE, "r", encoding="latin-1") as archivo:
                    return len(archivo.readlines())
            except Exception:
                return 0

    def update_counts(self):
        self.counts_label.config(text=f"Clientes: {len(clientes)} | Reservas: {len(reservas)} | Logs: {self.get_log_count()}")

    def execute_simulations(self):
        self.clear_output()
        self.update_status("Ejecutando simulaciones...")
        clientes.clear()
        reservas.clear()

        def task():
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

        run_with_output(task, self.append_output)
        self.update_status("Simulaciones ejecutadas")
        self.update_counts()

    def show_clients(self):
        self.clear_output()
        self.update_status("Mostrando clientes registrados...")

        def task():
            print("===== CLIENTES REGISTRADOS =====")
            if len(clientes) == 0:
                print("No hay clientes registrados")
            else:
                for cliente in clientes:
                    print(cliente.mostrar_datos())

        run_with_output(task, self.append_output)
        self.update_status("Clientes mostrados")
        self.update_counts()

    def show_reservations(self):
        self.clear_output()
        self.update_status("Mostrando reservas registradas...")

        def task():
            print("===== RESERVAS REGISTRADAS =====")
            if len(reservas) == 0:
                print("No hay reservas registradas")
            else:
                for reserva in reservas:
                    print(reserva.mostrar_reserva())

        run_with_output(task, self.append_output)
        self.update_status("Reservas mostradas")
        self.update_counts()

    def show_logs(self):
        self.clear_output()
        self.update_status("Cargando logs...")

        def read_logs():
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as archivo:
                    return archivo.read()
            except UnicodeDecodeError:
                with open(LOG_FILE, "r", encoding="latin-1") as archivo:
                    return archivo.read()

        def task():
            print("===== LOGS DEL SISTEMA =====")
            try:
                contenido = read_logs()
                print(contenido if contenido else "No hay registros de logs")
            except FileNotFoundError:
                print("Archivo de logs no encontrado")
            except Exception as e:
                print(f"No se pudo leer el archivo de logs: {e}")
                logging.error(f"Error al leer logs: {e}")

        run_with_output(task, self.append_output)
        self.update_status("Logs cargados")
        self.update_counts()

    def clear_logs(self):
        if not messagebox.askyesno("Confirmar", "¿Desea borrar todos los logs?"):
            return
        try:
            with open(LOG_FILE, "w", encoding="utf-8") as archivo:
                archivo.write("")
            self.append_output("Logs borrados correctamente\n")
            self.update_status("Logs borrados")
            self.update_counts()
        except Exception as e:
            self.append_output(f"No se pudo borrar el archivo de logs: {e}\n")
            logging.error(f"Error al borrar logs: {e}")
            self.update_status("Error borrando logs")

    def on_window_state_change(self, event):
        if str(self.root.state()) == "iconic":
            self.update_status("Ventana minimizada")
        else:
            self.update_status("Listo")


def main_gui():
    root = tk.Tk()
    ReservaApp(root)
    root.mainloop()


# MENÚ PRINCIPAL

def menu():

    while True:

        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ejecutar simulaciones")
        print("2. Ver clientes registrados")
        print("3. Ver reservas registradas")
        print("4. Ver logs")
        print("5. Borrar logs")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit() or opcion not in {"1", "2", "3", "4", "5", "6"}:
            print("Opción inválida. Por favor ingrese un número entre 1 y 6.")
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

            print("\n===== BORRAR LOGS =====")

            try:
                with open("logs.txt", "w") as archivo:
                    archivo.write("")
                print("Logs borrados correctamente")
            except Exception as e:
                print("No se pudo borrar el archivo de logs:", e)
                logging.error(f"Error al borrar logs: {e}")

        elif opcion == "6":

            print("\n===== FIN DEL SISTEMA =====")
            break

        else:

            print("Opción inválida")


if __name__ == "__main__":
    main_gui()