from models.voivodeship_model import Voivodeship
from models.county_model import County
from models.city_with_county_rights_model import CityWithCountyRights
from models.urban_rural_community_model import UrbanRuralCommunity
from models.rural_community_model import RuralCommunity
from models.urban_community_model import UrbanCommunity
from models.rural_area_model import RuralArea
from models.city_model import City
from models.delegacy_model import Delegacy


def create_voivodeship(region_list):
    for region in region_list:
        if region[5] == Voivodeship.area_type:
            name = region[4]
            number = int(region[0])
            return Voivodeship(name, number)


def insert_county_areas(voivodeship, region_list):
    for region in region_list:
        if region[5] == County.area_type:
            name = region[4]
            number = int(region[1])
            voivodeship.add_county_area(County(name, number, voivodeship))
        elif region[5] == CityWithCountyRights.area_type:
            name = region[4]
            number = int(region[1])
            voivodeship.add_county_area(CityWithCountyRights(name, number, voivodeship))


def insert_communities(voivodeship, region_list):
    for region in region_list:
        if region[5] == UrbanRuralCommunity.area_type:
            name = region[4]
            number = int(region[2])
            county_number = int(region[1])
            county = voivodeship.get_county_by_number(county_number)
            county.add_community(UrbanRuralCommunity(name, number, voivodeship, county))
        elif region[5] == RuralCommunity.area_type:
            name = region[4]
            number = int(region[2])
            county_number = int(region[1])
            county = voivodeship.get_county_by_number(county_number)
            county.add_community(RuralCommunity(name, number, voivodeship, county))
        elif region[5] == UrbanCommunity.area_type:
            name = region[4]
            number = int(region[2])
            county_number = int(region[1])
            county = voivodeship.get_county_by_number(county_number)
            county.add_community(UrbanCommunity(name, number, voivodeship, county))


def insert_elementary_regions(voivodeship, region_list):
    for region in region_list:
        if region[5] == RuralArea.area_type:
            name = region[4]
            number = int(region[3])
            county_number = int(region[1])
            county = voivodeship.get_county_by_number(county_number)
            community_number = int(region[2])
            community = county.get_community_by_number(community_number)
            community.add_elementary_region(RuralArea(name, number, voivodeship, county, community))


def load_database():
    with open('csv/malopolska.csv') as database:
        content = database.readlines()
    region_list = [line.strip().split('\t') for line in content]

    voivodeship = create_voivodeship(region_list)
    insert_county_areas(voivodeship, region_list)
    insert_communities(voivodeship, region_list)
    insert_elementary_regions(voivodeship, region_list)
    return voivodeship


def start_controller():
    """
    Switches between options

    Returns:
        None
    """

    voivodeship = load_database()
    print(voivodeship.name, voivodeship.administrative_number)
    for county in voivodeship.counties + voivodeship.cities_with_county_rights:
        print(county.name, county.administrative_number)
        for
