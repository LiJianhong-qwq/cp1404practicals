from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world() :  # put application's code here
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<qwq>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/c/<fahrenheit>')
def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    return str(celsius)


@app.route('/f/<celsius>')
def convert_to_fahrenheit(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return str(fahrenheit)


if __name__ == '__main__' :
    app.run()
