DNN_CPP 
=============================================

-------------------------------------------
DNN_CPPv2 Folder
-------------------------------------------

DNN_CPPv2:

Compile and run:

g++ DenseNeuralNetwork.cpp shapes.cpp -o shapes -O3

./shapes

Updates:
* Constructor accepts string argument for name of the loss function (as of now, that is “mean squared error” and “cross entropy”) and a vector of strings of the name of the activation functions (as of now, that is “linear”, “relu”, ”tanh”, “softmax”, and “logistic”)
* train() and test() method have been given an additional”isAccurate” parameter which is a function that accepts two vectors of doubles (the first argument being the predicted vector of the model, and the second vector being the correct output) and returns a boolean if the predicted vector correctly predicted the actual vector (or close enough). Yes, this puts more of a burden on the user. But there are so many metrics to test the “accuracy” of a model it is better if it is defined vs flooding the function body with if statements
* To account for the concern above, maxIndx() and zeroOrOne() was written as predefined static boolean function to measure accuracy. maxIndx() should be used if the output layer activation function is softmax and will return if the maximum value’s index of the predicted vector matches the maximum values index of the actual output. zeroOrOne() should be used if the output activation function is logistic and there is only one output node will return if the predicted output is closer to zero or one and compare that to the actual output
* Got rid of redundant code. Checking if activation functions are valid are checked multiple times when it only has to be checked once.  Still, a ton of redundant code exists, so future versions will hopefully have less of this
* Add generatingTriangle() method that generates right triangles
* Also fixed bounds of at the generateX() and generateSquare() method to where it won’t create super tiny Xs and squares
* Rewrote shapes.cpp to be a multi-classification problem with a softmax output layer. Training is not bad but very long (~85% accurate with testing data)
* moved delta arrays as an attribute of the class (this is used for updating the model, better to have it as an attribute vs allocating and deallocating the same memory 10,000 times)


Working on for v3 + Future Initiatives:
* Write file for mea squared error test. Not sure if DNN works for linear regression problems (it probably does)
* More loss functions
* More pre-defined accuracy functions
* Decrease time of execution (TensorFlow is WAY faster than this implementation, however, compiling with the -O3 flag reduces execution time significantly (cutting execution time over 1/2))
* Updating biases via back propagation (not just the weights). This is very important to do.
* Implement shapes.cpp in python and run this scenario on TensorFlow (closely mimicking the cpp implementation).
* Possibly implement the batch size hyperparameter.
* Add save option to store weights in a .txt file and read weights from a .txt file. [Will probably implement constructor or load() method or both that accepts a filename string as an argument, add save() method that saves all of the attributes of the model in a .txt file.
* Implement shuffling of data.



-------------------------------------------
DNN_CPPv1 Folder
-------------------------------------------

**Compile and run:**

g++ DenseNeuralNetwork.cpp shapes.cpp -o shapes

./shapes

**Short + Long:** 

Contains a DenseNeuralNetwork.h file that contains the overall structure of the DenseNeuralNetwork class,
a DenseNeuralNetwork.cpp file that implements the methods of the class, and a shapes.cpp file that randomly generates 
a vector of a vector of doubles that represents a square or an x. Each of the files has very specific documentation as to what each function/method does and the mathematics behind it. If the user does not care about the inner workings of the class, just view the .h file as it contains all of the methods the user can use and what each one does.

These shapes are then fed to a DenseNeuralNetwork object where it is asked to classify whether or not a given shape is an x 
or a square. The DenseNeuralNetwork uses gradient descent to update the weights (biases are always 0), 
the logistic activation function on every layer except the input layer, a learning rate of 0.01, 12 epochs, and binary cross-entropy as the loss function.  The model is ~84% accurate.


**Working on for v2:**

The user only has the ability to perform binary classification problems (the only loss function implemented is binary cross-entropy, and always uses logistic activation function on every layer). This means users cannot have more than 1 output layer, and cannot change any activation functions or the loss function (or serious errors would occur). The goal is to expand the class to perform computation for different types of problems. For example, regression problems (where activation functions like ReLU and a loss function like mean squared error are used) and multi-classification problems (activation functions like softmax, and a loss function like categorical cross-entropy).

**Future Initiatives:**
- In the Constructor, have users specify both a string that contains the name of the loss function being used and a vector of strings of what activation function to use on each layer (besides the input layer). [Easy to implement once I understand how each loss function and activation function works and what their corresponding partial derivatives are…]
- After this, add a generateTriangle() function to randomly create triangles and use the Neural Network for a multi-classification problem.
- Update shapes.cpp to prevent shapes from being created near the edge, or too small. Otherwise, shapes could be extremely small to where the DNN will always guess a low number (which is an x) and also look the same. For example, both generateX() and generateSquare() could create this shape anywhere on the grid:


OO\
OO

- Implement shapes.cpp in python and run this scenario on TensorFlow (closely mimicking the cpp implementation).
- Possibly implement the batch size hyperparameter.
- Add save option to store weights in a .txt file and read weights from a .txt file.
- Updating biases via back propagation (not just the weights).
- Implement shuffling of data.
