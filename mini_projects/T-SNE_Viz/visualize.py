import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import sklearn
import matplotlib.pyplot as plt

dataframe_all = pd.read_csv("https://d396qusza40orc.cloudfront.net/predmachlearn/pml-training.csv")
# print type(dataframe_all)
num_rows = dataframe_all.shape[0]
# print "num rows",num_rows

# Cleaning Data
counter_nan = dataframe_all.isnull().sum()
# print "counter_nan",counter_nan
counter_without_nan = counter_nan[counter_nan==0]
# print "counter_without_nan", counter_without_nan

dataframe_all = dataframe_all[counter_without_nan.keys()]
# remove the first 7 columns which contain no discriminative information
dataframe_all = dataframe_all.ix[:,7:]
# the list of columns (the last column is the class label)
columns = dataframe_all.columns
# print columns

# Retrieving features of the data and scaling the features.
# Converting features to numpy array

x = dataframe_all.ix[:, :-1].values
standard_scaler = StandardScaler()
x_std = standard_scaler.fit_transform(x)

# Getting class labels y and encoding it into a number
# Getting class label data
y = dataframe_all.ix[:,-1].values
# Encoding class label
class_labels = np.unique(y)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

test_percentage = 0.1
x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=test_percentage, random_state=0)
# t distributed Stochastic Neighbor Embedding (t-SNE) visualization
from sklearn.manifold import TSNE
tsne = TSNE(n_components = 2, random_state=0)
x_test_2d = tsne.fit_transform(x_test)

# scatter plot the sample points among 5 classes
markers=('s', 'd', 'o', '^', 'v')
color_map = {0:'red', 1:'blue', 2:'lightgreen', 3:'purple', 4:'cyan'}
plt.figure()
for idx, cl in enumerate(np.unique(y_test)):
    plt.scatter(x=x_test_2d[y_test==cl,0], y=x_test_2d[y_test==cl,1], c=color_map[idx], marker=markers[idx], label=cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc='upper left')
plt.title('t-SNE visualization of test data')
plt.show()
