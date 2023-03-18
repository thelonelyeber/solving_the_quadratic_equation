from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def solve():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])

    discr = b * b - 4 * a * c
    equation = f"{a}x^2+({b})x+({c})"

    if discr < 0:
        result = "Уравнение не имеет действительных корней."
    elif discr == 0:
        x = -b / (2 * a)
        result = "Уравнение имеет единственный корень: x = " + str(x)
    else:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        result = "Уравнение имеет два корня: x1 = " + str(x1) + ", x2 = " + str(x2)

    return render_template('index.html', result=result, equation=equation)


if __name__ == '__main__':
    app.run(debug=True)
