import Match
import ConvertToDescriptor
import database
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import person


def run():
    list_database = database.load_database("list")

    image, descriptors = ConvertToDescriptor.camera_to_descriptors(upscale=0)
    detections = ConvertToDescriptor.image_to_detections(image)

    fig, ax = plt.subplots()
    ax.imshow(image)

    unknown_desc = []

    for face, d in zip(descriptors, detections):
        # Recognize the person
        name = Match.recognizeImage(list_database, face, 0.10)

        if name is 'Unknown':
            name = f'Unknown {len(unknown_desc) + 1}'
            unknown_desc.append(face)

        # Print a rectangle around their face
        rect = Rectangle((d.left(), d.bottom()), d.right() - d.left(), d.top() - d.bottom(), linewidth=1, edgecolor='r',
                         facecolor='none')
        ax.add_patch(rect)

        # Print their name (or 'Unknown')
        plt.text(d.left(), d.bottom(), f"{name}", color='#42f545')

    plt.show()

    for idx, desc in enumerate(unknown_desc):
        text = input(f"We don't know Unknown {idx + 1}, what is their name? ")
        name = text

        data = database.load_database("dict")
        if name in data:
            data[name].add_descriptor(desc, data)
        else:
            database.add_person(person.Person(name, (desc,)), data)
