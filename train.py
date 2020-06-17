## Training the UNET model with the SWINySEG dataset. Make sure there is a Datasets/ directory in the same directory as the program, having the SWINySEG dataset. 
import os
import random
import matplotlib.pyplot as plt

from DataGen import *
from layers import *
import UNET

# Setting up parameters
image_size = 128
batch_size = 16
val_data_size = 600

# Dropout parameters for regularization
input_dropout_rate = 0.25
dropout_rate = 0.5

current_dir = os.getcwd()
# Training path having images and ground truths in different directories "images" and "GTmaps" 
train_path = current_dir + "/Datasets/SWINySEG/"

# Get image, GT ids. SWINySEG has .jpg images and .png GTs. To refer to a pair with same id, removing file extensions
lst = os.listdir(train_path+"images/")
train_ids = [x.split('.')[0] for x in lst]

# Divide ids into training and validation 
valid_ids = train_ids[:val_data_size]
train_ids = train_ids[val_data_size:]


# Setting up the model
UNET.image_size = image_size
UNET.input_dropout_rate = input_dropout_rate
UNET.dropout_rate = dropout_rate
model = UNET.UNet()


# To test if dataset is correctly loaded
def test_load():
    # Load a batch for testing
    gen = DataGen(train_ids, train_path, batch_size=batch_size, image_size=image_size)
    x, y = gen.__getitem__(0)
    print(x.shape, y.shape)

    # View a image, GT pair from testing batch
    r = random.randint(0, len(x)-1)

    fig = plt.figure()
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    ax = fig.add_subplot(1, 2, 1)
    fig.suptitle("Test load")
    ax.imshow(x[r])
    ax = fig.add_subplot(1, 2, 2)
    ax.imshow(np.reshape(y[r], (image_size, image_size)), cmap="gray")
    plt.show()

# To test if images have loaded correctly
# test_load()

# Learning rate for adam
learning_rate = "0.0005"

opt = keras.optimizers.Adam(learning_rate=float(learning_rate))
model.compile(optimizer=opt, loss="binary_crossentropy", metrics=["acc"])
model.summary()


train_gen = DataGen(train_ids, train_path, image_size=image_size, batch_size=batch_size)
valid_gen = DataGen(valid_ids, train_path, image_size=image_size, batch_size=batch_size)

train_steps = len(train_ids)//batch_size
valid_steps = len(valid_ids)//batch_size

# Number of epochs
num_epochs =  1 

model.fit(train_gen, validation_data=valid_gen, steps_per_epoch=train_steps, validation_steps=valid_steps, 
                    epochs=num_epochs)

# To save weights. Make sure there is a weights directory in the same directory as the program.
# model.save_weights("weights/"+str(learning_rate)+str(batch_size)+str(input_dropout_rate)+str(dropout_rate)+".h5")

# Test your predictions
x, y = valid_gen.__getitem__(2)
result = model.predict(x)

result = result > 0.5

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle("Testing predictions")

ax1.imshow(np.reshape(x[0], (image_size, image_size, 3)))
ax2.imshow(np.reshape(y[0], (image_size, image_size)), cmap="gray")
ax3.imshow(np.reshape(result[0], (image_size, image_size)), cmap="gray")
plt.show()
