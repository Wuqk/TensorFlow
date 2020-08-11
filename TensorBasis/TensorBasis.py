import tensorflow as tf

#Define canstant
v_1 = tf.constant([1,2])
v_2 = tf.constant([2,3])

#Define variables
#mostimportant thing:before use variables you must initialization it first,if not you will get an exception
v_3 = tf.Variable(tf.random_normal([1,3],dtype=tf.float32))
v_4 = tf.Variable(tf.random_normal([3,2],dtype=tf.float32))

#Define placeholder
v_5 = tf.placeholder(tf.float32)
v_6 = tf.placeholder(tf.float32)

#Define tensor operation

#Addition
tensor_sum = tf.add(v_1,v_2)
#multiplication
tensor_mul = tf.matmul(v_3,v_4)


#Define Session
sess = tf.Session()
#Initaliza variables
init = tf.initialize_all_variables()
#Run tensor operation with session run function,and print the result with print function
sess.run(init)
print("Addition result:")
print(sess.run(tensor_sum))
print("Multiplication result:")
print(sess.run(tensor_mul))

#After that,you must close the session
sess.close()

'''
#For another way,you can use "with" to realize session run funciton without session.close() function like this
with tf.Session() as sess:
    sess.run(init)
    print("Addition result:")
    print(sess.run(tensor_sum))
    print("Multiplication result:")
    print(sess.run(tensor_mul))
 '''

