# (1) Adapted from: https://keras.io/datasets/#mnist-database-of-handwritten-digits
# (2) Adapted from: https://datascience.stackexchange.com/questions/11704/reshaping-of-data-for-deep-learning-using-keras
# (3) Adapted from: https://github.com/DillonWard/Tensorflow-Worksheet/blob/master/Tensorflow-Worksheet.ipynb
# (4) Adapted from: https://github.com/fchollet/keras/issues/6351
# (5) Adapted from: https://towardsdatascience.com/exploring-activation-functions-for-neural-networks-73498da59b02

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


# (60000, 28, 28) (10000, 28, 28) (60000,) (10000,)
# print( x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# the datasets are reshaped so that it can be fed into the model
# the reshape takes in the number of images and the size of the images - (2)
# the images are then converted to floats
# ((x_train.shape[0] = 60000), (x_train.shape[1], x_train.shape[2] = 28, 28))
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2]).astype('float32')
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2]).astype('float32')

# currently, depending on the image, the input is 0 - 255
# 0 - 255 is taken from the pixels in the picture
# scale down the size of the pixels to be either 0 or 1 (true or false, there is or is not a pixel)
x_train = x_train/255
x_test = x_test/255

# the y or 'output' will be stored categorically
# they are encoded and stored as binary categorical variables - (3)
y_train = kr.utils.np_utils.to_categorical(y_train)
y_test = kr.utils.np_utils.to_categorical(y_test)

# create a model which will take in a list of layers or a 'linear stack of layers' - (3)
model = kr.models.Sequential()

# add 2 layers with input nodes - (3)
model.add(kr.layers.Dense(512, input_shape=(x_train.shape[1], x_train.shape[2])))

# reduces the dimensionality in the layers - (4)
model.add(kr.layers.Flatten())

# use the relu activation function - gradients (> 0) are set to 1,
# anything below 0 is set to 0 - (5)
model.add(kr.layers.Activation('relu'))

# adds the dropout layer to reduce overfitting onto the neural network
model.add(kr.layers.Dropout(0.2))

# add another layer, connected to the layer with 512 nodes, containing 10 output nodes - (3)
model.add(kr.layers.Dense(10))

# the softmax function squashes the outputs of each unit to be between 0 and 1 - (3)
model.add(kr.layers.Activation('softmax'))

# Configure the model for training. - (3)
# Uses the adam optimizer and categorical cross entropy as the loss function.
# Add in some extra metrics - accuracy being the only one. 
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Fit the model using our training data. - (3)
model.fit(x_train, y_train, batch_size = 128, epochs = 10, verbose = 1)

# Evaluate the model using the test data set. - (3)
loss, accuracy = model.evaluate(x_train, y_train, verbose=1)
print("\n\nLoss: %6.4f\tAccuracy: %6.4f" % (loss, accuracy))

# Predict the number.
prediction = np.around(model.predict(np.expand_dims(x_test[0], axis=0))).astype(np.int)[0]