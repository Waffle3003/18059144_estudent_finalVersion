import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas import DataFrame as df
import matplotlib.pylab as plt
from sklearn.ensemble import RandomForestRegressor
from matplotlib.pylab import rcParams
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#reading the csv amd ordering by months
dataRead = pd.read_csv(r'C:\Users\mhila\Desktop\estudent_app\3yeardata.csv')
data = dataRead.sort_values('month_int')
print(data)

#making the date field into datetime and setting it as the index
data['edit_date_savings'] = pd.to_datetime(data['edit_date_savings'], infer_datetime_format=True)
newData = data.set_index(['edit_date_savings'])
newData.head()

plt.xlabel('Date')
plt.ylabel('Saved that month')
#x = newData['edit_date_savings']

#plotting a graph of monthly leftovers from savings
y = newData['total_left_savings']
plt.plot(y)

x1 = newData['savings_budget']
x2 = newData['month_int']
x3 = newData['savings_used']
x3 = newData['savings_used'] = newData['savings_used'].astype(int)

y = newData['total_left_savings']

x1 = np.array(x1)
x2 = np.array(x2)
x3 = np.array(x3)
y = np.array(y)

#single column reshape
x1 = x1.reshape(-1,1)
x2 = x2.reshape(-1,1)
x3 = x3.reshape(-1,1)

y = y.reshape(-1,1)
z = np.concatenate((x1, x2, x3), axis = 1)
print(z)
print(y)

mymodel = RandomForestRegressor(n_estimators=150, max_features=3, random_state=5)
linReg = LinearRegression()
x_train = z[:-24]
x_test = z[-24:]
y_train = y[:-24]
y_test = y[-24:]

mymodel.fit(x_train, np.ravel(y_train))
linReg.fit(x_train, np.ravel(y_train))

linReg.get_params()

prediction = mymodel.predict(x_test)
plt.rcParams['figure.figsize'] = (16,8)
plt.plot(prediction, label = 'Predicted Savings')
plt.plot(y_test, label = 'Actual Savings')
plt.xlabel('month')
plt.ylabel('saved')
plt.legend(loc = 'lower left')
plt.show()

linearPrediction = linReg.predict(x_test)
plt.rcParams['figure.figsize'] = (16,8)
plt.plot(linearPrediction, label = 'Predicted Savings')
plt.plot(y_test, label = 'Actual Savings')
plt.xlabel('month')
plt.ylabel('saved')
plt.legend(loc = 'lower left')
plt.show()

randForest = sqrt(mean_squared_error(prediction, y_test))
liReg = sqrt(mean_squared_error(linearPrediction, y_test))
print(randForest)
print(liReg)