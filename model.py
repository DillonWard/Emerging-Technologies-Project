# (1) Adapted from: https://keras.io/datasets/#mnist-database-of-handwritten-digits
# (2) Adapted from: https://datascience.stackexchange.com/questions/11704/reshaping-of-data-for-deep-learning-using-keras

# Neural network where the model for predictions will be trained and tested
# the model will be trained using the MNIST dataset and will try to recognize hand writting
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 03/12/2017

# import numpy so the datasets can be stored in arrays
import numpy as np

# import keras which will run on top of Tensorflow for additional functionalities
import keras as kr

# from keras import the mnist dataset that contains hand written numbers
# these images will be fed into our model to train it
from keras.datasets import mnist

# loads in the MNIST Dataset for training and testing the model - (1)
# 2 tuples for the model will be returned
# x_train, x_test: uint8 array of grayscale image data with shape (num_samples, 28, 28)
# y_train, y_test: uint8 array of digit labels (integers in range 0-9) with shape (num_samples,)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# (10000, 28, 28) (60000, 28, 28) (10000,) (60000,)
# print(x_test.shape, x_train.shape, y_test.shape, y_train.shape)

# the datasets are reshaped so that it can be fed into the model
# the reshape takes in the number of images and the size of the images - (2)
x_train = x_train.reshape(x_train.shape[0], 1, 28, 28).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 1,  28, 28).astype('float32')
