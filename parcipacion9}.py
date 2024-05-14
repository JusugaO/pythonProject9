import math

class DatosMeteorologicos:
  """
  Esta clase permite procesar datos meteorológicos de un archivo de texto.

  Atributos:
    nombre_archivo: str - Ruta del archivo de texto que contiene los datos.

  Métodos:
    __init__(self, nombre_archivo): Inicializa la clase con el nombre del archivo.
    procesar_datos(self): Procesa los datos del archivo y devuelve las estadísticas.
  """

  def __init__(self, nombre_archivo):
    """
    Inicializa la clase con el nombre del archivo de texto.

    Args:
      nombre_archivo: str - Ruta del archivo de texto que contiene los datos.
    """
    self.nombre_archivo = nombre_archivo

  def procesar_datos(self):
    """
    Procesa los datos del archivo y devuelve las estadísticas.

    Returns:
      Tuple[float, float, float, float, str]: Tupla con las estadísticas calculadas:
        - Temperatura promedio
        - Humedad promedio
        - Presión promedio
        - Velocidad promedio del viento
        - Dirección predominante del viento
    """
    # Inicializar variables para almacenar promedios y datos de viento
    suma_temperatura = 0
    suma_humedad = 0
    suma_presion = 0
    suma_velocidad_viento = 0
    cantidad_mediciones = 0
    direccion_viento_frecuencias = {}

    # Abrir el archivo de texto en modo lectura
    with open(self.nombre_archivo, 'r') as archivo:
      # Leer cada línea del archivo
      for linea in archivo:
        # Eliminar espacios en blanco al inicio y final de la línea
        linea = linea.strip()

        # Si la línea está vacía, continuar a la siguiente
        if not linea:
          continue

        # Dividir la línea en sus componentes
        datos_linea = linea.split(',')
        nombre_estacion = datos_linea[0].split(':')[1].strip()
        latitud = float(datos_linea[1].split(':')[1].strip())
        longitud = float(datos_linea[2].split(':')[1].strip())
        fecha = datos_linea[3].split(':')[1].strip()
        hora = datos_linea[4].split(':')[1].strip()
        temperatura = float(datos_linea[5].split(':')[1].strip())
        humedad = float(datos_linea[6].split(':')[1].strip())
        presion = float(datos_linea[7].split(':')[1].strip())
        velocidad_viento, direccion_viento = datos_linea[8].split(':')[1].strip().split(',')
        velocidad_viento = float(velocidad_viento)

        # Actualizar promedios
        suma_temperatura += temperatura
        suma_humedad += humedad
        suma_presion += presion
        suma_velocidad_viento += velocidad_viento

        # Procesar dirección del viento
        direccion_viento_grados = self.convertir_direccion_grados(direccion_viento)
        if direccion_viento_grados in direccion_viento_frecuencias:
          direccion_viento_frecuencias[direccion_viento_grados] += 1
        else:
          direccion_viento_frecuencias[direccion_viento_grados] = 1

        # Actualizar conteo de mediciones
        cantidad_mediciones += 1

    # Calcular promedios
    temperatura_promedio = suma_temperatura / cantidad_mediciones
    humedad_promedio = suma_humedad / cantidad_mediciones
    presion_promedio = suma_presion / cantidad_mediciones
    velocidad_viento_promedio = suma_velocidad_viento / cantidad_mediciones

    # Determinar dirección predominante del viento
    direccion_predominante = self.calcular_direccion_predominante(direccion_viento_frecuencias)

    # Devolver tupla con las estadísticas
    return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_predominante

  def convertir_direccion_grados(self, direccion_viento):
    """
    Convierte una abreviatura de dirección del viento a grados.

    Args:
      direccion_viento: str - Abreviatura de la dirección del viento (


