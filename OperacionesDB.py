from Conexion import ObtenerConexion  # Importa la función para conectar con la base de datos
import psycopg2

# Validar el ingreso del usuario
def ValidaIngreso(username):
    """
    Valida si el usuario existe en la base de datos y obtiene su nombre y contraseña.

    Parámetros:
        username (str): El nombre de usuario a validar.

    Retorna:
        tuple: Una tupla con el nombre y la contraseña del usuario si existe.
        None: Si el usuario no existe o ocurre un error.
    """
    conn = ObtenerConexion()  # Crea la conexión con Supabase
    try:
        # Realiza una consulta en la tabla 'usuarios' para obtener el nombre y la contraseña
        response = conn.table("usuarios").select("name, password").eq("name", username).execute()

        if response.data:  # Si hay datos en la respuesta
            # Retorna el primer resultado como una tupla (name, password)
            return response.data[0]["name"], response.data[0]["password"]

        return None  # Retorna None si no se encontraron resultados
    except Exception as e:
        # Captura cualquier excepción y la imprime para depuración
        print(f"Error al validar ingreso: {e}")
        return None

# Obtener todas las tablas (esto puede adaptarse a tus necesidades reales)
def obtener_todas_las_tablas():
    """
    Obtiene todas las filas de la tabla 'tu_tabla' (puedes reemplazar 'tu_tabla' por el nombre real).

    Retorna:
        list: Una lista con los datos de la tabla si la consulta es exitosa.
        None: Si ocurre un error durante la consulta.
    """
    conn = ObtenerConexion()  # Crea la conexión con Supabase
    try:
        # Realiza una consulta para seleccionar todos los registros de 'tu_tabla'
        response = conn.table("movimientos_caja").select("*").execute()

        return response.data  # Retorna los datos de la respuesta
    except Exception as e:
        # Captura cualquier excepción y la imprime para depuración
        print(f"Error al obtener datos: {e}")
        return None
 


def guardar_en_db(fecha, monto, tipo_movimiento, tipo_pago, comentario):
    conn = ObtenerConexion() 
    try:
        data = {
            "fecha": fecha,
            "monto": monto,
            "tipoMovimiento": tipo_movimiento,
            "tipoPago": tipo_pago,
            "comentario": comentario
        }
        response = conn.table('movimientos_caja').insert(data).execute()
        return response.data  

    except Exception as e:
        raise Exception(f"Error al insertar en la base de datos: {e}")
    
    
def obtener_todos_los_movimientos():
    conn = ObtenerConexion()  # Asumiendo que ya tienes esta función configurada
    response = conn.table("movimientos_caja").select("*").execute() 
    return response.data