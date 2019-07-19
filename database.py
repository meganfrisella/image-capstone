import ConvertToDescriptor
import person

images = {"Megan Frisella": ["megan1.jpg", "megan2.jpg"]}
myPath = "/Users/MeganFrisella/Image-Capstone/images/"
database = {}


for name in images:
    # Loop through all of the photos we have for a specific person
    descriptors = []
    for path in images[name]:
        descriptors = ConvertToDescriptor.jpeg_to_descriptors(myPath + path, upscale=1)

    database[person] = person.Person(name, descriptors)


def load_database(database_type):
    if database_type is "dict":
        return database
    elif database_type is "list":
        return database.values()

