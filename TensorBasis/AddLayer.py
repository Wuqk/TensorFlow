import tensorflow as tf

#Define layer function
def addLayer(inputs,inSize,outSize,activationFunction):
    weights = tf.random_normal([inSize,outSize])
    biases = tf.random_normal([1,outSize])
    result = tf.matmul(inputs,weights)+biases
    if activationFunction==None:
        return result
    else:
        return activationFunction(result)