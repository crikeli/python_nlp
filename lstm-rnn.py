import copy, numpy as np
np.random.seed(0)

# Sigmoid Linearity Activation function
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# The output of the sigmoid function is converted to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)

# Training data-set generation
int2binary = {}
binary_dim = 8

largest_number = pow(2, binary_dim)
binary = np.unpackbits(np.array([range(largest_number)], dtype=np.uint8).T, axis = 1)
for i in range(largest_number):
    int2binary[i] = binary[i]

# input vars
alpha = 0.1
input_dim = 2
hidden_dim = 16
output_dim = 1

# Neural Network weights get initialized
synapse0 = 2*np.random.random((input_dim, hidden_dim)) - 1
synapse1 = 2*np.random.random((hidden_dim, output_dim)) - 1
synapseh = 2*np.random.random((hidden_dim, hidden_dim)) - 1

synapse_0_update = np.zeros_like(synapse0)
synapse_1_update = np.zeros_like(synapse1)
synapse_h_update = np.zeros_like(synapseh)

# Logic for Training
for j in range(10000):
    # simple addition problem
    a_int = np.random.randint(largest_number/2) #integer version
    a = int2binary[a_int] #binary encoding

    b_int = np.random.randint(largest_number/2)
    b = int2binary[b_int] # binary encoding

    # actual answer
    c_int = a_int + b_int
    # integer is converted to binary
    c = int2binary[c_int]

    # Store best answer here
    d = np.zeros_like(c)

    overallError = 0

    layer_2_deltas = list()
    layer_1_values = list()
    layer_1_values.append(np.zeros(hidden_dim))

    # Moving along binary encoding positions
    for position in range(binary_dim):
        # Generate random inputs & outputs
        X = np.array([[a[binary_dim - position - 1], b[binary_dim - position - 1]]])
        y = np.array([[c[binary_dim - position - 1]]]).T

        # hidden layer (input ~+ prev_hidden)
        layer_1 = sigmoid(np.dot(X, synapse0) + np.dot(layer_1_values[-1], synapseh))

        # output layer
        layer_2 = sigmoid(np.dot(layer_1, synapse1))

        # Figuring out the error
        layer_2_error = y - layer_2
        layer_2_deltas.append((layer_2_error)*sigmoid_output_to_derivative(layer_2))
        overallError += np.abs(layer_2_error[0])

        # Decode estimate so we can print it.
        d[binary_dim - position - 1] = np.round(layer_2[0][0])

        # Storing hidden layer so it can be used in the next timestep
        layer_1_values.append(copy.deepcopy(layer_1))

    future_layer_1_delta = np.zeros(hidden_dim)

    for position in range(binary_dim):
        X = np.array([[a[position], b[position]]])
        layer_1 = layer_1_values[-position-1]
        prev_layer_1 = layer_1_values[-position-2]

        # Checking for the error at output layer
        layer_2_delta = layer_2_deltas[-position-1]
        # Checking for an error at the hidden layer
        layer_1_delta = (future_layer_1_delta.dot(synapseh.T) + layer_2_delta.dot(synapse1.T)) * sigmoid_output_to_derivative(layer_1)

        # Updating weights
        synapse_1_update += np.atleast_2d(layer_1).T.dot(layer_2_delta)
        synapse_h_update += np.atleast_2d(prev_layer_1).T.dot(layer_1_delta)
        synapse_0_update += X.T.dot(layer_1_delta)

        future_layer_1_delta = layer_1_delta

    synapse0 += synapse_0_update * alpha
    synapse1 += synapse_1_update * alpha
    synapseh += synapse_h_update * alpha

    synapse_0_update *= 0
    synapse_1_update *= 0
    synapse_h_update *= 0

    # Progress of the training is printed
    if (j % 1000 == 0):
        print "Error:" + str(overallError)
        print "Pred:" + str(d)
        print "True:" + str(c)
        out = 0

        for index, x in enumerate(reversed(d)):
            out += x*pow(2, index)
        print str(a_int) + " + " + str(b_int) + " = " + str(out)
        print "-------------"
