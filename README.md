# Cloud-Coverage-in-OKTA
A project to calculate cloud coverage over an area

Cloud coverage is an important measurement for meteorological observations and predictions. This project implements different methods to calculate the cloud coverage via deep learning and image processing techniques. 
This project was done under the guidance of the Indian Metereological Department, as part of our Practice School-I program at BITS Pilani.

### OKTA
Okta is a standard unit of measurement for cloud cover for meteorological purposes. It is an integer value ranging from 0 to 8, where a 0 okta coverage denotes clear skies, and a 8 okta coverage denotes completely cloudy sky.

The project includes the following implementations:
1. From Satellite images: This program calculates the cloud coverage over any city in India using satellite IR image data provided by the Indian meteorological department website: (https://mausam.imd.gov.in/imd_latest/contents/satellite.php) This is done using thresholding operations.
2. From ground images using Fixed Thresholding: This program uses visible light images and uses simple thresholding operations to classify cloud and sky pixels. 
3. Semantic Segmentation: This program creates a CNN to train the model on visible cloud images. The model performs semantic segmentation on the image and generates binarised map of the image.
4. UNET deep learning model: This program uses a UNET neural network architecture to perform semantic segmentation on visible light images of the sky. 






