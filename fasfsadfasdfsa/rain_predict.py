# Disable tensorflow debug information
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import pandas as pd
import tensorflow as tf
import sys
import numpy as np
import matplotlib.pyplot as plt

from gpiozero import LED
from time import sleep

from keras.preprocessing import image

# define led
red = LED(16) # pin 17
green = LED(20) #pin 20

print("Using tensorflow version", tf.__version__);

# read argument file
file_path = sys.argv[1]

# Load model
interpreter = tf.lite.Interpreter(model_path="4Weather_v1.tflite")

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

# Image Preparation
img = image.load_img(file_path, target_size=(224, 224))

img = image.img_to_array(img)
img = np.expand_dims(img, axis=0)
img = np.vstack([img])

# Prediction
interpreter.set_tensor(input_details[0]["index"], img)

interpreter.invoke()
prediction = interpreter.get_tensor(output_details[0]['index'])

# Displaying to console
if (prediction[0][0] == max(prediction[0]) or prediction[0][1] == max(prediction[0])):
    print("\nPrediction: Rain\n\n RED LED ON \n\n Initiate Close Rain Gate.. ")
    red.on()
    sleep(3)
    red.off()
else:
    print("\nPrediction: Not_rain\n\n GREEN LED ON \n\n Initiate Open Rain Gate.. ")
    green.on()
    sleep(3)
    green.off()
