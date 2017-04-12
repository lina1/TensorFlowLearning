#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lina on 2017/4/12


import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

print (node1, node2)

session = tf.Session()
print session.run([node1, node2])
