#!/usr/bin/python3

from csv import DictReader, DictWriter
from sys import argv
from subprocess import Popen, PIPE

from pair_input import read_input_file

# argument order, input csv file, original trfx file, output trfx file,
# output csv file, round number
if __name__ == "__main__":
    players = read_input_file(argv[1])

    p = Popen( ('java', '-jar', 'javafo.jar', '-o', argv[3], argv[2] ),
               stdout=PIPE)
    (output, errrors) = p.communicate()
    match_ups = tuple(
        pair.split(' ')
        for pair in output.decode().splitlines()[1:] )

    with open(argv[4], 'w') as f:
        d = DictWriter(f, (
                'round',
                'whiteStartingRank', 'whiteName', 'whiteResult',
                'blackStartingRank', 'blackName', 'blackResult' ) )
        d.writeheader()
        d.writerows(
            {
                'round': argv[5],
                'whiteStartingRank': white,
                'whiteName': players[white]['name'],
                'whiteResult': '',
                'blackStartingRank': black,
                'blackName': players[black]['name'],
                'blackResult': ''
                }
            for white, black in match_ups
            )
