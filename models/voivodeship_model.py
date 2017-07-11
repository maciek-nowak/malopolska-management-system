class Voivodeship:
    """
    Attributes:
        name (str)
        administrative_number (int)
        counties (list)
        cities_with_county_rights (list)
        area_type (str)
    """

    area_type = 'województwo'

    def __init__(self, name, number):
        self.name = name
        self.administrative_number = number
        self.counties = []
        self.cities_with_county_rights = []
