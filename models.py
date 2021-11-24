from flask import Flask, render_template, flash, request, url_for, redirect, session
from db import *

#obtener rol y creacion usuario
"""def creacionusuario(): 
    if "id_user" in session and session["rol"] == "superadministrador":
        db = get_db()
        roles = db.execute(
            'SELECT id, rol FROM roles'
        ).fetchall()
        if request.method == 'POST':
            # POST:
            nombres= request.form['nombre']
            apellidos= request.form['apellidos']
            documentos = request.form['documentos']
            identificacion = request.form['identificacion']
            usuario = request.form['usuario']
            contrasena = request.form['contrasena']
            roles = request.form['roles']
            if nombres == "" or apellidos == "" or documentos == "" or identificacion == "" or usuario == "" or contrasena == "" or roles == "":
                error = 'Al menos un dato no fue ingresado'
                flash( error )
                return redirect(url_for("creacionusuario"))
            else:
                conn = get_db()        
                cursorObj = conn.cursor()        
                cursorObj.execute(
                    "INSERT INTO usuario (nombres, apellidos, documento, identificacion, usuario, contrasena, roles) VALUES (?,?,?,?,?,?,?)",(nombres, apellidos, documentos, identificacion, usuario, generate_password_hash(contrasena), roles)
                )
                print("Aquí.")
                conn.commit() 
                conn.close()
                return redirect(url_for("creacionusuario"))
            
        return render_template('creacionUsuario.html', roles=roles)
    else:
        session.clear()
        return redirect(url_for("index"))"""

#buscar producto
def buscarproductos(buscaproductos): 
    db = get_db()
    producto = db.execute(
        'SELECT * FROM productos WHERE nombre_producto="{}" COLLATE NOCASE or codigo_producto="{}" COLLATE NOCASE'.format(buscaproductos,buscaproductos)
    ).fetchall()
    return(producto)
