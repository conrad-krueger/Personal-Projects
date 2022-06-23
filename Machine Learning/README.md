Machine Learning
=============================================

This folder contains Machine Learning Architecture.

-------------------------------------------
classifyEmAll.py (uses pkmn_img)
-------------------------------------------
Run:
First download pkmn_img folder. Edit lines 20-22 and 122, by typing the directory of the pkmn_img folder where
<INSERT DIRECTORY HERE> is seen.
python classifyEmAll.py

Uses a CNN with a pre-trained model (tf.keras.applications.MobileNetV2) to classify images of 3 starter Pokemon
(Bulbasaur, Charmander, Squirtle).
~ 89% accurate.

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

-------------------------------------------
cyberAtkData.ipynb
-------------------------------------------
This project attempts to develop a Dense Neural Network that is able to predict the type of an attack (or if there is no attack) based on the following attributes from the NSL-KDD Dataset:

['protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate']

As of now, I have created a neural network that uses every single one of these attributes as a numeric input node
(with little preprocessing) and has generated an 85.1% accurate model on the test data and a 98.76% accurate
model on the training data on only 3 epochs.

List of attacks: ['normal' (no attack), 'neptune', 'warezclient', 'ipsweep', 'portsweep', 'teardrop', 'nmap', 'satan', 'smurf', 'pod', 'back', 'guess_passwd', 'ftp_write', 'multihop', 'rootkit', 'buffer_overflow', 'imap', 'warezmaster', 'phf', 'land', 'loadmodule', 'spy', 'perl']
