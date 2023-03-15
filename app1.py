from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from config1 import config, Config
import requests
import json

from models.ModelUser import ModelUser

from models.entities.User import User

app = Flask(__name__)


csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)
URL = Config()


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


@app.route("/home", methods=["GET"])
@login_required
def home():
    try:
        url = URL.IP+"ingresos"
        url1 = URL.IP+"total_estudiantes"
        url2 = URL.IP+"inasistencia"
        url3 = URL.IP+"promedio"
        url4 = URL.IP+"l_ingresos"
        url5 = URL.IP+"estadisticas_grafico"
        datos = requests.get(url)
        datos1 = requests.get(url1)
        datos2 = requests.get(url2)
        datos3 = requests.get(url3)
        ingresos = requests.get(url4)
        estadisticasGraficos = requests.get(url5)
        data = datos.text
        data1 = datos1.text
        data2 = datos2.text
        data3 = datos3.text
        ingresos = ingresos.text
        estadisticasGraficos = estadisticasGraficos.text
        data = json.loads(data)
        data1 = json.loads(data1)
        data2 = json.loads(data2)
        data3 = json.loads(data3)
        ingresos = json.loads(ingresos)
        estadisticasGraficos = json.loads(estadisticasGraficos)
        print(data)
        print(data1)
        print(data2)
        print(data3)
        # print(ingresos)
        print(estadisticasGraficos)
        return render_template('home.html', count=data, count1=data1, count2=data2, count3=data3, listar=ingresos, ingresosGra=estadisticasGraficos)
    except Exception as ex:
        return jsonify({"mensaje": "Error", "Exito": ex})


# @app.route("/estadistica")
# def estadistica():
#     return render_template("estadistica.html")

@app.route("/estadisticas", methods=["GET"])
@login_required
def estadisticas_ingreso():
    try:
        url = URL.IP+"estadisticas"
        datos = requests.get(url)
        resultado = datos.text
        resultado = json.loads(resultado)
        print(resultado)
        return render_template('estadistica.html', ingresos=resultado)
    except Exception as ex:
        return jsonify({"mensaje": "Error", "Exito": ex})

# @app.route("/protected")
# @login_required
# def protected():
#     return "<h1>Esta es una vista protegida, solo para usuarios autenticados</h1>"


@app.route("/usuarios", methods=['GET'])
@login_required
def listar_usuarios():
    try:
        url = URL.IP+"usuarios"
        datos = requests.get(url)
        usuarios = datos.text
        usuarios = json.loads(usuarios)
        print(usuarios)
        return render_template('listar_usuarios.html', employee=usuarios)
    except Exception as ex:
        return jsonify({"mensaje": "Error", "Exito": ex})


@app.route("/l_ingresos", methods=['GET'])
@login_required
def listar_ingresos():
    try:
        url = URL.IP+"l_ingresos"
        datos = requests.get(url)
        ingresos = datos.text
        ingresos = json.loads(ingresos)
        print(ingresos)
        return render_template('listar_ingresos.html', listar=ingresos)
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


@app.route("/Registrar_Usuario")
def Registrar_Usuario():
    return render_template('Registrar_Usuario.html')


@app.route("/Registrar_Usuarios", methods=["POST"])
@login_required
def Registrar_usuarios():
    try:
        if request.method == "POST":
            url = URL.IP+"registrar_Usuario"
            data = request.form.to_dict()
            data.pop("csrf_token")
            datos = requests.post(url, json=data)
            msj = json.loads(datos.text)
            flash(msj["mensaje"])
        return render_template("Registrar_Usuario.html")
    except Exception as ex:
        return jsonify({"mensaje": ex, "Exito": False})


def status_401(error):
    return redirect(url_for("login"))


def status_404(error):
    return "<h1>Página no encontrada</h1>"


if __name__ == '__main__':
    app.config.from_object(config["development"])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(host="0.0.0.0", port=9566)
