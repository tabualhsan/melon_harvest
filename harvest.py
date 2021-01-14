############
# Part 1   #
############
# sudo:
    # fill in the class with the melon type data as attributes
    # in func make_melon_types return a list objects from class MelonTypes
    # muskmelon = MelonType()
    l with proscuitto

    # Has seeds

    # Name: Yellow Watermelon

    # Reporting code: yw

    # First harvest in 2013

    # Color: yellow

    # Pairs well with ice cream

    # Has seeds
    # Name: Muskmelon

    # Reporting code: musk

    # First harvest in 1998

    # Color: green

    # Pairs well with mint

    # Seedless

    # Bestseller


    # Name: Casaba

    # Reporting code: cas

    # First harvest in 2003

    # Color: orange

    # Pairs well with strawberries and mint

    # Has seeds

    # Name: Crenshaw

    # Reporting code: cren

    # First harvest in 1996

    # Color: green

    # Pairs wel
    # Bestseller
class MelonType(object):
    """A species of melon at a melon farm."""
    
    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        #where would we be putting our instance attributes
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list.""" 
     
        self.pairings.append(pairing)


        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

        # Fill in the rest


def make_melon_types(*melon):
    all_melon_types = []

    """Returns a list of current melon types."""
    muskmelon = MelonType('musk', "1998", "green", "seedless", "bestseller") 
    casaba = MelonType("cas", "2003","orange", "seeds")
    crenshaw = MelonType("cren", "1996", "green", "seedless", "")
    yellowWatermelon = MelonType("yw", "2013", "yellow", "sees", "bestseller")
    
    all_melon_types.append(melon)

    # Fill in the rest
    return all_melon_types


print(make_melon_types(muskmelon, casaba, crenshaw, yellowWatermelon))
    

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



