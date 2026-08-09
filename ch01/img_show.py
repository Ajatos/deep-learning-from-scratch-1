import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('cactus.png') # 이미지 읽어오기(적절한 경로를 설정하세요!)

plt.imshow(img)
plt.show()
# 옮긴이분의 깃허브에서 그대로 다운받아서 옴 
# 이미지(cactus.png) 출처: WegraLee, deep-learning-from-scratch (GitHub)
# https://github.com/WegraLee/deep-learning-from-scratch/tree/master/ch01/images