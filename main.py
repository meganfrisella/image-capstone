import Match
import ConvertToDescriptor
import database
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

list_database = database.load_database("list")


def run():
    image, descriptors = ConvertToDescriptor.camera_to_descriptors(upscale=0)
    detections = ConvertToDescriptor.image_to_detections(image)

    fig, ax = plt.subplots()
    ax.imshow(image)

    for face, d in zip(descriptors, detections):
        # Recognize the person
        name = Match.recognizeImage(list_database, face, 0.12)

        # Print their name (or 'Unknown')
        plt.text(d.left(), d.bottom(), f"{name}", color='w')

        # Print a rectangle around their face
        rect = Rectangle((d.left(), d.bottom()), d.right() - d.left(), d.top() - d.bottom(), linewidth=1, edgecolor='r',
                         facecolor='none')
        ax.add_patch(rect)

        """
        # Add an unknown person to the database
        if name is 'Unknown':
            text = input("We don't know this person, what is their name? ")
            name = text
        """



