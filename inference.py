import numpy as np
from model.build_model import OnnxModel
from utils.utils import make_grid, pad_image
import cv2
from config.config import *

def inference(img_path: str) -> np.ndarray:
    '''
    dividing the large images into multiple
    images' tiles, make inference, and combining all
    images tiles into one.

    Parameters
    -----------
    img_path: path to the image

    Returns
    ----------
    numpy array 
    '''

    img = cv2.imread(img_path)

    #make sure the image is channel last
    if img.shape[-1] !=  3:
        img = img.reshape(img.shape[1].img.shape[2],3)

    ori_shape  = img.shape 
        
    img = pad_image(img, WINDOW_SIZE)
    new_shape = img.shape
    grid = make_grid(new_shape[:2], WINDOW_SIZE)

    output_img = np.zeros((new_shape[0],new_shape[1]))

    model = OnnxModel()

    for (x1,x2,y1,y2) in grid: 

        #divide image into smaller image tile
        sub_img = img[x1:x2,y1:y2]
        #inference
        out = model.inference(sub_img, WINDOW_SIZE)
        output_img[x1:x2,y1:y2] = out

    #return array with input image's shape
    return output_img[:ori_shape[0],:ori_shape[1]]


