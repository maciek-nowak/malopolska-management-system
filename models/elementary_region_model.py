from models.region_model import Region


class ElementaryRegion(Region):
    """
    Attributes:
        name (str)
        administrative_number (int)
        community (Community)
        area_type (str)
    """

    area_type = ''

    def __init__(self, name, number, community):
        super().__init__(name, number)
        self.community = community
