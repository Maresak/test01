'''
Created on 2019. 3. 20.

@author: Won Jong Hyun
'''
import tensorflow as tf

first_test = tf.constant("testing tensorflow-gpu")

with tf.Session() as sess:
    print(sess.run(first_test))