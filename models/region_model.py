class Region:
    """
    Attributes:
        name (str)
        administrative_number (int)
        area_type (str)
    """

    regions = []

    def __init__(self, name, number):
        if type(name) is str and type(number) is int:
            self.name = name
            self.administrative_number = number
            Region.regions.append(self)
        else:
            raise TypeError
