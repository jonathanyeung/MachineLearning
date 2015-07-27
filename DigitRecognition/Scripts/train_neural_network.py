import graphlab as gl
data = gl.SFrame('C:\Users\Jonathan\Documents\GitHub\MachineLearning\DigitRecognition\Data\\train_reduced.csv')

net = gl.deeplearning.create(data, target='label')

m = gl.neuralnet_classifier.create(data, target='label', network = net,max_iterations=30)

# Using the MSINT Default Network
mnist_net = gl.deeplearning.get_builtin_neuralnet('mnist')

m = gl.neuralnet_classifier.create(data, target='label', network = mnist_net,max_iterations=30)