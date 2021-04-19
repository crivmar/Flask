## Importar modulos ##

from flask import Flask, render_template, abort
from lxml import etree

app = Flask(__name__)

## Rutas ##

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route ('/potencia', methods=['GET','POST'])
@app.route('/potencia/<int:base>/<exponente>', methods=['GET','POST'])
def potencia(base=0,exponente=0,resultado='no definido'):
    exponente2=int(exponente)
    if exponente2 >= 1:
        resultado = base**exponente2
    elif exponente2 == 0 and base >=1:
        resultado = 1
    elif exponente2 < 0:
        resultado = 1/base**(-exponente2)
    return render_template("potencia.html", b=base,e=exponente,r=resultado)

@app.route ('/cuenta', methods=['GET','POST'])
@app.route ('/cuenta/<palabra>/<letra>', methods=['GET','POST'])
def cuenta(palabra='@', letra="@",resultado='@'):
    if len(letra) ==1:
        resultado= palabra.count(letra)
    else:
        abort(404)
    return render_template ("cuenta.html",p=palabra,l=letra,r=resultado)

## Debug ##

app.run('0.0.0.0',debug=True)