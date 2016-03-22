#!/usr/bin/python3

from csv import DictReader
from sys import argv

PLAYER_START_OF_LINE_FORMAT = (
    '001 {startingrank:>4} {sex:1.1}{title:>3.3} {name:<33.33} '
    '{rating:>4} {federation:>3.3} {membernumber:>11.11} {birthday:<10.10} '
    '{points:>4.1f} {rank:>4}'
    )

def create_rounds_part_of_player_line(*rounds):
    return '  ' + '  '.join(
        '{:>4} {:1.1} {:1.1}'.format(*round_v)
        for round_v in rounds
        )

def create_player_line(*rounds, **player):
    return \
        PLAYER_START_OF_LINE_FORMAT.format( **player ) + \
        create_rounds_part_of_player_line(*rounds)

def extract_round_info_from_player(player):
    i = 1
    while True:
        round_str = 'round%sop' % i
        if not round_str in player:
            break
        #else:
        yield (player[round_str],
               player['round%scolor' % i],
               player['round%sresult' % i] )
        i+=1
        
if __name__ == "__main__":
    with open(argv[1]) as f:
        d = DictReader(f)
        print ("""XXR 5
XXC rank black1""")
        print ("""XXP 10 14
XPP 12 13""")
        
        for player in d:
            rounds = list(extract_round_info_from_player(player))
            player['points'] = float(player['points'])
            player.update( dict(
                    sex='m', title="", federation="CAD",
                    birthday="1900/01/01", rank='1' ) )
            print( create_player_line(*rounds, **player) )
