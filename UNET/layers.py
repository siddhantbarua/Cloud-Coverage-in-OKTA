## Defines layers for UNET architecture.

from tensorflow import keras

# Convolution layer for downsampling
def down_block(x, filters, dropout_rate, kernel_size=(3, 3), padding="same", strides=1):
    conv = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(x)
    conv = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(conv)
    pool = keras.layers.MaxPool2D((2, 2), (2, 2))(conv)
    pool = keras.layers.Dropout(dropout_rate)(pool)

    return conv, pool

# Convolutional layer for upsampling
def up_block(x, skip, filters, dropout_rate, kernel_size=(3, 3), padding="same", strides=1):
    us = keras.layers.UpSampling2D((2, 2))(x)
    concat = keras.layers.Concatenate()([us, skip])
    concat = keras.layers.Dropout(dropout_rate)(concat)
    conv = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(concat)
    conv = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(conv)

    return conv

# Bottlenecking
def bottleneck(x, filters, kernel_size=(3, 3), padding="same", strides=1):
    conv = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(x)
    conv = keras.layers.Conv2D(filters, kernel_size, padding=padding, strides=strides, activation="relu")(conv)
    return conv
