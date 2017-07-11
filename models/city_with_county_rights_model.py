from models.county_area_model import CountyArea
from models.urban_community_model import UrbanCommunity


class CityWithCountyRights(CountyArea):
    """
    Attributes:
        name (str)
        administrative_number (int)
        urban_communities (list)
        voivodeship (Voivodeship)
        area_type (str)
    """

    area_type = 'miasto na prawach powiatu'

    def add_community(self, community):
        if type(community) is UrbanCommunity:
            self.urban_communities.append(community)
        else:
            raise TypeError

    def get_community_by_number(self, community_number):
        for community in self.urban_communities:
            if community.administrative_number == community_number:
                return community
