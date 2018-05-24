#!/usr/bin/env python
# -*-coding:utf-8-*-
# 手写数字的识别 神经网络算法,利用写好的神经网络算法测试
import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import LabelBinarizer
from neuralnetwork import NeuralNetwork
from sklearn.cross_validation import train_test_split

digits = load_digits()
X = digits.data
y = digits.target
# 特征值 0 1之间
X -= X.min()
X /= X.max()
# 归一化

#数据集中的图片为8*8的所以输入层为64，输出10个数是哪个数，所以10个
nn = NeuralNetwork([64, 100, 10], 'logistic')
#将数据集分成训练还有测试
X_train, X_test, y_train, y_test = train_test_split(X, y)
labels_train = LabelBinarizer().fit_transform(y_train)
labels_test = LabelBinarizer().fit_transform(y_test)
# 转化为01，
print('start fitting')
nn.fit(X_train, labels_train, epochs=3000)
predictions = []
for i in range(X_test.shape[0]):
    o = nn.predict(X_test[i])
    predictions.append(np.argmax(o))
#
print(confusion_matrix(y_test, predictions))
# 正确度
print(classification_report(y_test, predictions))
