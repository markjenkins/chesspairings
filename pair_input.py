from csv import DictReader
from collections import OrderedDict

def read_input_file(input_file):
    with open(input_file) as f:
        d = DictReader(f)
        players = OrderedDict( (player['startingrank'], player)
                               for player in d )
    return players
