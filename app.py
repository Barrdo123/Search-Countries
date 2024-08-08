import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pais/<nome>')
def rota_pais(nome):
    resposta = requests.get(f'https://restcountries.com/v3.1/name/{nome}') 
    if resposta.status_code == 404:
        return "<h1>Pais não encontrado</h1>", 404
    return render_template('paises.html', paises=resposta.json())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/todos')
def rota_todos():
    resposta = requests.get(f'https://restcountries.com/v3.1/all')
    return render_template('paises.html', paises=resposta.json())


app.run(debug=True)