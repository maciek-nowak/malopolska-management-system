from models.region_model import Region
from models.elementary_region_model import ElementaryRegion


class Community(Region):
    """
    Attributes:
        name (str)
        administrative_number (int)
        elementary_regions (list)
        county (CountyArea)
        area_type (str)
    """

    area_type = ''

    def __init__(self, name, number, county):
        super().__init__(name, number)
        self.county = county
        self.elementary_regions = []

    def add_elementary_region(self, elementary_region):
        if isinstance(elementary_region, ElementaryRegion):
            self.elementary_regions.append(elementary_region)
        else:
            raise TypeError
