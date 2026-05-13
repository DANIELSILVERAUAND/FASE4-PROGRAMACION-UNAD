# Sistema de Gestión - Software FJ

Proyecto desarrollado en Python para la fase 4 del curso Programación 213023A_2201 de la UNAD.
Estudiantes: DANIEL SILVERA GUTIERREZ, HENRY MARTINEZ ALVAREZ

## Características

### Conceptos OOP
- Programación Orientada a Objetos
- Herencia
- Polimorfismo
- Encapsulación
- Clases abstractas y contratos comunes

### Gestión de Errores
- Excepciones personalizadas: ClienteError, ServicioError, ReservaError y subclases especializadas
- Manejo robusto con bloques try/except, try/except/else y try/except/finally
- Encadenamiento de excepciones con raise ... from e
- Registro de errores y eventos en archivo de logs

### Cliente y Entidades
- Clase abstracta EntidadSistema
- Clase Cliente con encapsulación de datos privados
- Validaciones estrictas de identificación, nombre, email y teléfono
- Propiedades y métodos bien definidos

### Servicios
- Clase abstracta Servicio con polimorfismo
- Servicios especializados: ReservaSala, AlquilerEquipo, Asesoria
- Métodos sobrescritos para cálculo de costo, descripción y duración base
- Disponibilidad de servicio controlada con estado disponible/no disponible
- Cálculo con parámetros opcionales: impuesto y descuento

### Sistema de Reservas
- ID único generado automáticamente
- Duración configurable por reserva
- Estados de reserva: PENDIENTE, CONFIRMADA, CANCELADA, PROCESADA
- Operaciones de confirmación, cancelación y procesamiento
- Manejo avanzado de excepciones en el flujo de reservas
- Validación de datos y protección contra operaciones no permitidas

### Interfaz de Usuario
- Menú interactivo con validación de entrada
- Opción para visualizar logs del sistema
- Visualización de clientes registrados
- Visualización de reservas registradas
- Ejecución de simulaciones con casos válidos e inválidos

### Sistema de Simulaciones
- Simulaciones que muestran reservas exitosas y fallidas
- Casos de datos inválidos, servicios no disponibles y confirmaciones repetidas
- Registro de cada evento y error en el archivo de logs
- El programa continúa funcionando aún si una simulación falla

## Ejecución

```bash
python main.py
