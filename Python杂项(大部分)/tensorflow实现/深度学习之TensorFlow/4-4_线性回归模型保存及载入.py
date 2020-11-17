# -*- coding: utf-8 -*-
"""
与3-1_线性回归.py比较
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 存放批次值和损失值
plotdata = { "batchsize":[], "loss":[] }
def moving_average(a, w=10):
    if len(a) < w:
        return a[:]
    return [val if idx < w else sum(a[(idx-w):idx])/w for idx, val in enumerate(a)]

# 生成模拟数据
train_X = np.linspace(-1, 1, 100)
# y=2x, 但是加入了噪声
# 将x乘以2, 再加上一个[-1 1]之间的随机数X0.3
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3
# 显示模拟数据点
plt.plot(train_X, train_Y, 'ro', label='Original data')
plt.legend()
plt.show()

"""1"""
tf.reset_default_graph()
"""1"""

# 创建模型
# X和Y为占位符, 使用placeholder函数进行定义
# X代表输入
X = tf.placeholder("float")
# Y代表对应的真实值
Y = tf.placeholder("float")
# 模型参数, 使用variable函数定义变量
# W为权重, W被初始化为[-1, 1]的随机数, 形状为一维的数字
W = tf.Variable(tf.random_normal([1]), name="weight")
# b为偏执值, b的初始化为0, 形状也是一维的数字
b = tf.Variable(tf.zeros([1]), name="bias")
# 前向结构, multiply函数是两个数相乘的意思, 再加上b就等于z
z = tf.multiply(X, W) + b

# 反向优化
# 定义cost等于生成值与真实值的平方差
cost = tf.reduce_mean(tf.square(Y - z))
# 定义一个学习率, 代表调整参数的速度, 一般小于1.
# 值越大调整速度越大, 但不精确. 值越小调整精度越高, 但速度慢
learning_rate = 0.01
# GradientDescentOptimizer函数是封装好的梯度下降算法, 里面的参数learning_rate叫做学习率
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# 初始化所有变量
init = tf.global_variables_initializer()
# 定义参数
training_epochs = 20
display_step = 2

"""2"""
# 生成saver
saver = tf.train.Saver()
savedir = "log/"
"""2"""

# 启动session
with tf.Session() as sess:
    sess.run(init)
    #向模型输入数据
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # 显示训练中的详细信息
        if epoch % display_step == 0:
            loss = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
            print("Epoch:", epoch + 1, "cost=", loss, "W=", sess.run(W), "b=", sess.run(b))
            if not (loss == "NA"):
                plotdata["batchsize"].append(epoch)
                plotdata["loss"].append(loss)

    print(" Finished!")
    """3"""
    saver.save(sess, savedir + 'linermodel.cpkt')
    """3"""
    print("cost=", sess.run(cost, feed_dict={X: train_X, Y: train_Y}), "W=", sess.run(W), "b=", sess.run(b))
    # print ("cost:",cost.eval({X: train_X, Y: train_Y}))

    # 图形显示
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

    plotdata["avgloss"] = moving_average(plotdata["loss"])
    plt.figure(1)
    plt.subplot(211)
    plt.plot(plotdata["batchsize"], plotdata["avgloss"], 'b--')
    plt.xlabel('Minibatch number')
    plt.ylabel('Loss')
    plt.title('Minibatch run vs. Training loss')

    plt.show()

"""4"""
with tf.Session() as sess2:
    sess2.run(tf.global_variables_initializer())
    saver.restore(sess2, savedir+"linermodel.cpkt")
    print("x=0.2, z=", sess2.run(z, feed_dict={X: 0.2}))
"""4"""