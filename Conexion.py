from supabase import create_client, Client

# Configuración de Supabase
SUPABASE_URL = "https://bqblnbexahjyysduaach.supabase.co"  # Reemplaza con tu URL de Supabase
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJxYmxuYmV4YWhqeXlzZHVhYWNoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMTcwNjY4NCwiZXhwIjoyMDQ3MjgyNjg0fQ.FzACCxDLviOCH4k2VUWyXsLcnQSXjLLWRCFZv9Cyxh4"  # Reemplaza con tu clave de API

def ObtenerConexion():
    return create_client(SUPABASE_URL, SUPABASE_KEY)
