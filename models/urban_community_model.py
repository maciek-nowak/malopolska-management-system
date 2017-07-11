from models.community_model import Community
from models.delegacy_model import Delegacy


class UrbanCommunity(Community):
    """
    Attributes:
        name (str)
        administrative_number (int)
        voivodeship (Voivodeship)
        county (CountyArea
        delegacies (list)
        area_type (str)
    """

    area_type = 'gmina miejska'

    def __init__(self, name, number, voivodeship, county):
        super().__init__(name, number, voivodeship, county)
        self.delegacies = []

    def add_elementary_region(self, elementary_region):
        if type(elementary_region) is Delegacy:
            self.delegacies.append(elementary_region)
        else:
            raise TypeError
