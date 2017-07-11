from models.county_model import County
from models.city_with_county_rights_model import CityWithCountyRights


class Voivodeship:
    """
    Attributes:
        name (str)
        administrative_number (int)
        counties (list)
        cities_with_county_rights (list)
        area_type (str)
    """

    area_type = 'województwo'

    def __init__(self, name, number):
        self.name = name
        self.administrative_number = number
        self.counties = []
        self.cities_with_county_rights = []

    def add_county_area(self, county_area):
        if type(county_area) is County:
            self.counties.append(county_area)
        elif type(county_area) is CityWithCountyRights:
            self.cities_with_county_rights.append(county_area)
        else:
            raise TypeError

    def get_county_by_number(self, county_number):
        for county in self.counties + self.cities_with_county_rights:
            if county.administrative_number == county_number:
                return county
