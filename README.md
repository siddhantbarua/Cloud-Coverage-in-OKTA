# Cloud-Coverage-in-OKTA
A UNET model for performing semantic segmentation on images of the sky, to detect cloud coverage in an area.

Cloud coverage in an area is an important measurement for meteorological observations and predictions. This project trains a deep neural network to perform semantic segmentation on images of the sky. The output of the network is a binary segmentation map of the picture, classifying cloud and "non-cloud" pixels. The architecure used is the UNET model. 	

### UNET
UNET is a neural network architecture, first designed for use on biomedical images. It focus on image classification, where the input is an image and the output is a segmentation map of the image, into different classes. The original UNET paper can be found here: https://arxiv.org/pdf/1505.04597.pdf
The UNET architecture as shown below, has a contracting path, and an expanding path, giving it the appearence of a “U”.
![alt text](https://miro.medium.com/max/2824/1*f7YOaE4TWubwaFF7Z1fzNw.png)


### OKTA
Okta is a standard unit of measurement for cloud cover for meteorological purposes. It is an integer value ranging from 0 to 8, where a 0 okta coverage denotes clear skies, and a 8 okta coverage denotes completely cloudy sky.

### SWINySEG
For training the network, the SWINySEG (http://vintage.winklerbros.net/Publications/grsl2019.pdf) dataset was used. This dataset has 6768 day and night time images of sky/cloud patches and their corresponding binary segmentation maps. The dataset is available for download at: http://vintage.winklerbros.net/swinyseg.html

![alt test](http://vintage.winklerbros.net/Images/swinyseg.jpg)





