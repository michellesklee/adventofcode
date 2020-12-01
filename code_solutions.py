import itertools
import pandas as pd

def day1_part1():
    '''
    Based on an input of integers, find the combination of two integers where the sum equals 2020, then multiply the two together
    '''
    with open('day1input.txt') as f:
        lines = f.readlines()
        lines = [int(x.strip()) for x in lines]

    combinations = list(itertools.combinations(lines, 2))

    combination_sums = []
    for comb in combinations:
        combination_sums.append(sum(comb))

    combination_mult = [(x*y) for x, y in combinations]

    comb_dict = {'combinations': combinations, 'sums': combination_sums, 'mult': combination_mult}

    comb_df = pd.DataFrame(comb_dict)

    print(comb_df.loc[comb_df['sums'] == 2020])
