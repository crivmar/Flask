## Importar modulos ##

from flask import Flask, render_template, abort


app = Flask(__name__)

## Rutas ##

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route ('/potencia', methods=['GET','POST'])
@app.route('/potencia/<int:base>/<int:exponente>', methods=['GET','POST'])
def potencia(base=0,exponente=0,resultado='no definido'):
    if exponente >= 1:
        resultado = base**exponente
    elif exponente == 0 and base >=1:
        resultado = 1
    elif exponente < 0:
        resultado = 1/base**exponente
    return render_template("potencia.html", b=base,e=exponente,r=resultado)

@app.route ('/cuenta',methods=['GET','POST'])
@app route ('/cuenta/<palabra>/<letra>',methods=['GET','POST'])


## Debug ##

app.run('0.0.0.0',debug=True)