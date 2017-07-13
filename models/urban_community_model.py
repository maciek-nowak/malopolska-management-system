from models.community_model import Community


class UrbanCommunity(Community):
    """
    Attributes:
        name (str)
        administrative_number (int)
        voivodeship (Voivodeship)
        county (CountyArea)
        elementary_regions (list)
        area_type (str)
    """

    area_type = 'gmina miejska'
