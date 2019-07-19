import ConvertToDescriptor
import person
import pickle

images = {"Megan": ["m1.jpeg", "m2.jpeg", "m3.jpeg"], "Vaishnavi": ["v1.JPG", "v2.JPG", "v3.JPG", "v4.JPG"],
          "Christian": ["c1.jpg", "c2.jpeg"]}
myPath = "/Users/MeganFrisella/GitHub/Image-Capstone/images/"


def generate_database():
    database = {}

    for name in images:
        descriptors = []
        for path in images[name]:
            descriptors.append(ConvertToDescriptor.jpeg_to_descriptors(myPath + path, upscale=0))
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

def add_person(person,database):
    '''
    Adds a person object to the database

    Parameters:
    -----------
    person [type: Person]
        The Person object you want to add to the database

    database [type: dict]
        The database dictionary

    Returns:
    --------
    Nothing
    '''
    database[person.name] = person
    f = open('database.p','wb')
    pickle.dump(database,f)
    f.close