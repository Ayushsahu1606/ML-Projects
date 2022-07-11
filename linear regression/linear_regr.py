from email.quoprimime import quote
from re import X
import numpy as np
import random 
import matplotlib.pyplot as plt

def stu_reg(x_train,y_train):
    from sklearn.linear_model import LinearRegression
    reg=LinearRegression()
    reg.fit(x_train,y_train)
    return reg 

x=[]
for ii in range(100):
    x.append(random.randrange(20,80))

y=[ii*6.25 + random.randrange(0,10) for ii in x]

x=np.array(x)
y=np.array(y)
x=x.reshape(len(x),1)
y=y.reshape(len(y),1)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y)
regg=stu_reg(x_train,y_train)

print('cofficient:',regg.coef_)

print('intercept:',regg.intercept_)

print('testing data : ',regg.score(x_test,y_test))
print('training data : ',regg.score(x_train,y_train))

plt.plot(x_train,y_train,':r')
plt.plot(x_test,regg.predict(x_test),'b')
plt.xlabel('x points')
plt.ylabel('y points')
plt.show()
