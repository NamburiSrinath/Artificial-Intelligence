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
Y = Y/25

for i in range (506):
	if(Y[i] == 2):
		Y[i] = 1

#split data as 80,20. Random state is similar to seed number generation in random number generator
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)

Y_trainnew = Y_train.astype(int)
Y_testnew = Y_test.astype(int)
# X_trainnew = X_train.astype(int)
# X_testnew = X_test.astype(int)
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()
#print("...." + str(type(X_train)) + str(type(Y_train)))

# fit the model with data
logreg.fit(X_train,Y_trainnew)

#
y_pred=logreg.predict(X_test)
#print(y_pred, Y_testnew)
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(Y_testnew, y_pred)
#print(cnf_matrix.shape)

sns.heatmap(data=cnf_matrix, annot=True)
plt.show()

print("Accuracy:",metrics.accuracy_score(Y_testnew, y_pred))
print("Precision:",metrics.precision_score(Y_testnew, y_pred))
print("Recall or True Positive Rate:",metrics.recall_score(Y_testnew, y_pred))

y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(Y_testnew,  y_pred_proba)
auc = metrics.roc_auc_score(Y_testnew, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('Receiver Operating Characteristics Curve')
plt.show()


