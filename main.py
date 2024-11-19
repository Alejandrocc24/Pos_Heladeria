from flask import Flask, redirect, render_template, request, session, url_for, flash, g
from flask_wtf import CSRFProtect
from OperacionesDB import *  # Importación de operaciones personalizadas para manejo de la base de datos
import requests
import unittest
import logging

# Creación de la aplicación Flask
App = Flask(__name__)
App.secret_key = '125AS35%$#2564"#$365/'  # Clave secreta para manejar sesiones y cookies
csrf = CSRFProtect(App)  # Protección CSRF para evitar ataques de tipo Cross-Site Request Forgery

# Ruta para el inicio de sesión
@App.route('/')
def Login():  
    return render_template('Login.html')  # Renderiza la plantilla HTML de login

# Ruta principal para el Home y validación de login
@App.route('/Home/', methods=['POST','GET'])
def Home():    
    # Obtiene los datos del formulario de inicio de sesión
    Usuario = request.form.get('Name')
    Contra = request.form.get('Password')

    # Validación del usuario en la base de datos
    Dato = ValidaIngreso(Usuario)  # Consulta personalizada en la base de datos

    # Si la solicitud es POST, se procesa el login
    if request.method == 'POST':
        if Dato is not None:  # Si se encontró el usuario en la base de datos
            if Usuario == Dato[0] and Contra == Dato[1]:  # Validación de credenciales
                session['username'] = request.form.get('Name')  # Se inicia la sesión
                
                datos = obtener_todas_las_tablas()  # Obtiene datos adicionales (de prueba)

                return render_template('Home.html', Name=session['username'], datos=datos)  # Renderiza el home
            
            else:  # Contraseña incorrecta
                flash(f'Usuario: {Usuario}, Contraseña Incorrecta')                
        else:  # Usuario no encontrado en la base de datos
            flash(f'El Usuario {Usuario}, no está en la base de datos')
    return redirect('/')  # Redirige al login si falla la validación

# Ruta para cerrar sesión
@App.route('/Logout/', methods=['POST', 'GET'])
def Logout():
    if 'username' in session:  # Si hay una sesión activa
        session.pop('username')  # Elimina la sesión       
    return redirect('/')  # Redirige al login


# Ruta para retorno al home
@App.route('/HomePages/', methods=['POST', 'GET'])
def HomePages():
     return render_template('Home.html') 

# Ruta para ventas
@App.route('/Ventas/', methods=['POST', 'GET'])
def Ventas():
     return render_template('Ventas.html')  # Renderiza la plantilla de ventas

#Ruta para gastos
@App.route('/Gastos/', methods=['POST', 'GET'])
def Gastos():
     return render_template('Gastos.html')

#Ruta para productos
@App.route('/Productos/', methods=['POST', 'GET'])
def Productos():
     return render_template('Productos.html')

#Ruta para pantalla
@App.route('/Pantalla/', methods=['POST', 'GET'])
def Pantalla():
     return render_template('Pantalla.html')

#Ruta para configuracion
@App.route('/Configuracion/', methods=['POST', 'GET'])
def Configuracion():
     return render_template('Configuracion.html')


# Registro de respuesta HTTP para depuración
@App.after_request
def log_the_status_code(response):   
    print(str(response.status_code))  # Imprime el código de estado de cada respuesta
    return response

# Ruta de información útil para depuración (muestra detalles de la solicitud)
@App.route('/info', methods=["GET", "POST"])
def inicio():
    cad = ""  # Cadena para almacenar la información
    cad += "URL:" + request.url + "<br/>"
    cad += "Método:" + request.method + "<br/>"
    cad += "header:<br/>"    

    # Itera sobre los headers de la solicitud
    for item, value in request.headers.items():
        cad += "{}:{}<br/>".format(item, value)    

    # Información enviada en formularios (POST)
    cad += "información en formularios (POST):<br/>"
    for item, value in request.form.items():
        cad += "{}:{}<br/>".format(item, value)

    # Información enviada en la URL (GET)
    cad += "información en URL (GET):<br/>"
    for item, value in request.args.items():
        cad += "{}:{}<br/>".format(item, value)    

    # Archivos adjuntos
    cad += "Ficheros:<br/>"
    for item, value in request.files.items():
        cad += "{}:{}<br/>".format(item, value)

    return cad, 200, {"Status": 200}  # Retorna los datos con un código de estado 200

# Función de prueba para conexión a la base de datos
def prueba_conexion():
    conn = ObtenerConexion()  # Establece la conexión con la base de datos
    try:
        response = conn.table("usuarios").select("*").execute()  # Consulta de prueba
        print(response.data)  # Imprime los datos de la tabla usuarios
    except Exception as e:
        print(f"Error al conectar: {e}")  # Manejo de errores de conexión

# Inicio del servidor Flask
if __name__ == "__main__":
    prueba_conexion()  # Verifica la conexión antes de iniciar la aplicación
    App.run(debug=True, port=8080)  # Ejecuta el servidor en modo debug y puerto 8080
