from flask import Flask, render_template, flash, request, url_for, redirect, session
from models import *
import hashlib

from models import buscarproductos

salt = 'x32as9dAnijnK7AOJND5ksSH3bAwnT'

app = Flask(__name__)

app.secret_key ='ajsuhdesdsd'

#index
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#iniciarSesion
@app.route('/iniciarSesion', methods=['GET', 'POST'])
def iniciarSesion():
    return render_template('iniciarSesion.html')

#administrador
@app.route('/administrador', methods=['GET', 'POST'])
def administrador():
    return render_template('administrador.html')

#registrar
@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarU():
    return render_template('registrarU.html')

@app.route('/administrador/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
    return render_template('registrarUsuario.html')

@app.route('/registrarLote', methods=['GET', 'POST'])
def registrarLote():
    return render_template('registrarLote.html')

@app.route('/registrarProducto', methods=['GET', 'POST'])
def registrarProducto():
    return render_template('registrarProducto.html')

#Gestionar
@app.route('/gestionarUsuarios', methods=['GET', 'POST'])
def gestionarUsuarios():
    return render_template('gestionarUsuarios.html')

@app.route('/gestionarLotes', methods=['GET', 'POST'])
def gestionarLotes():
    return render_template('gestionarLotes.html')

@app.route('/gestionarProductos', methods=['GET', 'POST'])
def gestionarProductos():
    return render_template('gestionarProductos.html')

#Editar
@app.route('/editarUsuario', methods=['GET', 'POST'])
def editarUsuario():
    return render_template('editarUsuario.html')

@app.route('/editarLote', methods=['GET', 'POST'])
def editarLote():
    return render_template('editarLote.html')

@app.route('/editarProducto', methods=['GET', 'POST'])
def editarProducto():
    return render_template('editarProducto.html')

#Eliminar
@app.route('/eliminarUsuario', methods=['GET', 'POST'])
def eliminarUsuario():
    return render_template('eliminarUsuario.html')

@app.route('/eliminarLote', methods=['GET', 'POST'])
def eliminarLote():
    return render_template('eliminarLote.html')

@app.route('/eliminarProducto', methods=['GET', 'POST'])
def eliminarProducto():
    return render_template('eliminarProducto.html')

#Buscar
@app.route('/buscarUsuario', methods=['GET', 'POST'])
def buscarUsuario():
    return render_template('buscarUsuario.html')

@app.route('/buscarLote', methods=['GET', 'POST'])
def buscarLote():
    if request.method == "POST":
        buscalote = request.form["busqueda"] #aqui se esta obteniendo la informacion de busqueda del usuario
        buscalote = buscarproductos(buscalote)
        return render_template('buscarLote.html', buscalote=buscalote)
    return render_template('buscarLote.html')

@app.route('/buscarProducto', methods=['GET', 'POST'])
def buscarProducto():
    if request.method == "POST":
        buscaproductos = request.form["busqueda"] #aqui se esta obteniendo la informacion de busqueda del usuario
        producto = buscarproductos(buscaproductos)
        return render_template('buscarProducto.html', producto=producto)
    return render_template('buscarProducto.html')

#Errores
@app.route('/error401', methods=['GET', 'POST'])
def error401():
    return render_template('401.html')

@app.route('/error404', methods=['GET', 'POST'])
def error404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug = True)