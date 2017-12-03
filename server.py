# (1) - Adapted from: https://stackoverflow.com/a/25487483/8394648
# (2) - Adapted from: https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imread.html
# (3) - Adapted from: https://uk.mathworks.com/help/images/ref/imresize.html

# Server for manipulating data that's passed in from the 'front-end'
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 01/12/2017

# Import flask for creating our API and using some of its functionalities
import flask

# takes in requests from the web application
from flask import Flask, request, jsonify

# import re or 'regular expressions' for filtering text
# import base64 for encoding images to extract binary data
import re, base64

# import numpy to for handling arrays
import numpy as np

# import 'imread' for reading in images
# import 'imresize' for resizing and returning images
from scipy.misc import imread, imresize

# import keras to load the previously generated model
import keras as kr

# supress warnings from tensorflow
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

app = Flask(__name__)

# sets up the 'home' route 
@app.route('/')
def home():
    # returns the template 'index' when the user is on this route
    return app.send_static_file('index.html')

# route for POSTing images to the server
# image is uploaded and converted here
@app.route('/upload', methods=['POST'])
def uploadImage():
    # data is read in from the request made to the server 
    # the image source is read in an and stored in 'data'
    data = request.get_data()

    # use regular expressions to remove what we don't need from what's being read in - (1)
    # everything read in up until 'base64,' is removed - the rest is stored in 'img'
    img = re.search(b'base64,(.*)', data).group(1)

    # stores the images in the below directory
    # the data that was filtered using the reg-exp is decoded using base64
    with open('./images/uploaded-img.png','wb') as fh:
        fh.write(base64.b64decode(img))
    

    # the images is read in from the file as an array
    # the image is converted to greyscale, mode 'L' converts it to 8-bit pixels, black and white - (2)
    img_bytes = imread('./images/uploaded-img.png', mode ='L')
    # inverts the arrays that the integers are stored in 
    img_bytes = np.invert(img_bytes)
    # resizes the image bytes size to 28 rows and cols - (3)
    img_bytes = imresize(img_bytes, (28,28))

    new_predict = np.ndarray.flatten(np.array(img_bytes)).reshape(1, 28, 28).astype('float32')
    new_predict = new_predict / 255
    pred = newPredict(new_predict)

    '''
        # Used for testing to see the output of the image being converted
        for i in img_bytes:
            for j in i:
                if (j <= 127):
                    print('.', end='')

                else:
                    print ('#', end='')
            print() 
    '''
    # returns the predicted number to the webapp
    return pred

def newPredict(f):

    # the model that was saved previously is loaded in
    model = kr.models.load_model("./data/prediction_model.h5")
    
    # make a prediction with the model
    prediction = model.predict(f)

    # Return a string representation of the data in an array
    response = np.array_str(np.argmax(prediction))
    return response


if __name__ == '__main__':
    app.run() # runs the application