import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.python.framework.ops import disable_eager_execution

disable_eager_execution()

dataset = pd.read_csv('13.csv')

#print(dataset.TradePrice)

dataset2 = dataset[dataset['Type'] == 'Pre-owned Condominiums, etc.']
dataset3 = dataset2[dataset2['Purpose'] == 'House']
final_dataset = dataset3[dataset3['Renovation'] == 'Not yet']

target = np.array(final_dataset.TradePrice)

final_dataset = final_dataset.drop('TradePrice', axis=1)
final_dataset = final_dataset.drop('Type', axis=1)
final_dataset = final_dataset.drop('Purpose', axis=1)
final_dataset = final_dataset.drop('Renovation', axis=1)
final_dataset = final_dataset.drop('Prefecture', axis=1)
final_dataset = final_dataset.drop('Municipality', axis=1)
final_dataset = final_dataset.drop('MunicipalityCode', axis=1)
final_dataset = final_dataset.drop('DistrictName', axis=1)
final_dataset = final_dataset.drop('FloorPlan', axis=1)
final_dataset = final_dataset.drop('FrontageIsGreaterFlag', axis=1)
final_dataset = final_dataset.drop('BuildingYear', axis=1)
final_dataset = final_dataset.drop('Structure', axis=1)
final_dataset = final_dataset.drop('Use', axis=1)
final_dataset = final_dataset.drop('CityPlanning', axis=1)
final_dataset = final_dataset.drop('Period', axis=1)
final_dataset = final_dataset.drop('UnitPrice', axis=1)
final_dataset = final_dataset.drop('PricePerTsubo', axis=1)
final_dataset = final_dataset.drop('LandShape', axis=1)
final_dataset = final_dataset.drop('Frontage', axis=1)
final_dataset = final_dataset.drop('TotalFloorArea', axis=1)
final_dataset = final_dataset.drop('Direction', axis=1)
final_dataset = final_dataset.drop('Classification', axis=1)
final_dataset = final_dataset.drop('Breadth', axis=1)
final_dataset = final_dataset.drop('Remarks', axis=1)
final_dataset = final_dataset.drop('Region', axis=1)
final_dataset = final_dataset.drop('No', axis=1)
final_dataset = final_dataset.drop('NearestStation', axis=1)
final_dataset = final_dataset.drop('TimeToNearestStation', axis=1)
final_dataset = final_dataset.drop('MinTimeToNearestStation', axis=1)
final_dataset = final_dataset.drop('MaxTimeToNearestStation', axis=1)
final_dataset = final_dataset.drop('FloorAreaRatio', axis=1)
final_dataset = final_dataset.drop('AreaIsGreaterFlag', axis=1)
final_dataset = final_dataset.drop('TotalFloorAreaIsGreaterFlag', axis=1)
final_dataset = final_dataset.drop('CoverageRatio', axis=1)


feature = np.array(final_dataset)



#print(final_dataset)
#print(feature[0:1])
#print(target[0:1])
'''
        Area  PrewarBuilding  Year  Quarter
0         30               0  2019        3
6         35               0  2018        4
7         20               0  2018        3
9         30               0  2018        2
10        70               0  2018        2
...      ...             ...   ...      ...
358368    20               0  2015        3
358406    20               0  2014        3
358449    40               0  2017        1
358722    80               0  2013        4
367886    60               0  2013        3

[45118 rows x 4 columns]
[[  30    0 2019    3]]
[40000000]
'''

def norm(data): #正規化
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data - mean)/std

feature = norm(feature)
#print(feature)


#rint(feature.shape)

ones = np.ones((45118, 1))

feature = np.c_[ones, feature]

#print(feature.shape)


feature_train, feature_test, target_train, target_test = train_test_split(feature, target, test_size=0.2, random_state=42)
target_train = target_train.reshape(36094,1)
target_test = target_test.reshape(9024, 1)

#print(feature_train.shape)
#print(target_train.shape)
#print(feature_test.shape)
#print(target_test.shape)
'''
(36094, 5)
(36094, 1)
(9024, 5)
(9024, 1)
'''


#前処理終了

#学習率
learning_rate = 0.01
#エポック数
epochs = 100

n_dim = feature.shape[1]

#tf.compat.v1.disable_eager_execution()

X = tf.compat.v1.placeholder(tf.float32, [None,n_dim])
Y = tf.compat.v1.placeholder(tf.float32,[None,1])

W = tf.Variable(tf.ones([n_dim,1]))
b = tf.Variable(0.0)

y = tf.add(b, tf.matmul(X, W))

loss = tf.reduce_mean(tf.square(y-Y))

#training_step = tf.optimizers.SGD(learning_rate).minimize(lossg, var_list = [W, b])
#training_step = tf.SGD(learning_rate).minimize(lossg)
#training_step = tf.keras.optimizers.SGD(learning_rate).minimize(loss, var_list=W)
training_step = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(loss)
        
ini = tf.compat.v1.global_variables_initializer()

ses = tf.compat.v1.Session()
ses.run(ini)

loss_history = []

for epoch in range(epochs):
    ses.run(training_step, feed_dict={X:feature_train, Y:target_train})
    loss_history = np.append(loss_history, ses.run(loss, feed_dict={X:feature_train, Y:target_train}))
    if epoch % 100 == 0:
        W_val = ses.run(W)
        b_val = ses.run(b)

print(loss_history[1])
print(loss_history[10])
print(loss_history[50])
print(loss_history[99])
'''
i1919076481892352.0
1305362699386880.0
691152042852352.0
643262821957632.0
減少していることを確認
'''

pred_test = ses


