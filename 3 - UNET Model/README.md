# Cloud-Coverage-in-OKTA
A UNET model for performing semantic segmentation on images of the sky, to detect cloud coverage in an area.

(This project can also be tried on Google colab: https://colab.research.google.com/drive/1Wl5gOlZiABUomLTcF-H9wKFymGTRAMZm?authuser=1#scrollTo=xo2vbMchraQ-)

his project trains a deep neural network to perform semantic segmentation on images of the sky. The output of the network is a binary segmentation map of the picture, classifying cloud and "non-cloud" pixels. The architecure used is the UNET model. 	

### UNET
UNET is a neural network architecture, first designed for use on biomedical images. It focus on image classification, where the input is an image and the output is a segmentation map of the image, into different classes. The original UNET paper can be found here: https://arxiv.org/pdf/1505.04597.pdf
The UNET architecture as shown below, has a contracting path, and an expanding path, giving it the appearence of a “U”.
![alt text](https://miro.medium.com/max/2824/1*f7YOaE4TWubwaFF7Z1fzNw.png)

### SWINySEG
For training the network, the SWINySEG (http://vintage.winklerbros.net/Publications/grsl2019.pdf) dataset was used. This dataset has 6768 day and night time images of sky/cloud patches and their corresponding binary segmentation maps. The zipped file of the SWINySEG dataset is included in the "Cloud-Coverage-in-OKTA/Datasets/" directory. The password for unzipping the same can be found at: http://vintage.winklerbros.net/swinyseg.html

![alt test](http://vintage.winklerbros.net/Images/swinyseg.jpg)








