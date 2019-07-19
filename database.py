import ConvertToDescriptor
import person
import pickle

images = {"Megan": ["m1.jpeg", "m2.jpeg", "m3.jpeg"], "Vaishnavi": ["v1.JPG", "v2.JPG", "v3.JPG", "v4.JPG"],
          "Christian": ["c1.jpg", "c2.jpeg"]}
myPath = "/Users/MeganFrisella/GitHub/image-capstone/images/"


def generate_database():
    """
    Generates a database from images in the 'image' folder in the repo. To run this code, change 'myPath' to navigate
    to the folder on your local computer.
    :return: No return. Pickles the file in 'database.p'
    """
    database = {}

    for name in images:
        descriptors = []
        for path in images[name]:
            descriptors.append(ConvertToDescriptor.jpeg_to_descriptors(myPath + path))
        database[name] = person.Person(name, descriptors)

    output = open('database.p', 'wb')
    pickle.dump(database, output)
    output.close()


def load_database(database_type):
    """
    Loads the database of People objects as a specified data type
    :param database_type: either "dict" to load as a dictionary or "list" to load as a list
    :return: the database of People in the form of a dictionary or list
    """
    f = open("database.p", "rb")
    database = pickle.load(f)
    f.close()

    if database_type is "dict":
        return database
    elif database_type is "list":
        return database.values()

