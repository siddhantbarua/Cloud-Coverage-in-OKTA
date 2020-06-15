## Defining the UNET architecture 

import layers
from tensorflow import keras

def UNet():

    # filter shapes
    filter_shape = [16, 32, 64, 128, 256]

    inputs = keras.layers.Input((image_size, image_size, 3))
    
    pool0 = inputs

    # Downsampling 
    #128 -> 64
    conv1, pool1 = down_block(pool0, filter_shape[0], input_dropout_rate) 

    #64 -> 32
    conv2, pool2 = down_block(pool1, filter_shape[1], dropout_rate) 
    
    #32 -> 16
    conv3, pool3 = down_block(pool2, filter_shape[2], dropout_rate) 

    #16->8
    conv4, pool4 = down_block(pool3, filter_shape[3], dropout_rate) 


    # Bottlenecking
    botn = bottleneck(pool4, filter_shape[4])
    

    # Upsampling
    #8 -> 16
    uconv1 = up_block(botn, conv4, filter_shape[3], dropout_rate) 

    #16 -> 32
    uconv2 = up_block(uconv1, conv3, filter_shape[2], dropout_rate) 

    #32 -> 64
    uconv3 = up_block(uconv2, conv2, filter_shape[1], dropout_rate)

    #64 -> 128
    uconv4 = up_block(uconv3, conv1, filter_shape[0], dropout_rate)
    

    outputs = keras.layers.Conv2D(1, (1, 1), padding="same", activation="sigmoid")(uconv4)
    model = keras.models.Model(inputs, outputs)
    return model
