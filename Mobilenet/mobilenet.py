import pandas as pd
import numpy as np
import os
import keras
import matplotlib.pyplot as plt
from keras.layers import Dense,GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model, load_model
from keras.optimizers import Adam
import cv2
import tensorflow as tf

#os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
#os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
# from keras import backend as K
# print(K.tensorflow_backend._get_available_gpus())

#sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# In[2]:
# import tensorflow as tf
# with tf.device('/gpu:0'):
#     a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
#     b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
#     c = tf.matmul(a, b)
# with tf.Session() as sess:
#     print (sess.run(c))

# base_model=MobileNet(weights='imagenet',include_top=False) #imports the mobilenet model and discards the last 1000 neuron layer.

# x=base_model.output
# x=GlobalAveragePooling2D()(x)
# x=Dense(1024,activation='relu')(x) #we add dense layers so that the model can learn more complex functions and classify for better results.
# x=Dense(1024,activation='relu')(x) #dense layer 2
# x=Dense(512,activation='relu')(x) #dense layer 3
# preds=Dense(6,activation='softmax')(x) #final layer with softmax activation


# # In[3]:


# model=Model(inputs=base_model.input,outputs=preds)
#specify the inputs
#specify the outputs
#now a model has been created based on our architecture


# In[4]:


for layer in base_model.layers[:20]:
    layer.trainable=False
for layer in base_model.layers[20:]:
    layer.trainable=True


# In[5]:

model = load_model("/media/srinath/Major Project/Major/newmobilenet.h5")
# train_datagen=ImageDataGenerator(preprocessing_function=preprocess_input) #included in our dependencies

# train_generator=train_datagen.flow_from_directory('/media/srinath/Major Project/Major/newdata', # this is where you specify the path to the main data folder
#                                                  target_size=(224,224),
#                                                  color_mode='rgb',
#                                                  batch_size=32,
#                                                  class_mode='categorical',
#                                                  shuffle=True)


# In[33]:


#model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])
# Adam optimizer
# loss function will be categorical cross entropy
# evaluation metric will be accuracy

# step_size_train=train_generator.n//train_generator.batch_size
# model.fit_generator(generator=train_generator,
#                    steps_per_epoch=step_size_train,
# epochs=3)

#model.summary()
#print(model.summary())

#model.save('/media/srinath/Major Project/Major/newmobilenet.h5')

img = image.load_img("auto.jpeg", target_size = (224,224))
test_image = image.img_to_array(img)
test_image = np.expand_dims(test_image, axis = 0)
test_image  =preprocess_input(test_image)
print(test_image.shape)

output = model.predict(test_image)
output = output.reshape(len(output), 2, -1)
print(output.shape)
print(output)
print(output.argmax())
# pred_bboxes  =output[...,4]*224
# pred_shapes = output[..., 4:5]

# print(pred_shapes.shape, pred_shapes)
# print(pred_bboxes.shape, pred_bboxes)


# print(output)
# print(output.argmax())

# bbox_util = BBoxUtility(6)
# results = bbox_util.detection_out(output)
# print(results)




































#................LOADING THE IMAGE TO BE DONE BY KERAS. NOT BY OPENCV OR PIL................#
#img = cv2.imread("copy2.jpg",1)
#img = np.array("copy2.jpg")
#print(img.shape)
# plt.imshow(img)
# plt.show()
# height, width, channels = img.shape
# img = cv2.resize(img,(224,224))

# plt.imshow(img)
# plt.show()

#img = img.reshape(1, 224,224, 3)


# cv2.imshow("temp",img)
# cv2.waitKey(0)
#height, width, channels = img.shape
#print(height,width,channels)