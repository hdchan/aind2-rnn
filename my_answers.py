import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs

    X = np.array([series[x : x + window_size] for x in range(0, len(series) - window_size)])
    y = np.array([series[x] for x in range(window_size, len(series)) ])
    
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    # print(sorted(set(text)))
    '''
    Sorted unique characters
    [' ', '!', '"', '$', '%', '&', "'", '(', ')', '*', ',', '-', '.', 
    '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', 
    '?', '@', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
    'y', 'z', 'à', 'â', 'è', 'é']
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
    'y', 'z']
    punctuation = ['!', ',', '.', ':', ';', '?']

    keep =  alphabet + punctuation
    remove = set(text).difference(set(keep))
    for idx, c in enumerate(list(remove)):
        text = text.replace(c,' ')
    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # print(text[:100], window_size, step_size)
    # containers for input/output pairs
    inputs = [text[x : x + window_size] for x in range(0, len(text) - window_size, step_size)]
    outputs = [text[x] for x in range(window_size, len(text), step_size) ]

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars, activation='softmax'))
    return model
