## Defining the UNET architecture 

from layers import *
from tensorflow import keras

def UNet():

    # number of filters in every block
    num_filters = [16, 32, 64, 128, 256]

    inputs = keras.layers.Input((image_size, image_size, 3))
    
    pool0 = inputs

    # Downsampling 
    #128 -> 64
    conv1, pool1 = down_block(pool0, num_filters[0], input_dropout_rate) 

    #64 -> 32
    conv2, pool2 = down_block(pool1, num_filters[1], dropout_rate) 
    
    #32 -> 16
    conv3, pool3 = down_block(pool2, num_filters[2], dropout_rate) 

    #16->8
    conv4, pool4 = down_block(pool3, num_filters[3], dropout_rate) 


    # Bottlenecking
    botn = bottleneck(pool4, num_filters[4])
    

    # Upsampling
    #8 -> 16
    uconv1 = up_block(botn, conv4, num_filters[3], dropout_rate) 

    #16 -> 32
    uconv2 = up_block(uconv1, conv3, num_filters[2], dropout_rate) 

    #32 -> 64
    uconv3 = up_block(uconv2, conv2, num_filters[1], dropout_rate)

    #64 -> 128
    uconv4 = up_block(uconv3, conv1, num_filters[0], dropout_rate)
    

    outputs = keras.layers.Conv2D(1, (1, 1), padding="same", activation="sigmoid")(uconv4)
    model = keras.models.Model(inputs, outputs)
    return model
