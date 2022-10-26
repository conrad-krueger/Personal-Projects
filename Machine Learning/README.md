Machine Learning
=============================================

This folder contains Machine Learning Architecture.

-------------------------------------------
DNN_CPP folder
-------------------------------------------
A folder that contains an implementation of a Dense Neural Network from scratch in C++.

Current Version: v4 [v4 documentation coming soon]

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
TF.ipynb
-------------------------------------------
Contains notes about basic TensorFlow commands and a brief introduction to different types of Machine Learning
Models, including Linear Regression, Markov Models, and Neural Networks (DNN, CNN, RNN).
These notes were compiled based on freecodecamp.org's "TensorFlow 2.0 Complete Course - Python Neural Networks
for Beginners Tutorial"

-------------------------------------------
Stock_with_LSTM.py
-------------------------------------------

Short: This program experiments with and inevitably concludes a Long-Short-Term-Memory Recurrent Neural Network Architecture in this YouTube video (https://www.youtube.com/watch?v=QIUxPv5PJOY&t=2199s) is not fully capable of predicting stock prices (at least when it comes to making extrapolations in the not-so-far future).

Long: A YouTube video with almost 1 million views (https://www.youtube.com/watch?v=QIUxPv5PJOY&t=2199s) attempts to show how an LSTM RNN is capable of predicting stock prices. While the video flags viewers from using this model to make any financial advice, I argue that this model is very inaccurate even if one attempts to predict the stock value only a few days in the future.
This file will:
 
1. Recreate the model in the video with Amazon stock
 
2. Show why the model is inaccurate 
 
3. Create 2 functions to allow testing of the model with different hyperparameters with ease. This is in hopes of potentially getting the model to be more accurate as the model could potentially be overfitting the data in the video
