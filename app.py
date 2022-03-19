from flask import Flask
from api.route import route_api_nmap

app = Flask(__name__)
app.register_blueprint(blueprint=route_api_nmap.nmap_api)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
