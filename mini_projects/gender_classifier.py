# Helps create decision trees
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# [height,weight,shoe-size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# Gender
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# Stores the decision tree model from sklearn
clf = tree.DecisionTreeClassifier()
clf2 = KNeighborsClassifier(n_neighbors = 2)
clf3 = QuadraticDiscriminantAnalysis()

# The result is stored in the updated clf variable
# fit method trains the decision tree on the dataset
clf = clf.fit(X,Y)
clf2 = clf2.fit(X,Y)
clf3 = clf3.fit(X,Y)

# DecisionTreeClassifier Predictions
# predict method gives a result based on the pretrained data-set.
pred = clf.predict([[175, 60, 38]])
# Prints female
print "DecisionTreeClassifier",pred
pred2 = clf.predict([[165, 70, 38]])
# Prints female
print "DecisionTreeClassifier",pred2

# KNeighborsClassifier Predictions
pred3 = clf2.predict([[175, 60, 38]])
# prints female
print "KNeighborsClassifier",pred3
pred4 = clf2.predict([[165, 70, 38]])
# prints male
print "KNeighborsClassifier",pred4

# QuadraticDiscriminantAnalysis Predictions
pred5 = clf3.predict([[175, 60, 38]])
# prints female
print "QuadraticDiscriminantAnalysis",pred5
pred6 = clf3.predict([[165, 70, 38]])
# prints male
print "QuadraticDiscriminantAnalysis",pred6
