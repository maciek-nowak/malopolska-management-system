from models.community_model import Community
from models.rural_area_model import RuralArea
from models.city_model import City


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

    def add_elementary_region(self, elementary_region):
        if type(elementary_region) is RuralArea:
            self.rural_areas.append(elementary_region)
        elif type(elementary_region) is City:
            self.cities.append(elementary_region)
        else:
            raise TypeError
