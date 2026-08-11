import numpy as np #numpy를 np로 불러오기
import matplotlib.pylab as plt # 맷플롯립중 파이랩을 plt로 불러오기

def step_function(x): #계단식 함수 함수 정의
    return np.array(x > 0, dtype=int) # np배열로 반환, x > 0을 조건으로 bool로 나타내고 이를 int로 변환

x = np.arange(-5.0, 5.0, 0.1) #넘파이 배열(-5.0부터 5.0(마지막이 4.9)까지 0.1 간격으로 건너뛴 것)
y = step_function(x) #x를 계단식 함수에 넣어서 갈아만든x를 만드는 것(브로드캐스트로 원콤에)
plt.plot(x, y) #plot의 x값을 x y값을 y로
plt.ylim(-0.1, 1.1) #이게 뭐지?? -> y값을 -0.1부터 1.1까지 보여주라는 거
plt.show() #소환