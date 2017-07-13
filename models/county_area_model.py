from models.region_model import Region
from models.community_model import Community


class CountyArea(Region):
    """
    Attributes:
        name (str)
        administrative_number (int)
        communities (list)
        voivodeship (Voivodeship)
        area_type (str)
    """

    area_type = ''

    def __init__(self, name, number, voivodeship):
        super().__init__(name, number)
        self.communities = []
        self.voivodeship = voivodeship

    def add_community(self, community):
        if isinstance(community, Community):
            self.communities.append(community)
        else:
            raise TypeError

    def get_community_by_number(self, community_number):
        for community in self.communities:
            if community.administrative_number == community_number:
                return community
