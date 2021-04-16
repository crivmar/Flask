## Importar modulos ##

from flask import Flask, render_template, abort


app = Flask(__name__)

## Rutas ##

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route ('/potencia', methods=['GET','POST'])
@app.route('/potencia/base/exponente', methods=['GET','POST'])
def potencia(base=0,exponente=0):
    if exponente >=1:
        resultado = base**exponente
    elif exponente =0:
        resultado= 1
    elif exponente < 0:
        resultado= 1/(base**exponente)
    return render_template("potencia.html", b=base,e=exponente,r=resultado)

## Debug ##

app.run('0.0.0.0',debug=True)