
from flask import Flask, jsonify
import glob
import re

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return Flask

@app.route('/page1')
def page1():
    return "Если вы это читаете, \
                     вы что-то знаете :)"

@app.route('/configs')
def configs():
    L = glob.glob('C:\\Users\\ds.kottsov\\Desktop\\test_config\\config_files\\*.txt')
    d_id = 'hostname '
    i = ''
    R = ''
    for name in L:
        with open(name) as f:
            for L in f:
                if d_id in L:
                    i = i+L
    return i


if __name__ == '__main__':
    app.run(debug=True)