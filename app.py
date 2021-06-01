from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csfr = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Hello World"

@app.route("/bug")
def bad():
    try:
        raise TypeError()
    except TypeError as e:
        print(e)
    except TypeError as e:
        print("Duplicado.")


if __name__ == '__main__':
    app.run(debug=True)
