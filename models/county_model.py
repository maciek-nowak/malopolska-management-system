from models.county_area_model import CountyArea


class County(CountyArea):
    """
    Attributes:
        name (str)
        administrative_number (int)
        rural_communities (list)
        urban_rural_communities (list)
        urban_communities (list)
        voivodeship (Voivodeship)
        area_type (str)
    """

    area_type = 'powiat'

    def __init__(self, name, number, voivodeship):
        super().__init__(name, number, voivodeship)
        self.rural_communities = []
        self.urban_rural_communities = []
