from glob import glob
from keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


k = 0

datagen = ImageDataGenerator(
     rotation_range=40,
     width_shift_range=0.1,
     height_shift_range=0.1,
     shear_range=0.2,
     zoom_range=0.2,
     horizontal_flip=True,
     fill_mode='nearest',
      brightness_range=[0.2,1.2]
)


def generateData(index):
     
     try:
          img = load_img(f"/mnt/sda2/Final_year_project/btd_final_project/data/yes/y{index}.jpg")
          x =  img_to_array(img)
          x = x.reshape((1,)+ x.shape)
     

          i = 0
          for batch in datagen.flow(x, batch_size=1,
                                   save_to_dir='/mnt/sda2/Final_year_project/btd_final_project/augmentation/yesAug',save_format='jpeg'):
               i += 1
               
               if i > 5:
                    break  # otherwise the generator would loop indefinitely

     except Exception as e:
          print(e)

for i in range(300):
     generateData(i)