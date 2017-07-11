from models.elementary_region_model import ElementaryRegion


class City(ElementaryRegion):
    """
    Attributes:
        name (str)
        administrative_number (int)
        voivodeship (Voivodeship)
        county (CountyArea)
        community (Community)
        area_type (str)
    """

    area_type = 'miasto'
