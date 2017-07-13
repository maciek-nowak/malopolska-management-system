from models.region_model import Region
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
    """
    Creates voivodeship object.

    Args:
        region_list (list): list of regions with their data

    Returns:
        voivodeship (Voivodeship): object represents whole voivodeship
    """

    for region in region_list:
        if region[5] == Voivodeship.area_type:
            name = region[4]
            number = int(region[0])
            return Voivodeship(name, number)


def insert_county_areas(voivodeship, region_list):
    """
    Creates all objects of CuntyArea class.

    Args:
        voivodeship (Voivodeship): object represents whole voivodeship
        region_list (list): list of regions with their data

    Returns:
        None (function operates on voivodeship object)
    """

    classes = [County, CityWithCountyRights]
    for county_type in classes:
        for region in region_list:
            if region[5] == county_type.area_type:
                name = region[4]
                number = int(region[1])
                voivodeship.add_county_area(county_type(name, number, voivodeship))


def insert_communities(voivodeship, region_list):
    """
    Creates all objects of Community class.

    Args:
        voivodeship (Voivodeship): object represents whole voivodeship
        region_list (list): list of regions with their data

    Returns:
        None (function operates on voivodeship object)
    """

    classes = [UrbanRuralCommunity, RuralCommunity, UrbanCommunity, Delegacy]
    for community_type in classes:
        for region in region_list:
            if region[5] == community_type.area_type:
                name = region[4]
                number = int(region[2])
                county_number = int(region[1])
                county = voivodeship.get_county_by_number(county_number)
                county.add_community(community_type(name, number, county))


def insert_elementary_regions(voivodeship, region_list):
    """
    Creates all objects of ElementaryRegion class.

    Args:
        voivodeship (Voivodeship): object represents whole voivodeship
        region_list (list): list of regions with their data

    Returns:
        None (function operates on voivodeship object)
    """

    classes = [RuralArea, City]
    for region_type in classes:
        for region in region_list:
            if region[5] == region_type.area_type:
                name = region[4]
                number = int(region[3])
                county_number = int(region[1])
                county = voivodeship.get_county_by_number(county_number)
                community_number = int(region[2])
                community = county.get_community_by_number(community_number)
                community.add_elementary_region(region_type(name, number, community))


def load_database():
    """
    Prepares list with regions statistics.

    Returns:
        voivodeship (Voivodeship): object represents whole Małopolskie voivodeship
    """

    with open('csv/malopolska.csv') as database:
        content = database.readlines()
    region_list = [line.strip().split('\t') for line in content]

    voivodeship = create_voivodeship(region_list)
    insert_county_areas(voivodeship, region_list)
    insert_communities(voivodeship, region_list)
    insert_elementary_regions(voivodeship, region_list)
    return voivodeship
