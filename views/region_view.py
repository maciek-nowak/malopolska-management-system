import views.ui


def print_menu():
    menu = """\nWhat would you like to do:
    (1) List statistics
    (2) Display 3 cities with longest names
    (3) Display county's name with the largest number of communities
    (4) Display locations, that belong to more than one category
    (5) Advanced search
    (6) Show region dependancy tree
    (0) Exit program\n"""

    print(menu)


def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        None
    """

    print('\nError:', message)


def print_message(message):
    """
    Displays a message

    Args:
        message(str): message to be displayed

    Returns:
        None
    """

    print(message)


def get_input(message):
    """
    Gets input from the user.

    Args:
        message (str): message to display

    Returns:
        answer (str): string entered by user
    """

    answer = input(message + ': ')

    return answer


def print_regions_tree(voivodeship):
    """
    Prints all regions with proper layout.

    Args:
        voivodeship (Voivodeship): object represents whole voivodeship

    Returns:
        None
    """

    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RESET = '\033[0m'

    print(voivodeship.name + ' ' + voivodeship.area_type)

    for county in voivodeship.counties:
        print(RED + '\t' + county.name + ' ' + county.area_type + RESET)
        for community in county.communities:
            print(BLUE + '\t\t' + community.name + ' ' + community.area_type + RESET)
            for place in community.elementary_regions:
                print(GREEN + '\t\t\t' + place.name + ' ' + place.area_type + RESET)


def print_locations_list(locations):
    """
    Prints list of regions occuring in many region types.

    Args:
        locations (list): list of Region class objects

    Returns:
        None
    """

    list_to_print = [[locations[0].name, locations[0].area_type]]

    for region in locations[1:]:
        if region.name != list_to_print[-1][0]:
            list_to_print.append(['', ''])
        list_to_print.append([region.name, region.area_type])

    views.ui.print_table(list_to_print, ['name', 'region'])
