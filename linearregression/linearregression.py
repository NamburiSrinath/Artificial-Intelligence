#Import all libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
from sklearn.datasets import load_boston

#load dataset and assign variable
boston_dataset = load_boston()
#Print what all are the attreibutes/features in dataset
print(boston_dataset.keys())

boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
#boston.head()
#target missing in dataset. So assign manually
boston['MEDV'] = boston_dataset.target

#print(boston.isnull().sum())

#This is used to see corrlations and pick the most important ones. Visualise in HEATMAPS
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(boston['MEDV'], bins=30)
plt.show()

correlation_matrix = boston.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
#plt.show()

plt.figure(figsize=(20, 5))

features = ['LSTAT', 'RM']
target = boston['MEDV']

#plot the most important features
for i, col in enumerate(features):
    plt.subplot(1, len(features) , i+1)
    x = boston[col]
    y = target
    plt.scatter(x, y, marker='o')
    plt.title(col)
    plt.xlabel(col)
plt.ylabel('MEDV')
plt.show()

X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns = ['LSTAT', 'RM'])
Y = boston['MEDV']

#print(X['LSTAT'])
#print(Y)

#split data as 80,20. Random state is similar to seed number generation in random number generator
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)
print("Train data shape is, X_train " + str(X_train.shape))
print("Test data shape, X_test " +str(X_test.shape))
print("Train output shape, Y_train " + str(Y_train.shape))
print("Test output output " +str(Y_test.shape))

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
#LinearRegression() is the function which has gradient descent, predicting and all the attributes
lin_model = LinearRegression()
#Curve fitting
lin_model.fit(X_train, Y_train)
y_train_predict = lin_model.predict(X_train)

#Root mean square error and R2 score
rmse = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
r2 = r2_score(Y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

# model evaluation for testing set
y_test_predict = lin_model.predict(X_test)
rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))
r2 = r2_score(Y_test, y_test_predict)


print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

print("Coefficients are {}. How many features, those many coefficients. beta0 assumed as inherent constant".format(lin_model.coef_))

print("The equation will be beta0 + " + str(lin_model.coef_[0]) + "*x + " +str(lin_model.coef_[1]) + "*x^2")

# Plot outputs
plt.subplot(2,2,1)
plt.scatter(X_train['LSTAT'], Y_train,  color='black')
plt.scatter(X_train['LSTAT'], y_train_predict, color='blue')
plt.xticks(())
plt.yticks(())
plt.title('LSAT for train data')
plt.xlabel('LSAT feature')
plt.ylabel('MEDV feature')

plt.subplot(2,2,2)
plt.scatter(X_test['LSTAT'], Y_test,  color='black')
plt.scatter(X_test['LSTAT'], y_test_predict, color='blue')
plt.xticks(())
plt.yticks(())
plt.title('LSAT for test data')
plt.xlabel('LSAT feature')
plt.ylabel('MEDV feature')
#plt.show()

plt.subplot(2,2,3)
plt.scatter(X_train['RM'], Y_train,  color='black')
plt.scatter(X_train['RM'], y_train_predict, color='blue')
plt.xticks(())
plt.yticks(())
plt.title('RM for train data')
plt.xlabel('RM feature')
plt.ylabel('MEDV feature')

plt.subplot(2,2,4)
plt.scatter(X_test['RM'], Y_test,  color='black')
plt.scatter(X_test['RM'], y_test_predict, color='blue')
plt.xticks(())
plt.yticks(())
plt.title('RM for test data')
plt.xlabel('RM feature')
plt.ylabel('MEDV feature')
plt.show()








