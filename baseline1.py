# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing speed baseline experiments.
This baseline is the time needed to parse a set of sentences using the ACE parser without any speedups.
'''

import glob
from ace_wrapper import run_ace

#class baseline1:

def run(profiles_path, grammar, ace_exec, output_path):
    print('Running baseline 1 (no supertagging)...')
    responses = []
    for i, tsuite in enumerate(sorted(glob.iglob(profiles_path + '/**'))):
        responses_tsuite, coverage, avg_time = run_ace(tsuite, grammar, ace_exec, [], 'i-input', output_path)
        responses.extend(responses_tsuite)
        print('Coverage for ' + tsuite + ': ' + str(coverage))
        print('Average parsing time per sentence time for ' + tsuite + ': ' + str(avg_time))

