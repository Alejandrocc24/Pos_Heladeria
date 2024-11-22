from supabase import create_client, Client  # Importa la biblioteca de Supabase para la conexión

# Configuración de Supabase
SUPABASE_URL = "https://bqblnbexahjyysduaach.supabase.co"  
# URL del proyecto en Supabase (reemplaza con la URL de tu propio proyecto)

SUPABASE_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJxYmxuYmV4YWhqeXlzZHVhYWNoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMTcwNjY4NCwiZXhwIjoyMDQ3MjgyNjg0fQ.FzACCxDLviOCH4k2VUWyXsLcnQSXjLLWRCFZv9Cyxh4"
)  
# Clave de API del proyecto Supabase, permite autenticar y realizar consultas
# Asegúrate de mantener esta clave privada para evitar accesos no autorizados.

def ObtenerConexion():
    """
    Crea y retorna una conexión al cliente Supabase utilizando la URL y clave de API configuradas.

    Retorna:
        Client: Una instancia del cliente Supabase.
    """
    return create_client(SUPABASE_URL, SUPABASE_KEY)  # Inicializa la conexión con los datos configurados


