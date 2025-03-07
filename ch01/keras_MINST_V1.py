from keras.models import Sequential
model = Sequential()
model.add(Dense(12, input_dim=8, kernel_initializer='random_uniform'))

from __future__ import print_function
import numpy as np
from keras.datasets import mnist
form keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from keras.utils import np_utils

np.random.seed(1671)

NB_EPOCH = 200
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10
OPTIMIZER = SGD()
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2

(X_train, y_train), (X_test, y_test) = mnist.load_data()
RESHAPED = 784

X_train = X_train.reshape(60000, RESHAPED)
X_test = X_test.reshape(10000, RESHAPED)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

Y_train = np_utils.to_categorical(y_train, NB_CLASSES)
Y_test = np_utils.to_categorical(y_test, NB_CLASSES)

model = Sequential()
model.add(Dense(NB_CLASSES, input_shape=(RESHAPED, )))

model.add(Activation('softmax'))
model.summary()



import os
from time import gmtime, strftime
from keras.callbacks import TensorBoard

def make_tensorboard(set_dir_name=''):
    tictoc=strftime("%a_%d_%b_%Y_%H_%M_%S", gmtime())
    directory_name = tictoc
    log_dir = set_dir_name + '_' + directory_name
    os.mkdir(log_dir)
    tensorboard = TensorBoard(log_dir=log_dir)
    return tensorboard

callbacks = [make_tensorboard(set_dir_name='keras_MINST_VI')]

model.compile(loss='categorical_crossentropy' ,optimizer=OPTIMIZER, metrics=['accuracy'])

model.fit(X_train, Y_train,
batch_size=BATCH_SIZE, epochs=NB_EPOCH,
callbacks=callbacks,
verbose=VERBOSE, validation_split=VALIDATION_SPLIT)













