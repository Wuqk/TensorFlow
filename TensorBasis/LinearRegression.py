import tensorflow as tf
# make inputs data and labels first,and make parameter
trueWeights = tf.constant([3.14, -1.2], shape=(2, 1))
trueBiase = tf.constant([4.1])
inputs = tf.random_normal([1000, 2], dtype=tf.float32)
labels = tf.matmul(inputs, trueWeights) + trueBiase


def addLayer(inputs, inSize, outSize, activationFunction):
    weights = tf.Variable(tf.random_normal([inSize, outSize], dtype=tf.float32))
    biase = tf.Variable(tf.random_normal([1, outSize]), dtype=tf.float32)
    y = tf.matmul(inputs, weights) + biase
    if activationFunction == None:
        return y
    else:
        return activationFunction(y)


l1 = addLayer(inputs, 2, 10, tf.nn.relu)
prediction = addLayer(l1, 10, 1, None)

loss = tf.reduce_mean(tf.square(labels-prediction),axis=0)

trainStep = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
write = tf.summary.FileWriter("./log",sess.graph)

for i in range(1000):
    sess.run(trainStep)
    if i % 50 == 0:
        print(sess.run(loss))

#After you run the program,type "tensorboard --logdir=log" in the Terminal(get into the current dir first)
#Then you can see the graph of this program on http://ItemName:6006
