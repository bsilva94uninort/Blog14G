import os

import yagmail as yagmail
from flask import Flask, render_template, flash, request, url_for,redirect
import utils

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signup14G', methods=('GET', 'POST'))
def signup14G():
    #eljava="validarFormulario()"
    return render_template('signup14G.html')

@app.route('/login14G', methods=('GET', 'POST'))
def login14G():
    return render_template('login14G.html')

@app.route('/recuperar', methods=('GET', 'POST'))
def recuperar():
    return render_template('recuperar.html')

@app.route('/buscar', methods=('GET', 'POST'))
def buscar():
    return render_template('buscar.html')

@app.route('/comentar', methods=('GET', 'POST'))
def comentar():
    return render_template('comentar.html')

@app.route('/crearactualizar', methods=('GET', 'POST'))
def crearactualizar():
    return render_template('crear_actualizar.html')

@app.route('/eliminar', methods=('GET', 'POST'))
def eliminar():
    return render_template('eliminar.html')

@app.route('/index14G', methods=('GET', 'POST'))
def index14G():
    return render_template('index14G.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['password']
            email = request.form['email']
            error = None

            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash(error)
                return render_template('register.html')
                #return redirect(url_for('register'))

            if not utils.isPasswordValid(password):
                error = 'La contraseña debe contenir al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('register.html')
                #return redirect(url_for('register'))

            if not utils.isEmailValid(email):
                #print("4")
                error = 'Correo invalido'
                flash(error)
                return render_template('register.html')
                #return redirect(url_for('register'))

            yag = yagmail.SMTP('pruebamintic2022', 'Jmd12345678') #modificar con tu informacion personal
            yag.send(to=email, subject='Activa tu cuenta',
                     contents='Bienvenido, usa este link para activar tu cuenta ')
            flash('Revisa tu correo para activar tu cuenta')
            return render_template('login.html')
        #print("Llego al final")
        return render_template('register.html')
    except:
        return render_template('register.html')
if __name__ == "__main__":
    app.run(debug = True, port=8000)
