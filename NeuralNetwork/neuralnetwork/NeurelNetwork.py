#!/usr/bin/env python  
# -*-coding:utf-8-*-
# 神经网络的实现方法

import numpy as np


# 定义双曲函数
def tanh(x):
    return np.tanh(x)


# 双曲线求导
def tanh_deriv(x):
    return 1.0 - np.tanh(x) * np.tanh(x)


# 逻辑函数
def logistic(x):
    return 1 / (1 + np.exp(-x))


# 求导
def logistic_derivative(x):
    return logistic(x) * (1 - logistic(x))


class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv
        self.weights = []
        # 初始化权重
        for i in range(1, len(layers) - 1):
            self.weights.append((2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1) * 0.25)
            self.weights.append((2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1) * 0.25)

    def fit(self, X, y, learning_rate=0.2, epochs=10000):
        # 每次随机抽取epochs个实例
        X = np.atleast_2d(X)
        temp = np.ones([X.shape[0], X.shape[1] + 1])
        temp[:, 0:-1] = X
        X = temp
        # bias初值
        y = np.array(y)

        for k in range(epochs):
            # 随机抽取每行
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            # 更新的实例
            # 正向更新
            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            error = y[i] - a[-1]  # 反向传送最后一个错误率
            deltas = [error * self.activation_deriv(a[-1])]
            # 输出层Errj=Oj(1-Oj)(Tj-Oj)
            # 根据误差反向传送
            # 隐藏层
            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.activation_deriv(a[l]))
            deltas.reverse()
            # 更新权重
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a

# if __name__ == '__main__':
#     nn = NeuralNetwork([2, 2, 1], 'tanh')
#     # 算法集
#     X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#
#     y = np.array([0, 1, 1, 0])
#     nn.fit(X, y)
#     for i in [[0, 0], [0, 1], [1, 0], [1, 1]]:
#         print(i, nn.predict(i))