## Data generator for the UNET model

import os

import cv2
import numpy as np

import tensorflow as tf
from tensorflow import keras

# Define image size
image_size = 128

# DataGen class to initialise batch and get batches of images and ground truths
class DataGen(keras.utils.Sequence):

    def __init__(self, ids, path, batch_size=8, image_size=128):
        self.ids = ids
        self.path = path
        self.batch_size = batch_size
        self.image_size = image_size
        self.on_epoch_end()


    # function to load an image    
    def __load__(self, id_name):
        # Paths. For SWINySEG, images are .jpg, and GTs are .png. Change the paths below to suit your dataset.
        image_path = os.path.join(self.path, "images/", id_name) + ".jpg"
        GTmap_path = os.path.join(self.path, "GTmaps/", id_name) + ".png"
  
        # Reading Image
        image = cv2.imread(image_path, 1)
        image = cv2.resize(image, (self.image_size, self.image_size))
        # cv2 stores in BGR
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Reading GT
        GT = cv2.imread(GTmap_path, 1)
        GT = cv2.resize(GT, (self.image_size, self.image_size))
        # To convert GT to Grayscale
        GT = cv2.cvtColor(GT, cv2.COLOR_BGR2GRAY)
           
        # Normalizaing 
        image = image/255.0
        GT = GT/255.0
        
        return image,GT
    

    # function to get batch of images and GTs
    def __getitem__(self, index):
        # For last batch
        if ((index+1)*self.batch_size) > len(self.ids):
            self.batch_size = len(self.ids) - index*self.batch_size
        
        # Selecting images
        batch_files = self.ids[index*self.batch_size : (index+1)*self.batch_size]
        
        image_list = []
        GT_list  = []
        
        # Loadig the images of the batch
        for id_name in batch_files:
            _img, _GT = self.__load__(id_name)
            image_list.append(_img)
            GT_list.append(_GT)
            
        image_list = np.array(image_list)
        GT_list  = np.array(GT_list)
        
        return image_list, GT_list
    
    
    def on_epoch_end(self):
        pass
    
    
    def __len__(self):
        return int(np.ceil(len(self.ids)/float(self.batch_size)))
