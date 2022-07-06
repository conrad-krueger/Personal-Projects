DNN_CPP 
=============================================

-------------------------------------------
DNN_CPPv3 Folder
-------------------------------------------
Compile and run:

g++ DenseNeuralNetwork.cpp shapes.cpp -o shapes -O3

./shapes


g++ DenseNeuralNetwork.cpp regress.cpp -o regress -O3

./regress

Updates:
* shuffle boolean parameter in train() function. Shuffles dataset
* save() and load() functions that save DenseNeuralNetwork information to a .txt file and read DenseNeuralNetwork information from a .txt file respectively. Also another constructor with just a string parameter was created to create DenseNeuralNetwork objects from .txt files
* Biases now update during backpropagation. 
* Added new attributes L (as the actual loss function), D_L (derivative of the Loss Function), activations (vector of actual activation functions), activationDerivatives (vector of functions that are derivatives of their corresponding activation function). It makes the code way more readable, with significantly less if-statements
* Wrote the derivatives of the activation functions relu, linear, tanh, softmax, and logistic as static functions in the class
* Wrote the functions and derivatives of the loss functions mean squared error (use) and cross entropy (cross_entropy) as static functions in the class
* regress.cpp updated to include a +5 biases and with noise which the model correctly identifies (bias = 4.5)
* shapes.cpp updated to save the model to a .txt file called “shapemodel.txt” so there is no need to retrain
* model.txt is sample of what the save() function will produce. 

Working on for v4:
Most of the major stuff has been completed. Now it is just minor improvements (except batch size).

Future Initiatives:
* More loss functions
* More pre-defined accuracy functions
* Decrease time of execution
* Implement shapes.cpp in python and run this scenario on TensorFlow (closely mimicking the cpp implementation).
* Possibly implement the batch size hyperparameter (thinking about using threads for this).

------------------
**UPDATE:** Added regress.cpp to DNN_CPPv2

Compile and run:

g++ DenseNeuralNetwork.cpp regress.cpp -o line -O3

./line

Used to simulate 2,000 data points between -10 and 10 and use 2 points and generate a label of 2x - 3y + noise. The architecture of the DNN is 2 input nodes and 1 output node. The .cpp file also prints the weights of the DNN before and after training). After only 5 epochs the weights are incredibly close to 2 and -3.

Note 1: Mimicked this article for demonstration https://www.analyticsvidhya.com/blog/2021/06/linear-regression-using-neural-networks/
Note 2: The accuracy function that was used per epoch was an inappropriate metric of accuracy. However, at the end of the cpp file, the test set was looped through again to develop a coefficient of determination which is more indicative of how the DNN is able to explain the linear relationship between the two input values and the output value. A coefficient of determination of 1 means a strong linear relationship. 0 is no linear relationship.

Thus, two very important things to work on for v3 are:
1. Update biases. Very important if the linear relationship does not go through the origin
2. Adapt the “accuracy” function to accept functions that must wait until the end of the epoch to make an accuracy claim (not on a data point by data point basis

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
* Moved delta pointer as an attribute of the class (this is used for updating the model, better to have it as an attribute vs allocating and deallocating the same memory 10,000 times)


Working on for v3 + Future Initiatives:
* [DONE. SEE UPDATE ABOVE] Write file for mean squared error test. Not sure if DNN works for linear regression problems (it probably does)
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
