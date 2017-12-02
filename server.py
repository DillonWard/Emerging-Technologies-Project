# (1) Adapted from - https://stackoverflow.com/questions/25045373/use-regex-re-sub-to-remove-everything-before-and-including-a-specified-word
import flask
from flask import Flask, request
import re, base64

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST'])

def uploadImage():
    data = request.get_data()
    # use regular expressions to remove or everything before a specific character - (1)
    img = re.search(b'base64,(.*)', data).group(1)


    with open('./images/uploaded-img.png','wb') as fh:
        fh.write(base64.b64decode(img))

    return 'Uploaded'

if __name__ == '__main__':
    app.run()