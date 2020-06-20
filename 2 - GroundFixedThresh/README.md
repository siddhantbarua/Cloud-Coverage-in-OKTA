# Cloud Cover using Ground image using Fixed Thresholding
This project provides the cloud cover in percentage and okta unit from the image of visible spectrum taken from the ground.

## Installation
To run this script, one needs to have MATLAB installed on the computer, along with a licence to run MATLAB. Image Processing Toolbox is also required to run this script.

## Usage

The script consists of two functions which gives out the cloud cover in the image provided. The image is converted into HSV color space and saturation channel is used to segment the sky and cloud. Pure white has saturation value of 0 so it helps in differentiating between sky and cloud. The image is binarised using Otsu's method and a binary image is obtained.

### saturateinv()
The function saturateinv() inputs a visible cloud image from ground and gives the output 'bin' which is a binary image with white pixel as cloud and black pixel as sky. This function can be used to view the binary segmented image.

```matlab 
bin=saturateinv(img);
```
### groundThresh()
The function groundThresh() recieves the visible ground image and uses the saturateinv() function and finds out the cloud cover
The variable cent stores the cloud cover in percentage and okta variable gives its okta unit equivalent.

```matlab 
[cent, okta]=groundThresh(img);
```
