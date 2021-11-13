from flask import Flask, render_template, flash, request, url_for, redirect, session
import hashlib

salt = 'x32as9dAnijnK7AOJND5ksSH3bAwnT'

app = Flask(__name__)

app.secret_key ='ajsuhdesdsd'

#index
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index1')
def index1():
    return render_template('index1.html')

#administrador
@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

#registrar
@app.route('/registrarUsuario')
def registrarUsuario():
    return render_template('registrarUsuario.html')

@app.route('/registrarLote')
def registrarLote():
    return render_template('registrarLote.html')

@app.route('/registrarProducto')
def registrarProducto():
    return render_template('registrarProducto.html')

#Gestionar
@app.route('/gestionarUsuarios')
def gestionarUsuarios():
    return render_template('gestionarUsuarios.html')

@app.route('/gestionarLotes')
def gestionarLotes():
    return render_template('gestionarLotes.html')

@app.route('/registrarProductos')
def gestionarProductos():
    return render_template('gestionarProductos.html')

#Editar
@app.route('/editarUsuario')
def editarUsuario():
    return render_template('editarUsuario.html')

@app.route('/editarLote')
def editarLote():
    return render_template('editarLote.html')

@app.route('/editarProducto')
def editarProducto():
    return render_template('editarProducto.html')

#Eliminar
@app.route('/eliminarUsuario')
def eliminarUsuario():
    return render_template('eliminarUsuario.html')

@app.route('/eliminarLote')
def eliminarLote():
    return render_template('eliminarLote.html')

@app.route('/eliminarProducto')
def eliminarProducto():
    return render_template('eliminarProducto.html')

#Buscar
@app.route('/buscarUsuario')
def buscarUsuario():
    return render_template('buscarUsuario.html')

@app.route('/buscarLote')
def buscarLote():
    return render_template('buscarLote.html')

@app.route('/buscarProducto')
def buscarProducto():
    return render_template('buscarProducto.html')

<<<<<<< HEAD
"""
#detalles
@app.route('/detalles', methods=['GET', 'POST'])
def detalles():
    return render_template('detalles.hmtl')"""

=======
>>>>>>> bfbb39250f8abc3095cf9fb9f1f94f03a838eb7b
#Errores
@app.route('/error401')
def error401():
    return render_template('401.html')

@app.route('/error404')
def error404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug = True)