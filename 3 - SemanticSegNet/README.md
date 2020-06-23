# Cloud Cover using Convolutional Neural Network
This project provides the cloud cover in percentage and okta unit from the image of visible spectrum taken from the ground.
It contains the scripts to train and check the performance of the network created. It also has a pretrained model to perform semantic segmentation.

## Installation
To run this script, one needs to have MATLAB installed on the computer, along with a licence to run MATLAB. Image Processing Toolbox and Deep Learning Toolbox is also required to run this script.
Make sure to provide the correct directory location of the dataset folder while training.

## Usage

The script consists of the function getOktaSemSeg() which gives out the cloud cover in the image provided. The function imports the pretrained network, and uses the model to perform semantic segmentation on the given image. The binarised image is generated from the model and its cloud cover in percentage and okta value is obtained.

```matlab 
[cent,okta]=getOktaSemSeg(img);
```

### train.m
The script train.m can train a network by providing the dataset. You can modify the layers and other parameters of the layers. The trained model can be tested and its confusion matrix can be generated

### performance.m
This script uses the pretrained network and can be used to debug and view the images obtained after it passes through the network. You can see the best and worst detected image by the network.

### segnet_ny6000.mat
This is the pretrained model which can be loaded into MATLAB to perform sematic segmentation. It has been trained using swinyseg dataset of 6000 images.
