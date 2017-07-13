import sys
from models.region_model import Region
from controllers import database_import
from views import region_view
import views.ui


def get_statistics():
    """
    Prepares list with regions statistics.

    Returns:
        statistics (list): list with pairs (region type and their amount)
    """

    statistics = {}

    for region in Region.regions:
        if region.area_type in statistics:
            statistics[region.area_type] += 1
        else:
            statistics[region.area_type] = 1
    region_order = ['województwo', 'powiat', 'miasto na prawach powiatu', 'gmina miejska', 'gmina miejsko-wiejska',
                    'gmina wiejska', 'delegatura', 'miasto', 'obszar wiejski']
    statistics = [[statistics[region_type], region_type] for region_type in region_order]

    return statistics


def get_longest_cities():
    """
    Prepares list with 3 longest city names.

    Returns:
        longest_city_names (list): list of 3 longest city names
    """

    city_types = ['miasto', 'miasto na prawach powiatu']
    city_names = [region.name for region in Region.regions if region.area_type in city_types]
    sorted_city_names = sorted(city_names, key=lambda city: len(city))

    longest_city_names = sorted_city_names[-1:-4:-1]
    longest_city_names = [[city] for city in longest_city_names]
    return longest_city_names


def get_county_with_most_communities(voivodeship):
    """
    Returns object of CountyArea class with most communities.

    Returns:
        most_numerous_county (CountyArea): county object containing most communities
    """

    most_numerous_county = voivodeship.get_county_by_number(1)
    for county in voivodeship.counties:
        if len(county.communities) > len(most_numerous_county.communities):
            most_numerous_county = county

    return most_numerous_county


def get_keyword_regions(keyword):
    """
    Prepares list with regions which contains given keyword in their name.

    Args:
        keyword (str): keyword used in searching objects

    Returns:
        keyword_regions (list): list with pairs (region name and their type)
    """

    keyword_regions = []
    for region in Region.regions:
        if keyword in region.name:
            keyword_regions.append([region.name, region.area_type])
    keyword_regions.sort()
    return keyword_regions


def get_regions_with_many_categories():
    """
    Prepares list with regions which name repeats in different region types.

    Returns:
        locations (list): list with Region class objects
    """

    locations = []
    for i in range(len(Region.regions)):
        for k in range(len(Region.regions)):
            name_1 = Region.regions[i].name
            name_2 = Region.regions[k].name
            if name_1 == name_2 and Region.regions[i] not in locations and i != k:
                locations.append(Region.regions[i])
    locations.sort(key=lambda x: x.name)
    return locations


def advanced_search():
    """
    Asks user for keyword and prints list of regions with keyword in their name.

    Returns:
        None
    """

    keyword = region_view.get_input('Searching for')
    keyword_regions = get_keyword_regions(keyword)
    if keyword_regions:
        region_view.print_message('Found ' + str(len(keyword_regions)) + ' location(s):')
        views.ui.print_table(keyword_regions, ['location', 'type'])
    else:
        region_view.print_error_message('There is no such region!')


def start_controller():
    """
    Switches between options

    Returns:
        None
    """

    region_view.print_message('Welcome in Know your neighbourhood!')
    try:
        voivodeship = database_import.load_database()
    except FileNotFoundError:
        region_view.print_message('Database file not found!')
        region_view.get_input('Press ENTER to exit the program!')
        sys.exit(0)

    choice = ''
    while choice != '0':
        region_view.print_menu()
        choice = region_view.get_input('Enter your choice')
        if choice == '1':
            statistics = get_statistics()
            views.ui.print_table(statistics, ['amount', 'type'])
        elif choice == '2':
            longest_city_names = get_longest_cities()
            views.ui.print_table(longest_city_names, ['Cities with longest names'])
        elif choice == '3':
            county_with_most_communities = get_county_with_most_communities(voivodeship)
            table_to_print = [[county_with_most_communities.name, str(len(county_with_most_communities.communities))]]
            views.ui.print_table(table_to_print, ['county with most communities', 'amount of communities'])
        elif choice == '4':
            locations = get_regions_with_many_categories()
            region_view.print_locations_list(locations)
        elif choice == '5':
            advanced_search()
        elif choice == '6':
            region_view.print_regions_tree(voivodeship)
        elif choice == '0':
            region_view.print_message('Thank you for using our app. See you next time!')
        else:
            region_view.print_error_message('There is no such option!')
