import numpy as np
import os
import glob
import tifffile

source_dir ="test_image"
save_to = "outputs"


def get_image(source_dir): 

    IDs = []
    for i in range(len(glob.glob(source_dir + "\*.tif"))):

        images = glob.glob(source_dir + "\*.tif")
        
        if len(images) == 0:
            print("There is no .tif file in the folder")
            exit
        
        elif len(images) == 1:
            print("There is 1 .tif file in the folder")
        
        else:
            print("There are {} .tif files in the folder".format(len(images)))

        imge_ID = source_dir + '_' + i
        IDs.append(image_ID)
        yield IDs

def im2npy(source_dir,save_to,image_extension):

    IDs = get_image_ID_generator(source_dir = source_dir, extension = image_extension)
    iter_IDs = iter(IDs)
