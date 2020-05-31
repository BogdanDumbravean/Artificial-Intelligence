# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
import tensorflow as tf
import input_data
#%matplotlib inline
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0" #for training on gpu


data = input_data.read_data_sets('data/',one_hot=True)

# Create dictionary of target classes
class_names = {
 0: '0',
 1: '1',
 2: '2',
 3: '3',
 4: '4',
 5: '5',
 6: '6',
 7: '7',
 8: '8',
 9: '9',
}

# Reshape training and testing image
train_images = data.train.images.reshape(-1, 28, 28, 1)
test_images = data.test.images.reshape(-1,28,28,1)

train_labels = data.train.labels
# transform for keras
train_labels = np.argmax(train_labels, axis=1)

test_labels = data.test.labels
# transform for keras
test_labels = np.argmax(test_labels, axis=1)

# number of iterations for training
training_iters = 200 
# learning rate for weights
learning_rate = 0.001 
# batch of images to train at a time
batch_size = 128

# MNIST data input (img shape: 28*28)
n_input = 28
# MNIST total classes (0-9 digits)
n_classes = 10



# Create the convolutional base
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# Add Dense layers on top
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))



# Compile and train model

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['acc'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))


# Evaluate model

plt.plot(history.history['acc'], label='accuracy')
plt.plot(history.history['val_acc'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

print('\n\nTest data:')
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)


print(test_acc)



