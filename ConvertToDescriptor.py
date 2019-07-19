import numpy as np
import skimage.io as io

from camera import take_picture

from dlib_models import load_dlib_models
load_dlib_models()
from dlib_models import models

face_detect = models["face detect"]
face_rec_model = models["face rec"]
shape_predictor = models["shape predict"]

def image_to_descriptors(img_array, upscale=0):
    """
    Detects faces in an image array and turns each one
    into a 128-D descriptor.
    
    Parameters
    ----------
    img_array : np.array[int]
        RGB image-array or 8-bit greyscale of shape=(H, W(, 3))
    
    upscale : int, optional (default=0)
        The number of times to upscale the image and reprocess it,
        to find smaller faces
    
    Returns
    -------
    List[np.array[float]]
        List of descriptor vectors of all detected faces in the
        image
        
    """
    assert upscale >= 0 and isinstance(upscale, int)
    assert len(img_array.shape) == 3
    
    detections = list(face_detect(img_array, upscale))
    descriptors = []
    
    for d in detections:
        shape = shape_predictor(img_array, d)
        face_descriptor = face_rec_model.compute_face_descriptor(img_array, shape)
        descriptors.append(face_descriptor)
    
    return descriptors

def image_to_detections(img_array, upscale=0):
    """
    Detects faces in an image array.
    
    Parameters
    ----------
    img_array : np.array[int]
        RGB image-array or 8-bit greyscale of shape=(H, W(, 3))
        
    upscale : int, optional (default=0)
        The number of times to upscale the image and reprocess it,
        to find smaller faces
    
    Returns
    -------
    List[fhog_object_detector]
        List of all face detections in the image
    
    """
    return list(face_detect(img_array, upscale))

def camera_to_descriptors(upscale=0):
    """
    Detects faces from a photo taken by the camera and turns
    each one into a 128-D descriptor.
    
    Parameters
    ----------
    upscale : int, optional (default=0)
        The number of times to upscale the image and reprocess it,
        to find smaller faces
    
    Returns
    -------
    np.array[int]
        RGB image-array or 8-bit greyscale of shape=(H, W(, 3))
        
    List[np.array[float]]
        List of descriptor vectors of all detected faces in the
        image
    
    """
    img_array = take_picture()
    return img_array, image_to_descriptors(img_array, upscale)

def jpeg_to_descriptors(filepath, upscale=0):
    """
    Detects faces from a jpeg image file and turns each
    one into a 128-D descriptor.
    
    Parameters
    ----------
    filepath : string
        The file path to the jpeg image.
    
    upscale : int, optional (default=0)
        The number of times to upscale the image and reprocess it,
        to find smaller faces
    
    Returns
    -------
    List[np.array[float]]
        List of descriptor vectors of all detected faces in the
        image
    
    """
    return image_to_descriptors(io.imread(filepath), upscale)