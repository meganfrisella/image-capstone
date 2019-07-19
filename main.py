import Match
import ConvertToDescriptor
import database

list_database = database.load_database("list")


def run():
    descriptors = ConvertToDescriptor.camera_to_descriptors(upscale=1)
    name = Match.recognizeImage(list_database, descriptors, 0.5)
    return name
