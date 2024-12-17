from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    numeros = ["12000", "14000", "15940"]
    primos = [
        "el ultimo numero primo de 1200 es 11987",
        "el ultimo numero primo de 14000 es 13999",
        "el ultimo numero primo de 15940 es 15937"
    ]
    longitud = len(numeros)  # Calculo la longitud una sola vez
    return render_template('index.html', numeros=numeros, primos=primos, longitud=longitud)


