import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#Placeholder is a keyword in tensorflow which takes input. Necessary argument is the datatype that we are going to give
a_0 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

#Initial 784 nodes --> 30 nodes --> 10 output classes
middle1 = 30
middle2 = 20

#w1 --> 784x30 with each row having 30 weights connected to 30 nodes of hidden layer
#b1 --> 1x30 as it has 1 node and connects to 30 nodes of hidden layer
#w2 --> 30x10 as it has 30 nodes in hidden layer and connects to 10 output nodes
#b2 --> 1x10 as it has 1 node and connects to 10 nodes of output layer
#Variable --> declaring and truncated_normal --> take with mean 0 and std 1

w_1 = tf.Variable(tf.truncated_normal([784, middle1]))
b_1 = tf.Variable(tf.truncated_normal([1, middle1]))
w_2 = tf.Variable(tf.truncated_normal([middle1, middle2]))
b_2 = tf.Variable(tf.truncated_normal([1, middle2]))
w_3 = tf.Variable(tf.truncated_normal([middle2,10]))
b_3 = tf.Variable(tf.truncated_normal([1, 10]))
print("First layer(input --> hidden layer 1) " + str(w_1))
print("First layer(input --> hidden layer 1) bias " + str(b_1))
print("Second layer(hidden layer 1 --> hidden layer 2) " + str(w_2))
print("Second layer(hidden layer 1 --> hidden layer 2) bias " + str(b_2))
print("Third layer(hidden layer 2 --> output) " + str(w_1))
print("Third layer(hidden layer 2 --> output) bias " + str(w_1))
def sigma(x):
    return tf.div(tf.constant(1.0),
                  tf.add(tf.constant(1.0), tf.exp(tf.negative(x))))


#FORWARD PROPAGATION
z_1 = tf.add(tf.matmul(a_0, w_1), b_1)
a_1 = sigma(z_1)
z_2 = tf.add(tf.matmul(a_1, w_2), b_2)
a_2 = sigma(z_2)
z_3 = tf.add(tf.matmul(a_2, w_3), b_3)
a_3 = sigma(z_3)
diff = tf.subtract(a_3, y)

#derivative is x(1-x) that is defined in sigmaprime
def sigmaprime(x):
    return tf.multiply(sigma(x), tf.subtract(tf.constant(1.0), sigma(x)))

#Backpropagation formulas
# d_z_2 = tf.multiply(diff, sigmaprime(z_2))
# d_b_2 = d_z_2
# d_w_2 = tf.matmul(tf.transpose(a_1), d_z_2)

# d_a_1 = tf.matmul(d_z_2, tf.transpose(w_2))
# d_z_1 = tf.multiply(d_a_1, sigmaprime(z_1))
# d_b_1 = d_z_1
# d_w_1 = tf.matmul(tf.transpose(a_0), d_z_1)



# eta = tf.constant(0.5)
# step = [
#     tf.assign(w_1,
#             tf.subtract(w_1, tf.multiply(eta, d_w_1)))
#   , tf.assign(b_1,
#             tf.subtract(b_1, tf.multiply(eta,
#                                tf.reduce_mean(d_b_1, axis=[0]))))
#   , tf.assign(w_2,
#             tf.subtract(w_2, tf.multiply(eta, d_w_2)))
#   , tf.assign(b_2,
#             tf.subtract(b_2, tf.multiply(eta,
#                                tf.reduce_mean(d_b_2, axis=[0]))))
# ]

cost = tf.multiply(diff, diff)
step = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

acct_mat = tf.equal(tf.argmax(a_3, 1), tf.argmax(y, 1))
acct_res = tf.reduce_sum(tf.cast(acct_mat, tf.float32))



#Session uses physical resources and is used to accomplish the task. Assign the variables, create the graph etc
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

for i in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(10)
    sess.run(step, feed_dict = {a_0: batch_xs,
                                y : batch_ys})
    if i % 1000 == 0:
        res = sess.run(acct_res, feed_dict =
                       {a_0: mnist.test.images[:1000],
                        y : mnist.test.labels[:1000]})
        print(res)


