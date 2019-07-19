import Match
import ConvertToDescriptor
import database
import matplotlib.pyplot as plt

list_database = database.load_database("list")


def run():
    image, descriptors = ConvertToDescriptor.camera_to_descriptors(upscale=0)
    name = Match.recognizeImage(list_database, descriptors, 0.2)

    detections = ConvertToDescriptor.image_to_detections()

    fig, ax = plt.subplots()
    ax.imshow(image)

    return name
