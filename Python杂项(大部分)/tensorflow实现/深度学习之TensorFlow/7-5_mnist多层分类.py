import tensorflow as tf

# 导入mnist数据集
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/data", one_hot=True)

# 参数设置
learning_rate = 0.001
training_epochs = 25
batch_size = 100
display_step = 1

# 设置网络模型参数
n_hidden_1 = 256# 第一个隐藏层节点个数
n_hidden_2 = 256# 第二个隐藏层节点个数
n_input = 784# mnist共784(28X28)维
n_classes = 10# mnist共10个类别(0-9)

# 定义占位符
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])

# 创建model
def multilayer_perceptron(x, weights, biases):
    # 第一层隐藏层
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # 第二层隐藏层
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # 输出层
    out_layer = tf.matmul(layer_2, weights['out']) + biases['output']
    return out_layer

# 学习参数
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# 输出值
pred = multilayer_perceptron(x, weights, biases)

# 定义loss和优化器
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

