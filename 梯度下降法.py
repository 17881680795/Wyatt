# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-04-19
# @FileName: 梯度下降法.py
import numpy as np


def gradient_descent(X, y, alpha=0.01, max_iters=1000, tol=1e-4):
    """
    使用梯度下降法训练线性回归模型

    参数：
    X: ndarray, 特征矩阵，形状为 (m, n)，m 为样本数，n 为特征数
    y: ndarray, 目标变量，形状为 (m, )
    alpha: float, 学习率，默认为 0.01
    max_iters: int, 最大迭代次数，默认为 1000
    tol: float, 收敛阈值，默认为 1e-4

    返回：
    theta: ndarray, 训练得到的参数向量，形状为 (n, )
    J_history: list, 每次迭代损失函数的值
    """
    m, n = X.shape
    theta = np.zeros(n)
    J_history = []

    for i in range(max_iters):
        # 计算梯度
        delta = 1 / m * np.dot(X.T, np.dot(X, theta) - y)
        # 更新参数
        theta -= alpha * delta

        # 计算损失函数
        J = 1 / (2 * m) * np.sum((np.dot(X, theta) - y) ** 2)
        J_history.append(J)

        # 判断是否收敛
        if i > 0 and abs(J_history[-1] - J_history[-2]) < tol:
            break

    return theta, J_history
