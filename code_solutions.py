import itertools
import pandas as pd

def day1(comb_len):
    '''
    Based on an input of integers, find the combination of two integers where the sum equals 2020, then multiply the two together
    '''
    with open('day1input.txt') as f:
        lines = f.readlines()
        lines = [int(x.strip()) for x in lines]

    def prod(val):
        '''
        Multiply elements in a tuple
        '''
        res = 1
        for ele in val:
            res *= ele
        return res

    combinations = list(itertools.combinations(lines, comb_len))

    combination_sums = []
    for comb in combinations:
        combination_sums.append(sum(comb))

    combination_mult = []
    for comb in combinations:
        combination_mult.append(prod(comb))

    comb_dict = {'combination': combinations, 'sum': combination_sums, 'mult': combination_mult}

    comb_df = pd.DataFrame(comb_dict)

    print(comb_df.loc[comb_df['sums'] == 2020])

if __name__ == '__main__':
    day1(3)
