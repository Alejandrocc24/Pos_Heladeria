from Conexion import ObtenerConexion

# Validar el ingreso del usuario
def ValidaIngreso(username):
    conn = ObtenerConexion()
    try:
        response = conn.table("usuarios").select("name, password").eq("name", username).execute()
        if response.data:
            return response.data[0]["name"], response.data[0]["password"]
        return None
    except Exception as e:
        print(f"Error al validar ingreso: {e}")
        return None

# Obtener todas las tablas (esto puede adaptarse a tus necesidades reales)
def obtener_todas_las_tablas():
    conn = ObtenerConexion()
    try:
        response = conn.table("tu_tabla").select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None
