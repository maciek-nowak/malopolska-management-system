class ElementaryRegion:
    """
    Attributes:
        name (str)
        administrative_number (int)
        voivodeship (Voivodeship)
        county (CountyArea)
        community (Community)
        area_type (str)
    """

    area_type = ''

    def __init__(self, name, number, voivodeship, county, community):
        self.name = name
        self. administrative_number = number
        self.voivodeship = voivodeship
        self.county = county
        self.community = community
