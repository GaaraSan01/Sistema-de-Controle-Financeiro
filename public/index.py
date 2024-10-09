from flask import Flask, jsonify
from src.controller.all_transacao import AllTransacao

app = Flask(__name__)

@app.route("/")
def index():
    content = AllTransacao()
    return content.handle()

if __name__ == '__main__':
    app.run(debug=True)