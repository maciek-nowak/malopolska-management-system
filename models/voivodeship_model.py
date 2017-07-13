from models.region_model import Region
from models.county_area_model import CountyArea


class Voivodeship(Region):
    """
    Attributes:
        name (str)
        administrative_number (int)
        counties (list)
        area_type (str)
    """

    area_type = 'województwo'

    def __init__(self, name, number):
        super().__init__(name, number)
        self.counties = []

    def add_county_area(self, county_area):
        if isinstance(county_area, CountyArea):
            self.counties.append(county_area)
        else:
            raise TypeError

    def get_county_by_number(self, county_number):
        for county in self.counties:
            if county.administrative_number == county_number:
                return county
