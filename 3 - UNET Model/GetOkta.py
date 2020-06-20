## Predicts cloud cover in an image and returns measurement in percentage and okta.

import os 

import cv2
import matplotlib.pyplot as plt 
import numpy as np
import UNET

def get_okta(pred):
    num_pix = image_size*image_size 
    cloud_pix = np.count_nonzero(pred==1) 
    
    percentage = cloud_pix*100/num_pix 
    okta = round(percentage/12.5)

    return percentage, okta

def predict(image, image_name):
    image = np.expand_dims(image, axis=0)
    result = model.predict(image)

    result = result>0.5
    pred = np.reshape(result[0], (image_size, image_size))

    percentage, okta = get_okta(pred)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle("The cloud cover in image '{}' = {}% OR {} OKTA".format(image_name, percentage, okta))

    ax1.imshow(image[0])
    ax1.set_title("Image")
    ax2.imshow(pred*255, cmap="gray")
    ax2.set_title("Prediction")
    plt.show()

    return pred

image_size = 128
current_dir = os.getcwd()
# Test path having test images
test_path = current_dir + "/Test/"
# Test image ids
test_ids = next(os.walk(test_path))[2]
# Directory to load trained weights from
weights_dir = current_dir + "/Weights/"
weights_filename = "0.0005800.3.h5"

UNET.image_size = image_size
UNET.input_dropout_rate = 0
UNET.dropout_rate = 0
model = UNET.UNet()
# Loading weights
weights = model.load_weights(weights_dir + weights_filename)

for image_id in test_ids:
    image_path = os.path.join(test_path, image_id)
    image = cv2.imread(image_path, 1)
    image = cv2.resize(image, (image_size, image_size))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pred = predict(image, image_id)

