from flask import Flask, render_template, flash, request, url_for, redirect, session
import hashlib

salt = 'x32as9dAnijnK7AOJND5ksSH3bAwnT'

app = Flask(__name__)

app.secret_key ='ajsuhdesdsd'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar')
def registrar():
    return render_template('registrarUsuario.html')


if __name__ == '__main__':
    app.run(debug = True)