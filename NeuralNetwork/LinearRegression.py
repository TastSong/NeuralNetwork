#!/usr/bin/env python  #恶心的导入模块的方法，python2与3的导入方式不同
# -*-coding:utf-8-*-
# 神经网络测试的例子
# 简单非线性关系数据集测试(XOR)异或的运算
from neuralnetwork import NeuralNetwork
import numpy as np

nn = NeuralNetwork([2, 2, 1], 'tanh')
# 算法集
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

y = np.array([0, 1, 1, 0])
nn.fit(X, y)
for i in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    print(i, nn.predict(i))