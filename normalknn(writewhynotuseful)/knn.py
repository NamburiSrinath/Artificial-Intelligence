#KNN for this dataset wont give good results as a general cluster cannot be visualised. So, demonstrate this to differentiate between Linear 
#regression and KNN and the importance of Algorithm vs dataset


#Load all the libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
from sklearn.datasets import load_boston

#load dataset and assign a variable
boston_dataset = load_boston()
#Using Pandas dataframes to access data/columns
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)

#boston.head(). Used to print first 5 rows
#Give the target variable. Not given in dataset
boston['MEDV'] = boston_dataset.target

#Taken onlythe most important features. Determined from HEATMAPS in linearregression.py
X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns = ['LSTAT', 'RM'])
Y = boston['MEDV']

#split data as 80,20. Random state is similar to seed number generation in random number generator
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)#5 is just arbitrary
Y_trainnew = Y_train.astype(int)
Y_testnew = Y_test.astype(int)
#print(Y_trainnew[0:])

# Train the model using the training sets
model.fit(X_train,Y_trainnew)

#Predict Output
Y_predicted= model.predict(X_test) 
print(Y_predicted)
Y_testnew = np.array(Y_testnew)
print(Y_testnew)

print("Number of non equal cases " + str(np.sum(Y_predicted != Y_testnew)) + " out of 102")

from sklearn import metrics
# Model Accuracy
print("Accuracy: ",metrics.accuracy_score(Y_testnew, Y_predicted))



