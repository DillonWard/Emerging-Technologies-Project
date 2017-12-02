import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST'])

def uploadImage():
    print("here")
    data = request.get_data()
    print(data)
        

if __name__ == '__main__':
    app.run()