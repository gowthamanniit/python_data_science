import pandas as pd
df=pd.read_csv(open("D:/desktop/AI Training Content/multireg.csv","rb"))

x=df.iloc[:,:-1]
y=df.iloc[:,-1]


import numpy as np
x=np.array(x)
y=np.array(y)


from sklearn.impute import SimpleImputer
im=SimpleImputer()
x=im.fit_transform(x)   #rule: min 2D array


from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
x=sc.fit_transform(x)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y, test_size=0.2)


#now select the algo: as target is of continous type use regression algo: Linear Regression, RandomForest
# it works on equation of a line: y=bx+a     

#Types: Simple linear regression {1 input column: 1 output column} 2) Multi linear regression{more than 1 input and 1 output}.
  
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(xtrain,ytrain)
pred=lr.predict(xtest)

#for regression the evaluation method is completely different.
#1) visualization

xaxis=np.linspace(1,len(pred),len(pred))
import matplotlib.pyplot as plt
plt.plot(xaxis,pred,color='red')
plt.plot(xaxis,ytest,color='blue')
plt.show()

#2) how much good??? to define it in a number RMSE calculate
from sklearn.metrics import mean_squared_error
res=np.sqrt(mean_squared_error(pred,ytest))

print("Margin of error ",res)

