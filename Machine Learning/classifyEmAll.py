# Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image
import glob
import cv2
keras = tf.keras


pkmn = []
label = []
test_pkmn = []
test_label = []

starterPkmn = ["Bulbasaur","Squirtle","Charmander"]

#CHANGE THESE TO CORRECT DIRECTORY
bLoc = r'<INSERT DIRECTORY HERE>\pkmn_img\Bulbasaur\*'
cLoc = r'<INSERT DIRECTORY HERE>\pkmn_img\Charmander\*'
sLoc = r'<INSERT DIRECTORY HERE>\pkmn_img\Squirtle\*'

allLoc=[bLoc,sLoc,cLoc]

b = np.array([1,0,0])
s = np.array([0,1,0])
c = np.array([0,0,1])

tracker = 0
for x in range(len(starterPkmn)):
    poke = starterPkmn[x]
    direct = allLoc[x]
    loaded = 0
    

    print("Currently on:",poke)
    for filename in glob.glob(direct):
        try:
            im=Image.open(filename)
            npim = np.asarray(im)
            npim = cv2.resize(npim, dsize=(160, 160), interpolation=cv2.INTER_CUBIC)
            if (npim.shape != (160,160,3)): continue

            tracker += 1
            if (tracker%7 == 0):
                test_pkmn.append(npim)
                if (poke == "Bulbasaur"): test_label.append(b)
                if (poke == "Squirtle"): test_label.append(s)
                if (poke == "Charmander"): test_label.append(c)
                continue

            pkmn.append(np.asarray(npim))
            #rotation
            pkmn.append(cv2.resize(np.asarray(im.rotate(45)), dsize=(160, 160), interpolation=cv2.INTER_CUBIC))
            pkmn.append(cv2.resize(np.asarray(im.rotate(90)), dsize=(160, 160), interpolation=cv2.INTER_CUBIC))
            pkmn.append(cv2.resize(np.asarray(im.rotate(270)), dsize=(160, 160), interpolation=cv2.INTER_CUBIC))
            pkmn.append(cv2.resize(np.asarray(im.rotate(180)), dsize=(160, 160), interpolation=cv2.INTER_CUBIC))
            pkmn.append(cv2.resize(np.asarray(im.rotate(25)), dsize=(160, 160), interpolation=cv2.INTER_CUBIC))
            pkmn.append(cv2.resize(np.asarray(im.rotate(75)), dsize=(160, 160), interpolation=cv2.INTER_CUBIC))
            loaded += 7
            for x in range(7):
                if (poke == "Bulbasaur"): label.append(b)
                if (poke == "Squirtle"): label.append(s)
                if (poke == "Charmander"): label.append(c)
        except Exception: 
            print("ERROR Loading:", filename)
        
    print("LOADED:",loaded)

print(len(pkmn))
train_feature = np.array(pkmn)
train_label = np.array(label)

test_feature = np.array(test_pkmn)
test_label = np.array(test_label)

print("Training Data Size:",len(train_feature),len(train_label))
print("Testing Data Size:",len(test_feature),len(test_label))

"""# Training NN"""

mobileNet = tf.keras.applications.MobileNetV2(input_shape=(160,160,3),include_top=False, weights='imagenet') 
#mobileNet.summary()


##FREEZING THE BASE##
mobileNet.trainable = False



##PUT MODEL TOGETHER##
model = tf.keras.Sequential([
  mobileNet,
  keras.layers.GlobalAveragePooling2D(),
  keras.layers.Dense(3, activation="softmax")
])


##COMPILE MODEL##

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.CategoricalCrossentropy(), 
              metrics=['accuracy'])



##TRAIN MODEL##

history = model.fit(train_feature, train_label, epochs=8,shuffle=True,batch_size=32)

model.save("ClassifyEmAll.h5")

#Evaluate
model.evaluate(test_feature,test_label)

"""# Testing NN"""

pkmn = []
npPkmn = []
#model = tf.keras.models.load_model('ClassifyEmAllv4.h5')
for filename in glob.glob(r'<INSERT DIRECTORY HERE>\pkmn_img\TEST\*'):
    try:
        im=Image.open(filename)
        pkmn.append(im)
    except Exception:
        print("ERROR Loading:", filename)

for x in pkmn:
    npPkmn.append(np.asarray(x))

test = []
for x in range(len(npPkmn)):
    IMG_SIZE = 160
    image = cv2.resize(npPkmn[x], dsize=(160, 160), interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    #plt.imshow(image)
    #plt.show(block=True)
    test.append(np.array([image]))

    
for inst in test:
    
    prediction=model.predict(np.array(inst))[0]
    choice = np.argmax(prediction)

    print("Model Predicts:",starterPkmn[choice])
    plt.imshow(inst[0])
    plt.show(block=True)
    
    print(prediction)
    print()
    

#[Bulbasaur % ,Squirtle %, Charmander %]

