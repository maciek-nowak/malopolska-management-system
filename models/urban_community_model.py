from models.community_model import Community


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
