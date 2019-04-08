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
columns = ['LSTAT', 'RM']
X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns = ['LSTAT', 'RM'])
Y = boston['MEDV']

Y = Y/25

for i in range (506):
	if(Y[i] == 2):
		Y[i] = 1

#split data as 80,20. Random state is similar to seed number generation in random number generator
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)

Y_trainnew = Y_train.astype(int)
Y_testnew = Y_test.astype(int)
# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=2)

# Train Decision Tree Classifer
clf = clf.fit(X_train,Y_trainnew)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(Y_testnew, y_pred))
print(np.sum(Y_trainnew == 1))

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = columns,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('boston.png')
Image(graph.create_png())