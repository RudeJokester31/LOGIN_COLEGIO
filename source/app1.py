from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from config1 import config
import requests
import json

from models.ModelUser import ModelUser

from models.entities.User import User

app = Flask(__name__)


csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(id)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for("home"))
            else:
                flash(logged_user)
            return render_template('auth/login.html')
        else:
            flash("Usuario o contraseña incorrecto")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/protected")
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados</h1>"


@app.route("/usuarios", methods=['GET'])
@login_required
def listar_usuarios():
    try:
        url = "http://192.168.1.11:5000/usuarios"
        datos = requests.get(url)
        usuarios = datos.text
        usuarios = json.loads(usuarios)
        print(usuarios)
        return render_template('listar_usuarios.html', employee=usuarios)
    except Exception as ex:
        return jsonify({"mensaje": "Error", "Exito": ex})


@app.route("/usuario/<id>", methods=['GET'])
@login_required
def Consultar_usuario(id):
    try:
        cursor = db.connection.cursor()
        sql = "SELECT * FROM usuario WHERE id='{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario = {"id": datos[0], "username": datos[1], "password": datos[2], "NOMBRES": datos[3],
                       "APELLIDOS": datos[4], "EDAD": datos[5], "GRADO": datos[6], "ROL": datos[7], "ID_HUELLA": datos[8]}
            return jsonify({"Usuario": usuario, "mensaje": "Usuario encontrado"})
        else:
            return jsonify({"mensaje": "Usuario no encontrado", "Exito": True})
    except Exception as ex:
        return jsonify({"mensaje": "Error", "Exito": False})


@app.route("/usuarios", methods=["POST"])
@login_required
def Registrar_usuarios():
    try:
        cursor = db.connection.cursor()
        sql = """INSERT INTO usuario (id, username, password, NOMBRES, APELLIDOS, EDAD, GRADO, ROL, ID_HUELLA)
        VALUES ('{0}','{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')""".format(request.json['id'], request.json['username'], request.json['password'], request.json['NOMBRES'], request.json['APELLIDOS'], request.json['EDAD'], request.json['GRADO'],
                                                                                        request.json['ROL'], request.json['ID_HUELLA'])
        cursor.execute(sql)
        db.connection.commit()
        return jsonify({"mensaje": "Usuario registrado", "Exito": True})
    except Exception as ex:
        return jsonify({"mensaje": "Error", "Exito": False})


def status_401(error):
    return redirect(url_for("login"))


def status_404(error):
    return "<h1>Página no encontrada</h1>"


if __name__ == '__main__':
    app.config.from_object(config["development"])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(host="", port=9566)
