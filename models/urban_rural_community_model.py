from models.community_model import Community


class UrbanRuralCommunity(Community):
    """
    Attributes:
        name (str)
        administrative_number (int)
        voivodeship (Voivodeship)
        county (CountyArea
        rural_areas (list)
        cities (list)
        area_type (str)
    """

    area_type = 'gmina miejsko-wiejska'

    def __init__(self, name, number, voivodeship, county):
        super().__init__(name, number, voivodeship, county)
        self.rural_areas = []
        self.cities = []
