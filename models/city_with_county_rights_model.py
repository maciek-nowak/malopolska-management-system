from models.county_area_model import CountyArea


class CityWithCountyRights(CountyArea):
    """
    Attributes:
        name (str)
        administrative_number (int)
        communities (list)
        voivodeship (Voivodeship)
        area_type (str)
    """

    area_type = 'miasto na prawach powiatu'
