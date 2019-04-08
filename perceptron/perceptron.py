import numpy as np
#from perceptron import Perceptron

class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
           
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activation = 1
        else:
          activation = 0            
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
        	#Simply backpropagation algorithm
            for inputs, label in zip(training_inputs, labels):
            #ZIP is used to group variables so that can be used together in for loop
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)



training_inputs = []
training_inputs.append(np.array([1, 1]))
training_inputs.append(np.array([1, 0]))
training_inputs.append(np.array([0, 1]))
training_inputs.append(np.array([0, 0]))

labels = np.array([1, 0, 0, 0])
perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)
print("MIMICKING AND GATE")
print("Input = " + str([1,1]) + " Output is " + str(perceptron.predict([1,1])))
print("Input = " + str([1,0]) + " Output is " + str(perceptron.predict([1,0])))
print("Input = " + str([0,1]) + " Output is " + str(perceptron.predict([0,1])))
print("Input = " + str([0,0]) + " Output is " + str(perceptron.predict([0,0])))

labels = np.array([0, 1, 1, 1])
perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)
print("MIMICKING NAND GATE")
print("Input = " + str([1,1]) + " Output is " + str(perceptron.predict([1,1])))
print("Input = " + str([1,0]) + " Output is " + str(perceptron.predict([1,0])))
print("Input = " + str([0,1]) + " Output is " + str(perceptron.predict([0,1])))
print("Input = " + str([0,0]) + " Output is " + str(perceptron.predict([0,0])))

labels = np.array([1,1,1,0])
perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)
print("MIMIKING OR GATE")
print("Input = " + str([1,1]) + " Output is " + str(perceptron.predict([1,1])))
print("Input = " + str([1,0]) + " Output is " + str(perceptron.predict([1,0])))
print("Input = " + str([0,1]) + " Output is " + str(perceptron.predict([0,1])))
print("Input = " + str([0,0]) + " Output is " + str(perceptron.predict([0,0])))

labels = np.array([0,0,0,1])
perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)
print("MIMIKING NOR GATE")
print("Input = " + str([1,1]) + " Output is " + str(perceptron.predict([1,1])))
print("Input = " + str([1,0]) + " Output is " + str(perceptron.predict([1,0])))
print("Input = " + str([0,1]) + " Output is " + str(perceptron.predict([0,1])))
print("Input = " + str([0,0]) + " Output is " + str(perceptron.predict([0,0])))

labels = np.array([0,1,1,0])
perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)
print("MIMIKING EXOR GATE")
print("Input = " + str([1,1]) + " Output is " + str(perceptron.predict([1,1])))
print("Input = " + str([1,0]) + " Output is " + str(perceptron.predict([1,0])))
print("Input = " + str([0,1]) + " Output is " + str(perceptron.predict([0,1])))
print("Input = " + str([0,0]) + " Output is " + str(perceptron.predict([0,0])))

labels = np.array([1,0,0,1])
perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)
print("MIMICKING EXNOR GATE")
print("Input = " + str([1,1]) + " Output is " + str(perceptron.predict([1,1])))
print("Input = " + str([1,0]) + " Output is " + str(perceptron.predict([1,0])))
print("Input = " + str([0,1]) + " Output is " + str(perceptron.predict([0,1])))
print("Input = " + str([0,0]) + " Output is " + str(perceptron.predict([0,0])))


