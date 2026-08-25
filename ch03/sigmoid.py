import numpy as np #np라는 이름으로 numpy를 호출하겠다.
import matplotlib.pylab as plt 

def sigmoid(x): #매개변수 x를 가지는 sigmoid라는 이름의 함수를 선언하겠다.
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()