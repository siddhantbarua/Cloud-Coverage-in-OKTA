# Cloud-Coverage-in-OKTA
A project to calculate cloud coverage over an area

Cloud coverage is an important measurement for meteorological observations and predictions. This project implements different methods to calculate the cloud coverage via deep learning and image processing techniques. These implementations are:

1. 




### OKTA
Okta is a standard unit of measurement for cloud cover for meteorological purposes. It is an integer value ranging from 0 to 8, where a 0 okta coverage denotes clear skies, and a 8 okta coverage denotes completely cloudy sky.

### SWINySEG
For training the network, the SWINySEG (http://vintage.winklerbros.net/Publications/grsl2019.pdf) dataset was used. This dataset has 6768 day and night time images of sky/cloud patches and their corresponding binary segmentation maps. The dataset is available for download at: http://vintage.winklerbros.net/swinyseg.html

![alt test](http://vintage.winklerbros.net/Images/swinyseg.jpg)

