import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #
from dataset.mnist import load_mnist #

(x_train, t_train), (x_test,t_test) = \
    load_mnist(flatten = True, normalize = False)  #

print(x_train.shape)  #  (60000,784)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)