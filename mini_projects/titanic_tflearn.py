# VARIABLE DESCRIPTIONS:
# survived        Survived
#                 (0 = No; 1 = Yes)
# pclass          Passenger Class
#                 (1 = 1st; 2 = 2nd; 3 = 3rd)
# name            Name
# sex             Sex
# age             Age
# sibsp           Number of Siblings/Spouses Aboard
# parch           Number of Parents/Children Aboard
# ticket          Ticket Number
# fare            Passenger Fare

from __future__ import print_function

import numpy as np
import tflearn

# Downloading the titanic data-set from tflearn
from tflearn.datasets import titanic
titanic.download_dataset('titanic_dataset.csv')

# Loading the csv file
from tflearn.data_utils import load_csv
# load_csv loads data from a csv file to a python list
# target_column indicates that labels(survived or not) are located in the first column.
# The function returns a tuple (data, labels)
data, labels = load_csv('titanic_dataset.csv', target_column=0, categorical_labels=True, n_classes=2)
# print data
# print labels

# We first discard fields not important to the analysis("name" & "ticket" fields)
def preprocess(data, columns_to_ignore):
    # reverse = highest to lowest(descending id)
    for id in sorted(columns_to_ignore, reverse=True):
        # The columns that match the id are deleted.
        [r.pop(id) for r in data]
    for i in range(len(data)):
        # The sex field is converted to a float.
        data[i][1] = 1. if data[i][1] == 'female' else 0.
    return np.array(data, dtype=np.float32)

# The name and ticket columns are ignored(1 & 6 of the data_array)
to_ignore = [1,6]

# Now we run the preprocess function
data = preprocess(data, to_ignore)

# Training the three layer neural net.
# The shape of the input data is that it has a total of six features(none stands for an unknown dimension)
net = tflearn.input_data(shape=[None, 6])
# incoming is the tensor from the previous node, followed by the number of neurons in the layer
net = tflearn.fully_connected(net, 32)
# incoming is the tensor from the previous node, followed by the number of neurons in the layer
net = tflearn.fully_connected(net, 32)
# incoming is the tensor from the previous node, followed by the number of neurons in the layer
# An activation function is applied, in this case, a softmax.
# Softmax functions are implemented in the final layerof a classification centric NN.
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)

# Training
model = tflearn.DNN(net)
model.fit(data, labels, n_epoch=10, batch_size=20, show_metric=True)

# Test data
kelin = [1, 'Kelin Christi', 'male', 24, 0, 0, 'N/A', 5.00]
emma = [1, 'Emma Watson', 'female', 17, 1, 2, 'N/A', 100.00]

kelin, emma = preprocess([kelin, emma], to_ignore)

pred = model.predict([kelin, emma])
print("Kelins Chance of Survival:", pred[0][1])
print("Emmas Chance of Survival:", pred[1][1])

# RESULT
# Kelins Chance of Survival: 0.268235772848
# Emmas Chance of Survival: 0.87525421381
