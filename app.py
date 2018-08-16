from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    print('me executou pelo terminal')
    app.run(host='0.0.0.0', port=80)
else:
    print('me executou como um módulo')

        