import numpy as np
import matplotlib.pyplot as plt

#데이터 준비
x = np.arange(0, 6, 0.1) #0부터 6까지 0.1간격으로 생성
y1 = np.sin(x) #x의 모든 원소의 sin값을 그대로 y에 넣기.
y2 = np.cos(x) #cos버전.

#그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")  #cos 함수는 점선으로 그리기 #센스ㅋㅋㅋ.
plt.xlabel("x")        # x축 이름
plt.ylabel("y")        # y축 이름
plt.title('sin & cos') # 제목
plt.legend()           #레전드 ㄷㄷ.
plt.show()

#왜 내가 아는거랑 다른가 했더니 라디안이었으..