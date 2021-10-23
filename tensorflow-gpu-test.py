import tensorflow as tf

print(tf.test.is_gpu_available())
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
hello = tf.constant('test!')
sess = tf.Session()
print(sess.run(hello))
