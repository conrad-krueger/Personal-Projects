import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("AMZN.csv")

#data preproccessing
df['Date'] = pd.to_datetime(df['Date'])
df.shape

temp = df.loc[3000:5880]

plt.plot(temp['Date'],temp['Close'])

all_feat = temp.filter(['Close']).values

all_feat1 = all_feat
#scalar = MinMaxScaler(feature_range=(0,1))
#all_feat = scalar.fit_transform(all_feat)
all_feat /= 10000

#80% of data will train
train_feat = []
train_label = []
train_lim = int(len(all_feat)*.85)+1
days = 80

for x in range(days,train_lim):
  train_feat.append(all_feat[x-days:x])
  train_label.append(all_feat[x])

test_feat = []
test_label= []
for x in range(train_lim + days,len(all_feat)):
  test_feat.append(all_feat[x-days:x])
  test_label.append(all_feat[x])


train_feat = np.array(train_feat)
train_label = np.array(train_label)
test_feat = np.array(test_feat)
test_label = np.array(test_label)

print(test_feat.shape)


#build model

model = tf.keras.Sequential()
model.add(tf.keras.layers.LSTM(50,return_sequences=True,input_shape=(days,1)))
model.add(tf.keras.layers.LSTM(50,return_sequences=False))
model.add(tf.keras.layers.Dense(25))
model.add(tf.keras.layers.Dense(1))

model.compile(optimizer='adam',loss='mean_squared_error')

model.fit(train_feat,train_label,epochs=1,batch_size=4)


results = model.predict(test_feat)

#results = scalar.inverse_transform(results)

rmse=np.sqrt(np.mean(((results- test_label)**2)))


plt.style.use('fivethirtyeight')
plt.figure(2)
plt.xlabel("Date")
plt.ylabel("Close")
plt.plot(all_feat*10000,label="Entire Graph")
plt.plot(all_feat1[:train_lim],label="Actual")
xs = np.array([x for x in range(2550,2901)])
xs=xs.reshape(351,1)
plt.plot(xs,results*10000,label="Predicted")
plt.legend()
plt.xlim([2500,3000])

plt.show(block=True)
