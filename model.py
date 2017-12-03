import numpy as np
import keras as kr
from keras.datasets import mnist


(train_input, train_output), (test_input, test_output) = mnist.load_data()

print(train_input.shape, test_input.shape)
