import ConvertToDescriptor
import person

images = {"Megan Frisella": ["megan1.jpg", "megan2.jpg"]}
myPath = "/Users/MeganFrisella/Image-Capstone/images/"
database = {}

for name in images:
    descriptors = []
    for path in images[name]:
        descriptors = ConvertToDescriptor.jpeg_to_descriptors(myPath + path, upscale=1)

    database[person] = person.Person(name, descriptors)


def load_database(database_type):
    """
    Loads the database of People objects as a specified data type
    :param database_type: either "dict" to load as a dictionary or "list" to load as a list
    :return: the database of People in the form of a dictionary or list
    """
    if database_type is "dict":
        return database
    elif database_type is "list":
        return database.values()

