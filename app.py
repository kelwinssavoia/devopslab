from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csfr = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Atividade Kelwin Sanches Savoia"


if __name__ == '__main__':
    app.run(debug=True)
