import numpy as np
import matplotlib.pylab as plt

def function_1(x): #매개변수 x를 가지는 이차함수 정의
    return 0.01*x**2 +0.1*x  #^가 아니라 **

x = np.arange(0.0,20.0, 0.1) #0부터 20까지 0.1간격
y = function_1(x) #함수안에 넣기

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()