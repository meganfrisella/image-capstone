
import Match
import ConvertToDescriptor
import database
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import person

list_database = database.load_database("list")


def run(image):
    descriptors = ConvertToDescriptor.image_to_descriptors(image)
    detections = ConvertToDescriptor.image_to_detections(image)

    fig, ax = plt.subplots()
    ax.imshow(image)

    unknown_desc = []

    for face, d in zip(descriptors, detections):
        # Recognize the person
        name = Match.recognizeImage(list_database, face, 0.12)

        if name is 'Unknown':
            name = f'Unknown {len(unknown_desc)+1}'
            unknown_desc.append(face)

        # Print a rectangle around their face
        rect = Rectangle((d.left(), d.bottom()), d.right() - d.left(), d.top() - d.bottom(), linewidth=1, edgecolor='r',
                         facecolor='none')
        ax.add_patch(rect)

        # Print their name (or 'Unknown')
        plt.text(d.left(), d.bottom(), f"{name}", color='w')

    plt.show()

    for idx, desc in enumerate(unknown_desc):
        text = input(f"We don't know Unknown {idx+1}, what is their name? ")
        name = text
        print(desc)
        database.add_person(person.Person(name, (desc,)), database.load_database("dict"))
        print(database.load_database("dict"))
