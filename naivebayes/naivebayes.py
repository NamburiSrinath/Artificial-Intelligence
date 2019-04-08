import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
 
# &amp;amp;nbsp;
 
dataset = datasets.load_iris()

model = GaussianNB()
model.fit(dataset.data, dataset.target)

expected = dataset.target
#print(dataset.data)
predicted = model.predict(dataset.data)

print("Precision, recall values")
print(metrics.classification_report(expected, predicted))
print("Confusion matrix")
print(metrics.confusion_matrix(expected, predicted))

unique, counts = np.unique(expected, return_counts = True)
print("Expected counts")
print(unique, counts)

matrix = (expected == predicted)
for i in range (150):
	if(matrix[i] == False):
		print("Location of mismatch " + str(i))

print("Number of non equal cases " + str(np.sum(predicted != expected)) + " out of 150")

unique_predicted, counts_predicted = np.unique(predicted, return_counts = True)
print("Predicted counts...Though the number is same, some are misclassified")
print(unique_predicted, counts_predicted)

#print(dataset.data[52],dataset.data[70],dataset.data[77], dataset.data[106], dataset.data[119], dataset.data[133])
print("For 52 expected and predicted are " + str(expected[52]) + " and " + str(predicted[52]))
print("For 70 expected and predicted are " + str(expected[70]) + " and " + str(predicted[70]))
print("For 77 expected and predicted are " + str(expected[77]) + " and " + str(predicted[77]))
print("For 106 expected and predicted are " + str(expected[106]) + " and " + str(predicted[106]))
print("For 119 expected and predicted are " + str(expected[119]) + " and " + str(predicted[119]))
print("For 133 expected and predicted are " + str(expected[133]) + " and " + str(predicted[133]))
A = [[7,3,5,1]]
print("A = " + str(A) + " and 52 index is " + str(dataset.data[52]) + " and the predicted is " + str(model.predict(A)))