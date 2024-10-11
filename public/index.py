from flask import Flask
from src.controller.all_transacao import AllTransacao

app = Flask(__name__)

@app.route("/")
def index():
    conteudo = AllTransacao()
    return conteudo.handle()

if __name__ == '__main__':
    app.run(debug=True)