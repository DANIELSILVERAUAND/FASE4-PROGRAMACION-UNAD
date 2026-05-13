# Sistema de Gestión - Software FJ

Proyecto desarrollado en Python para la fase 4 del curso Programación 213023A_2201 de la UNAD.
Estudiantes: DANIEL SILVERA GUTIERREZ, HENRY MARTINEZ ALVAREZ

## Características

### Conceptos OOP
- Programación Orientada a Objetos
- Herencia
- Polimorfismo
- Encapsulación
- Clase abstracta

### Gestión de Errores
- Excepciones personalizadas (ClienteError, ServicioError, ReservaError)
- Manejo específico de errores por tipo
- Sistema de logs detallado
- Validaciones robustas en todas las operaciones

### Sistema de Reservas
- ID único generado automáticamente para cada reserva
- Duración configurable por reserva
- Cálculo automático de costo total (costo base × duración)
- Fecha y hora de creación de cada reserva
- Estados de reserva: Pendiente, Confirmada, Cancelada
- Validación completa de datos antes de confirmar
- Contador de reservas creadas

### Interfaz de Usuario
- Menú interactivo con 5 opciones
- Opción para visualizar logs del sistema
- Visualización de clientes registrados
- Visualización de reservas confirmadas
- Ejecución de 10 simulaciones (5 exitosas, 5 con errores esperados)

### Sistema de Simulaciones
- 10 simulaciones completas que prueban diferentes escenarios
- Casos de éxito y casos de error controlados
- Registro detallado de cada simulación en logs
- Mensajes de error específicos y diferenciados

## Ejecución

```bash
python main.py
