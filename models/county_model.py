from models.county_area_model import CountyArea
from models.urban_rural_community_model import UrbanRuralCommunity
from models.urban_community_model import UrbanCommunity
from models.rural_community_model import RuralCommunity


class County(CountyArea):
    """
    Attributes:
        name (str)
        administrative_number (int)
        rural_communities (list)
        urban_rural_communities (list)
        urban_communities (list)
        voivodeship (Voivodeship)
        area_type (str)
    """

    area_type = 'powiat'

    def __init__(self, name, number, voivodeship):
        super().__init__(name, number, voivodeship)
        self.rural_communities = []
        self.urban_rural_communities = []

    def add_community(self, community):
        if type(community) is UrbanRuralCommunity:
            self.urban_rural_communities.append(community)
        elif type(community) is UrbanCommunity:
            self.urban_communities.append(community)
        elif type(community) is RuralCommunity:
            self.rural_communities.append(community)
        else:
            raise TypeError

    def get_community_by_number(self, community_number):
        for community in self.urban_communities + self.urban_rural_communities + self.rural_communities:
            if community.administrative_number == community_number:
                return community
