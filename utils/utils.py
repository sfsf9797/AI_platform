import numpy as np
from typing import Tuple
from datetime import datetime


def make_grid(
    shape: Tuple[int, int], 
    window: int) ->np.ndarray :
    """
        Return Array of size (N,4), where N - number of tiles,
        2nd axis represente slices: x1,x2,y1,y2 

    Parameters
    -----------
    shape
        the shape of the image 
    window:
        size of one image tile 

    Return 
    --------
    np.array

    a grid that help us divide image into tiles with window size.

    """
    x, y = shape
    nx = x // window if x > window else 1
    x1 = np.linspace(0, x, num=nx, endpoint=False, dtype=np.int64)
    x1[-1] = x - window
    x2 = (x1 + window).clip(0, x)
    ny = y // window
    y1 = np.linspace(0, y, num=ny, endpoint=False, dtype=np.int64)
    y1[-1] = y - window if y > window else 1
    y2 = (y1 + window).clip(0, y)
    slices = np.zeros((nx,ny, 4), dtype=np.int64)
    
    for i in range(nx):
        for j in range(ny):
            slices[i,j] = x1[i], x2[i], y1[j], y2[j]    
    return slices.reshape(nx*ny,4) 


def pad_image(image: np.ndarray, window: int) ->np.ndarray :
    '''
        pad image with zero if either dimension in x or y
        is less than the window size

    Parameters
    ----------------
    image: 
        input image
    window:
        window size
    
    Returns
    --------
    np array of image
    '''

    padded_img = None

    x,y,c = image.shape 

    if x < window or y < window:

        new_x = x if x > window else window
        new_y = y if y > window else window 

        padded_img = np.zeros((new_x, new_y, c))

        padded_img[:x, :y] = image[:x, :y]

        return padded_img  
        
    return image


def generate_filename(filename: str) ->str:

    '''
    produce hashed fileName

    parameters
    -----------
    filename:
        file's name
    '''

    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return 'uploaded_' + str(hash(filename + dt_string)) + '.png'






