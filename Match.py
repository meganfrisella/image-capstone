def recognizeImage(people, d, cutoff):
    """
    :param people: list(), type: person
            d: np.array, type: float, shape: (128)
            cutoff: float
    :return: String
    This function takes in a list of people and returns either the name of a match or "Unknown"
    """
    for p in people:
        if p.match(d, cutoff):
            return p.name
    return "Unknown"
