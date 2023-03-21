from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/nuestrosaliados')
def nuestrosaliados():
   return render_template('nuestrosaliados.html')

@app.route('/quienessomos')
def quienessomos():
    return render_template('quienessomos.html')

@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')

@app.route('/solucionesyservicios')
def solucionesyservicios():
    return render_template('solucionesyservicios.html')

@app.route('/infraestructura')
def infraestructura():
    return render_template('infraestructura.html')

@app.route('/seguridad')
def seguridad():
    return render_template('seguridad.html')

@app.route('/conectividad')
def conectividad():
    return render_template('conectividad.html')

@app.route('/soporteyservicios')
def soporteyservicios():
    return render_template('soporteyservicios.html')


if __name__=='__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
    