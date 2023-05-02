# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing speed baseline experiments.
This baseline is the time needed to parse a set of sentences using the ACE parser without any speedups.
'''

import sys
from delphin import ace, itsdb
import glob


class baseline1:

    def run(path, grammar, ace_exec, output_path):
        print('Running baseline 1...')
        for i, tsuite in enumerate(sorted(glob.iglob(path + '/**'))):
            ts = itsdb.TestSuite(tsuite)
            items = list(ts.processed_items())
            baseline_responses = []
            no_result = []
            with open('ace_err.txt', 'w') as errf:
                with ace.ACEParser(grammar, executable=ace_exec, stderr=errf) as parser:
                    for response in items:
                        # Reparse each sentence, to measure the parser speed without supertagging
                        baseline_response = parser.interact(response['i-input'])
                        if len(baseline_response['results']) == 0:
                            no_result.append(response['i-input'])
                        else:
                            baseline_responses.append(response)
            with open('ace_err.txt', 'r') as errf:
                errors = errf.readlines()
            with open('noresults.txt', 'w') as f:
                for i, nrs in enumerate(no_result):
                    f.write(nrs + ': ' + errors[i] + '\n')
            return baseline_responses
