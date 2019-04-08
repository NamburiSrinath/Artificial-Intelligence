import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()

# create X (features) and y (response)

# X features are width and height of sepals and petals
#Y feature says which flower it is
X = iris.data
y = iris.target

#Use these to debug if errors come
#print(type(X))

#print(X[:,0])
#print(y.shape)
#print("Number of 0's " + str(np.sum(y == 0)) + " and no's of 1's are " + str(np.sum(y ==1)) + " no of 2's are " + str(np.sum(y == 2)))

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

#Below lines use complete set for training thus giving trivial solution/overfitting. So we need to divide into train/test data 
#Or train with entire dataset and give user data. Right now it is commented 

# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X, y)
# y_pred = knn.predict(X)
# print(metrics.accuracy_score(y, y_pred))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

#Use this if any errors regarding shapes
# print("Train X shape " + str(X_train.shape))
# print("Train Y shape " + str(y_train.shape))
# print("Test X shape " + str(X_test.shape))
# print("Test Y shape " + str(y_test.shape))

plt.subplot(2,2,1)
plt.scatter(X[:,0], y, marker = 'o')
plt.xlabel("Feature 0")
plt.ylabel("Y")
plt.title("Plot between one feature and output")
plt.subplot(2,2,2)
plt.scatter(X[:,1], y, marker = 'o')
plt.xlabel("Feature 1")
plt.ylabel("Y")
plt.title("Plot between one feature and output")
plt.subplot(2,2,3)
plt.scatter(X[:,2], y, marker = 'o')
plt.xlabel("Feature 2")
plt.ylabel("Y")
plt.title("Plot between one feature and output")
plt.subplot(2,2,4)
plt.scatter(X[:,3], y, marker = 'o')
plt.xlabel("Feature 3")
plt.ylabel("Y")
plt.title("Plot between one feature and output")
plt.show()

k_range = range(1, 26)
# Create Python dictionary using [] or dict()
scores = []

#Use for loop to determine max accuracy for which K 
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))
print("Scores are ")
print(scores)
print("And the max index is there for ")
K_max = scores.index(max(scores))
print(K_max)
print("So, use that as K and now give some test inputs to check your clustering model")
knn = KNeighborsClassifier(n_neighbors= K_max)
knn.fit(X_train, y_train)

plt.plot(k_range, scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')
plt.show()

print("An example input and output from train set to cross verify " + str(X_train[0]) + " ---> " +str(y_train[0]))
print("An example input and output from test set to cross verify " + str(X_test[0]) + " ---> " +str(y_test[0]))
input = np.array([[4.3,3.2,1.2,0.15],[6.2,2.7,5.45,1.9]])
input = input[:,np.newaxis]
print("User inputs are " + str(input[0]) + "  " + str(input[1]))


print("For input 0 prediction is "+ str(knn.predict(input[0])) + " and for input 1 it is "+ str(knn.predict(input[1])))