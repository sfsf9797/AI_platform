from typing import Tuple

import openslide
from PIL.Image import Image


def get_slide_patch_image(
    wsi_path: str,
    location: Tuple[int, int],
    level: int = 0,
    size: Tuple[int, int] = (1024, 1024)
) -> Image:
    """ Read the slide file and extract the image of specified region

    Parameters
    ----------
    wsi_path: str
        The path to the input whole-slide image file
    location: Tuple[int, int]
        (x, y) tuple giving the top left pixel in the level 0 reference frame
    level: int
        the level number
    size: Tuple[int, int]
        (width, height) tuple giving the region size

    Returns
    -------
    PIL.Image.Image
        an RGBA Image containing the contents of the specified region.
    """
    wsi = openslide.OpenSlide(wsi_path)
    return wsi.read_region(location, level, size)
