import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)  #5

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)

#아니 왜이렇게 쓸게많아!!!!!!!!!!