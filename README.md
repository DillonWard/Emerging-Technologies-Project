# Emerging Technologies Project
###### *Dillon Ward - G00326756 - Emerging Technologies*
---

## Introduction
The following repository contains a Single Page Web Application for a fourth-year undergraduate project for the module Graph Theory. The module is taught to undergraduate students at GMIT in the Department of Computer Science and Applied Physics. The lecturer is Ian McLoughlin.

## Prerequisites
* [git](https://git-scm.com/)
* [Python](https://www.python.org/downloads/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Anaconda](https://anaconda.org/)
* [Flask](http://flask.pocoo.org/)

## Cloning this Repository
To clone this repository and run the solutions, do the following:

```
In the command line change to a directory:
cd <directory>

Clone the repository:
git clone https://github.com/DillonWard/Emerging-Technologies-Project.git

Change directory into the cloned folder:
cd <folder name>

Run the program:
py setup.py
```

## Tensorflow
### What is Tensorflow?
[TensorFlow](https://en.wikipedia.org/wiki/TensorFlow) is an open-source software library for dataflow programming across a range of tasks. It is a symbolic math library, and also used for machine learning applications such as neural networks.

It was originally developed by the Google Brain Team within Google's Machine Intelligence research organization for machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well.

TensorFlow is cross-platform. It runs on nearly everything: GPUs and CPUs—including mobile and embedded platforms—and even tensor processing units, which are specialized hardware to do tensor math on.

### What is Tensorflow used for?
Tensorflow has an multiple uses, such as image recognition, human language, and linear models. See the [Tensorflow Tutorials](https://www.tensorflow.org/tutorials/) for more details.

### [Installation](https://stackoverflow.com/a/42129546/8394648)
```
conda create --name tensorflow python=3.6
activate tensorflow
conda install jupyter
conda install scipy
pip install tensorflow-gpu

```
## Keras
### What is Keras?
[Keras](https://keras.io/) is a neural networks programming framework written in Python that is used for simplifying of creating deep learning applicaitons. Rather than Keras providing all of the functionalities itself, it's ran on top of Tensorflow, CNTK, or Theano and adds a simplified interface.

### What is Keras used for?
Use Keras if you need a deep learning library that:

* Allows for prototyping through a user friendly interface
* Supports convolutional networks, recurrent networks, or a combination of both.
* Runs seamlessly on CPU and GPU.

### Installation
```
pip install h5py # used for saving modules
pip install keras
```

## Anaconda
### What is Anaconda?
[Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)) is an open source distribution for Python and R programming languages, used for large-scale data processing, predictive analytics, and scientific computing, and aims to simplify package management and deployment. Anaconda aims to provide users with everything they need to get started with data science.

### Installation
To download and install Anaconda, head over to the Anaconda [Installation Section](https://conda.io/docs/user-guide/install/index.html) on their website.
* [Anaconda for Windows](https://conda.io/docs/user-guide/install/windows.html)
* [Anaconda for macOS](https://conda.io/docs/user-guide/install/macos.html)
* [Anaconda for Linux](https://conda.io/docs/user-guide/install/linux.html)

## Flask
### What is Flask?
[Flask](http://flask.pocoo.org/) is a small web framework that is designed to support the development of web applications with Python. Flask provides the user with tools, libraries, and technologies that allow you to build data driven web applications.
### Installation
````
pip install flask
````

## Project Overview
### Specifications
1. Create a Single-Page Web Application w/ Flask.
2. Allow the user to draw an image containing a single digit
3. The image containing the digit will be sent to the server
3. Send a response to the user with the digit contained in the image

# Architecture
### [Setup](https://raw.githubusercontent.com/DillonWard/Emerging-Technologies-Project/master/setup.py)

`setup.py` is our script that will setup our environment and run the application for us.

First it will check if a folder called 'images' already exists. If that folder doesn't exist, create the folder - this folder is where our images that will be sent to the server will be stored. The same is done for our 'data' folder where our model will be saved.
Next, the node modules for the design of the application is generated.
Finally, the server is started and the application is being hosted locally.
```
if not os.path.exists('./images'):
    os.mkdir('./images') 

if not os.path.exists('./data'):
    os.mkdir('./data') 

os.system('npm install')

os.system('py server.py')
```

### [Server](https://raw.githubusercontent.com/DillonWard/Emerging-Technologies-Project/master/server.py)
`server.py` is our back-end that will host out `index.html` file, convert and resize the images fed in from the 'front-end', and make predictions about what the digit in the image is.

***For a more detailed explanation of each of the following functions, you can check the solution that has been commented***.
#### Imports
`flask` will be imported for creating our API and using some of the functionalities that comes along with flask, such as `request` for taking in data from the front-end.
`re` and `base64` will be used once we read in the data taken from the image sent to the server. `re` will use regular-expressions to strip some of the text read in. `base64` is used to decode the encoded string.
`numpy` is imported for handling and manipulating arrays.
`imread` is imported for reading in images from files and `imresize` is used for resizing the the bytes that are read in from the image file, compressing it. Finally, `keras` is used for loading in our previously trained model. We also import `os` for suppressing warnings from Tensorflow, though it isn't necessary. 

```
import flask
from flask import Flask, request
import re, base64
import numpy as np
from scipy.misc import imread, imresize
import keras as kr
```
#### Home Route
First, we set up our Home Route that will return our `index.html` when the user is on the `/` route.
```
@app.route('/')
def home():
    return app.send_static_file('index.html')
```

#### Upload Route
The upload route is the route that will be called by the front-end to upload the image to the server. The upload route has 2 functions, `uploadImage` which is used for taking in the image, compressing/converting the image, and predicting what the digit inside the image is. The `uploadImage` function will take the request sent from the front-end and read in the data passed back. The, the necessary data we need is stripped using regular expressions and the encoded string is decoded.

Next, the image is converted to grayscale to ensure our model can read it and the array the now decoded string is in is inverted and the image is resized to 28 * 28.

Finally, the array is "flattened" which returns a copy of the array collapsed into one dimension, and is passed into the `newPredict` function.

```
@app.route('/upload', methods=['POST'])
def uploadImage():
    data = request.get_data()
    img = re.search(b'base64,(.*)', data).group(1)

    with open('./images/uploaded-img.png','wb') as fh:
        fh.write(base64.b64decode(img))
    
    img_bytes = imread('./images/uploaded-img.png', mode ='L')
    img_bytes = np.invert(img_bytes)
    img_bytes = imresize(img_bytes, (28,28))

    new_predict = np.ndarray.flatten(np.array(img_bytes)).reshape(1, 28, 28).astype('float32')
    new_predict = new_predict / 255
    pred = newPredict(new_predict)
    return pred
```

The other function is the `newPredict` which takes in the converted file. First, the model that was previously trained is loaded in with keras and the image is fed into the model. Then, the response or prediction is returned to the `uploadImage` function that will return the prediction to the front-end.

```
def newPredict(f):
    model = kr.models.load_model("./data/prediction_model.h5")
    prediction = model.predict(f)
    response = np.array_str(np.argmax(prediction))
    return response
```


## References
* [Wikipedia - Tensorflow](https://en.wikipedia.org/wiki/TensorFlow)
* [Tensorflow Tutorials](https://www.tensorflow.org/tutorials/)
* [Keras](https://keras.io/)
* [Lynda - What is Keras?](https://www.lynda.com/Google-TensorFlow-tutorials/What-Keras/601801/642171-4.html)
* [Anaconda](https://anaconda.org/)
* [Anaconda Installation](https://anaconda.org/)