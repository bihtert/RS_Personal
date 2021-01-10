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

        image_ID = source_dir + '_' + i
        IDs.append(image_ID)
        
        return images
        yield IDs

def tif2array(source_dir,save_to):

    IDs = get_image(source_dir)
    iter_IDs = iter(IDs)

    for i,image in enumerate(images):

        image = tifffile.imread(image)
        ID = next(iter_IDs)
        array_img = np.asarray(image)

        np.save(save_to + '\\np-' + ID[-1] + '.npy', np_img)

    print("Process Ended. {} numpy arrays are created in total.".format(i + 1))

tif2array(source_dir, save_to)
