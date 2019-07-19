import Match
import ConvertToDescriptor
import person


def run():
    descriptors = ConvertToDescriptor.camera_to_descriptors(upscale=1)
    name = Match.recognizeImage(people, descriptors, 0.5)