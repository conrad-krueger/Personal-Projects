Machine Learning
=============================================

This folder contains Machine Learning Architecture.

-------------------------------------------
DNN_CPP folder
-------------------------------------------
A folder that contains an implementation of a Dense Neural Network from scratch in C++.

Current Version: v3 [v3 documentation in DNN_CPP Folder]

-------------------------------------------
classifyEmAll.py (uses pkmn_img)
-------------------------------------------
Run:
First download pkmn_img folder. Edit lines 20-22 and 122, by typing the directory of the pkmn_img folder where
<INSERT DIRECTORY HERE> is seen.

python classifyEmAll.py

Uses a CNN with a pre-trained model (tf.keras.applications.MobileNetV2) to classify images of 3 starter Pokemon
(Bulbasaur, Charmander, Squirtle).
~90% accurate (depends on the device the program is ran on).

-------------------------------------------
stockPrediction.py (uses AMZN.csv)
-------------------------------------------
Run:

python stockPrediction.py

Uses a Long Short Term Memory Recurrent Neural Network to predict the trend of Amazon stock (AMZN.csv).
More extrapolation = significantly more inaccuracy.
 
-------------------------------------------
TF.ipynb
-------------------------------------------
Contains notes about basic TensorFlow commands and a brief introduction to different types of Machine Learning
Models, including Linear Regression, Markov Models, and Neural Networks (DNN, CNN, RNN).
These notes were compiled based on freecodecamp.org's "TensorFlow 2.0 Complete Course - Python Neural Networks
for Beginners Tutorial"


