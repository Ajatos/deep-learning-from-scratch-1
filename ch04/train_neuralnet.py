import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정하는걸 까먹어서 한참 해맴
import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True) #normalize로 이미지의 픽셀값을 0.0-1.0으로 정규화하고 원 핫 배열로 받기

train_loss_list = []
train_acc_list = []
test_acc_list = []

#하이퍼파라미터(!!)
iters_num = 10000 #반복 횟수
train_size = x_train.shape[0]
batch_size = 100 #미니배치 크기ㅣㅣ
learning_rate = 0.1

#1에포크당 반복수(이거 빼먹음;;)
iter_per_epoch = max(train_size / batch_size, 1)

network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)

for i in range(iters_num): #반복문 안에 안넣었음;;;
     #마나배치 뽑기
     batch_mask = np.random.choice(train_size, batch_size)
     x_batch = x_train[batch_mask]
     t_batch = t_train[batch_mask]

     #기울기 구하기
     grad = network.numerical_gradient(x_batch,t_batch)
     #grad = network.gradient(x_batch,t_batch) #성능 개선판      이라고 책에 써있었음

     #매개변수
     for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    #학습 경과 기록
     loss = network.loss(x_batch, t_batch)
     train_loss_list.append(loss)

    #1 에포크당 정확도 계산
     if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc =network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc :" + str(train_acc) + ", "+str(test_acc))