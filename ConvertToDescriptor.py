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
    detections = list(face_detect(img_array, upscale))
    descriptors = []
    
    for d in detections:
        shape = shape_predictor(img_array, d)
        face_descriptor = face_rec_model.compute_face_descriptor(img_array, shape)
        descriptors.append(np.array(face_descriptor))
    
    return descriptors

def camera_to_descriptors(upscale=0):
    return image_to_descriptors(take_picture(), upscale)

def jpeg_to_descriptors(filepath, upscale=0):
    return image_to_descriptors(io.imread(filepath), upscale)