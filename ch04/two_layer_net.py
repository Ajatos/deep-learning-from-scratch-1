#드디어 드디어 드디어 신경망 학습

#1단계 미니배치
#훈련 데이터중 일부를 무작위로 가져오기

#2단계 기울기 산출
#각 가중치 매개변수의 기울기 구하기

#3단계 매개변수 갱신
#가중치 매개변수를 기울기 방향으로 아주 조금 움직이기

#4단계 
#1-3 반복

#역전파 포함해도 이렇게인가??


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from common.functions import *
from common.gradient import numerical_gradient

class TwoLayerNet: #2층 신경망
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        #가중치 초기화하기
        self.params = {} #빈 딕셔너리 생성
        self.params['W1'] = weight_init_std * \
                            np.random.randn(input_size,hidden_size) #입력층 은닉층 랜덤
        self.params['b1'] = np.zeros(hidden_size) # 은닉층 영벡터로

        self.params['W2'] = weight_init_std * \
                                    np.random.randn(hidden_size,output_size) #마찬가지
        self.params['b2'] = np.zeros(output_size)

    def predict(self,x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x,W1) +b1 #입력층에 가중치 행렬곱하고 편향 더하기
        z1 = sigmoid(a1) #시그모이드 함수에 넣어서 비선형이되도록 바꾸기
        a2 = np.dot(z1, W2) + b2 # 시그모이드에 넣은거랑 가중치2 행렬곱하고 편향 더하기
        y = softmax(a2) #소프트맥스에 넣어서 확률화

        return y 

    def loss(self, x, t):
        y = self.predict(x)

        return cross_entropy_error(y,t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    #x:입력 데이터 t:정답 레이블
    def numerical_gradient(self,x,t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        
        return grads