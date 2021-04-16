## Importar modulos ##

from flask import Flask, render_template, abort


app = Flask(__name__)

## Rutas ##

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

## Debug ##

app.run('0.0.0.0',debug=True)