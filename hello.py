from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_method():
    data = [1,2,3,45,6]
    return render_template('hello.html', data=data)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)