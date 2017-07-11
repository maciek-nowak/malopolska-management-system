class CountyArea:
    """
    Attributes:
        name (str)
        administrative_number (int)
        urban_communities (list)
        voivodeship (Voivodeship)
        area_type (str)
    """

    area_type = ''

    def __init__(self, name, number, voivodeship):
        self.name = name
        self.administrative_number = number
        self.urban_communities = []
        self.voivodeship = voivodeship
