from flask import Flask, redirect, render_template, request, session, url_for, flash, g
from flask_wtf import CSRFProtect
from OperacionesDB import *
import requests
import unittest
import logging

App = Flask(__name__)
App.secret_key = '125AS35%$#2564"#$365/'
csrf = CSRFProtect(App)

# Ruta para el login
@App.route('/')
def Login():  
    return render_template('Login.html')

#Conexion con base de datos
@App.route('/Home/', methods=['POST','GET'])
def home():    

    Usuario = request.form.get('Name')
    Contra = request.form.get('Password')

    Dato = ValidaIngreso(Usuario)
    

    if request.method == 'POST':
        if Dato != None:
            if Usuario == Dato[0] and Contra == Dato[1]:
                session['username'] = request.form.get('Name') # Iniciar sesión

                datos = obtener_todas_las_tablas() # Obtener datos de prueba

                return render_template('Home.html', Name=session['username'], datos=datos)
            
            else:
                flash(f'Usuario:{Usuario}, Contraseña Incorrecta')                
        else:
            flash(f'El Usuario {Usuario}, no esta en la base de datos')
    return redirect('/')


# Ruta para cerrar sesión
@App.route('/Logout/',  methods=['POST','GET'])
def Logout():
    if 'username' in session:
        session.pop('username')   # Eliminar sesión       
    return redirect('/') 

# @App.route('/Home/',  methods=['POST','GET'])
# def prueba():
#     return render_template('Modal.html')

# Registro de respuesta para depuración
@App.after_request
def log_the_status_code(response):   
    print(str(response.status_code))  
    return response

# Ruta de prueba para verificar funcionalidad    
@App.route('/Prueba',  methods=['POST','GET'])
def Prueba():
    
    return 'OK'

# Ruta para mostrar información de la solicitud (útil para depuración)
@App.route('/info',methods=["GET","POST"])
def inicio():
    cad=""
    cad+="URL:"+request.url+"<br/>"
    cad+="Método:"+request.method+"<br/>"
    cad+="header:<br/>"    

    for item,value in request.headers.items():
        cad+="{}:{}<br/>".format(item,value)    
    cad+="información en formularios (POST):<br/>"
    for item,value in request.form.items():
        cad+="{}:{}<br/>".format(item,value)
    cad+="información en URL (GET):<br/>"
    for item,value in request.args.items():
        cad+="{}:{}<br/>".format(item,value)    
    cad+="Ficheros:<br/>"
    for item,value in request.files.items():
        cad+="{}:{}<br/>".format(item,value)
    return cad , 200, {"Status":200}
    
def prueba_conexion():
    conn = ObtenerConexion()
    try:
        response = conn.table("usuarios").select("*").execute()
        print(response.data)  # Deberías ver los datos de la tabla usuarios
    except Exception as e:
        print(f"Error al conectar: {e}")

if __name__ == "__main__":
    prueba_conexion()    

if __name__ == '__main__':
    App.run(debug=True, port=8080)


