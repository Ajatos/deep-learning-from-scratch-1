import numpy as np
import matplotlib.pyplot as plt
#pip install matplotlib -> pip(파이썬 패키지 관리자)에게 matplotlib을 인터넷에서 받아서 설치하라고 요청.
#데이터  준비
x = np.arange(0, 6, 0.1) #0에서 6까지 0.1 간격으로 생성
y = np.sin(x)

#그래프 그리기
plt.plot(x, y)
plt.show()

#y/r sin 함수.