#!/usr/bin/python3

from csv import DictReader, DictWriter
from sys import argv

from pair_input import read_input_file

REWARD_WIN = False

def score_delta(result, reward_win=False):
    if reward_win:
        return {'0': 0,
                '1': 3,
                '=': 1 }[result]
    else:
        return {'0': 0,
                '1': 1,
                '=': 0.5}[result]

if __name__ == "__main__":
    players = read_input_file(argv[1])
    
    max_round_seen = 0
    with open(argv[2]) as f:
        d = DictReader(f)
        for pair_result in d:

            round_num = pair_result['round']
            max_round_seen = max(max_round_seen, int(round_num))

            round_num_op = "round%sop" % round_num
            round_color = "round%scolor" % round_num
            round_result = "round%sresult" % round_num

            white = pair_result['whiteStartingRank']
            black = pair_result['blackStartingRank']
            players[white][round_num_op] = black
            players[black][round_num_op] = white
            players[white][round_color] = 'w'
            players[black][round_color] = 'b'
            players[white][round_result] = pair_result['whiteResult']
            players[black][round_result] = pair_result['blackResult']

            white_score_delta = score_delta(players[white][round_result],
                                            reward_win=REWARD_WIN)
            black_score_delta = score_delta(players[black][round_result],
                                            reward_win=REWARD_WIN)

            players[white]['points'] = \
                float(players[white]['points']) + white_score_delta

            players[black]['points'] = \
                float(players[black]['points']) + black_score_delta
            

        output_fields = ('startingrank', 'rating',
                         'name', 'membernumber', 'points'
                         )
        for i in range(1, max_round_seen+1):
            output_fields = output_fields + \
                ('round%sop' % i, 'round%scolor' % i, 'round%sresult' % i)

        with open(argv[3], 'w') as f:
            d = DictWriter(
                f, 
                output_fields
                )
            d.writeheader()
            d.writerows(players.values())
    
