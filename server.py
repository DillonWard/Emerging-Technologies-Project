import flask
from flask import Flask, request
import re, base64
import numpy as np
from scipy.misc import imread, imresize

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST'])

def uploadImage():
    data = request.get_data()
    # use regular expressions to remove what we don't need from what's being read in
    img = re.search(b'base64,(.*)', data).group(1)

    # the image is decoded using base64 and saved
    with open('./images/uploaded-img.png','wb') as fh:
        fh.write(base64.b64decode(img))
    
    img_bytes = imread('./images/uploaded-img.png', mode ='L')
    img = np.invert(img_bytes)
    img_bytes = imresize(img_bytes, (28,28))

    for i in img_bytes:
        for j in i:
            if (j <= 127):
                print('.', end='')

            else:
                print ('#', end='')
        print()


    return 'Uploaded'

if __name__ == '__main__':
    app.run()