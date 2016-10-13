# NN Trained on city names, and generate new city names.
# Future link between python 2 & 3

from __future__ import absolute_import, division, print_function

# important to read data on the pc
import os
from six import moves
import ssl
# Machine learning library dependent on tensor flow
import tflearn
from tflearn.data_utils import *

# Retrieve the city names.
path = "US_Cities.txt"
if not os.path.isfile(path):
    # Initializes key & proxy managers as we will retrieve external data
    context = ssl._create_unverified_context()
    # Retrieval of data from the url
    moves.urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt", path, context=context)

# The maximum length of the city name
maxlen = 20

# # # Vectorizing text (abstracting data)
# # # X = Input(words)
# # # Y = Target(vectors)
# # # char_idx = dictionary of the input & target
X, Y, char_idx = textfile_to_semi_redundant_sequences(path, seq_maxlen=maxlen, redun_step=3)

# Input layer of the NN
g = tflearn.input_data(shape=[None, maxlen, len(char_idx)])
# 512 neurons in this layer.
g = tflearn.lstm(g, 512, return_seq=True)
# To avoid overfitting(trained model won't work for new data), we dropout(randomly turning off nodes so different neurons can be utilized)
g = tflearn.dropout(g, 0.5)
g = tflearn.lstm(g, 512)
g = tflearn.dropout(g, 0.5)
# softmax a logistic regression useful for classification.
g = tflearn.fully_connected(g, len(char_idx), activation='softmax')
g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
                       learning_rate=0.001)

# Generating City Names
m = tflearn.SequenceGenerator(g, dictionary=char_idx,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,
                              checkpoint_path='model_us_cities')

# Training the Network
for i in range(40):
    seed = random_sequence_from_textfile(path, maxlen)
    m.fit(X, Y, validation_set=0.1, batch_size=128,
          n_epoch=1, run_id='us_cities')
    print("TESTING")
    print(m.generate(30, temperature=1.2, seq_seed=seed))
    print(m.generate(30, temperature=1.0, seq_seed=seed))
    print(m.generate(30, temperature=0.5, seq_seed=seed))
