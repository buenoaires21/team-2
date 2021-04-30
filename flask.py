from flask import Flask
import sqlobject as SO

PUERTO = int(os.environ.get('PORT', 5000))


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#connection =  SO.connectionForURI("postgres://thzsdadoufayxv:53207294de51bffb638d3e4b01ebecca459317bdf0f251d6ae2a6fc6d5e41609@ec2-54-84-238-74.compute-1.amazonaws.com:5432/d340nsj63nu9qe")


if __name__ == "__main__":
    app.run(debug=True)
