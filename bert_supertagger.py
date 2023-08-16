# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing experiments using fine-tuned BERT supertagger.
'''

import glob
from ace_wrapper import run_ace

#class bert_supertagger:

def run(profiles_path, supertags_path, grammar, ace_exec, output_path):
    print('Running experiment with BERT supertags...')
    for i, tsuite in enumerate(sorted(glob.iglob(profiles_path + '/**'))):
        #supertags = find_supertags(tsuite, supertags_path)
        responses_tsuite, coverage, avg_time = run_ace(tsuite, grammar, ace_exec, ['-z', supertags_path], 'i-input', output_path)
        print('Coverage for ' + tsuite + ': ' + str(coverage))
        print('Average parsing time per sentence time for ' + tsuite + ': ' + str(avg_time))

def find_supertags(tsuite, supertags_path):
    # the tsuite name is the portion after the last slash:
    tsuite_name = tsuite.rsplit('/', 1)[-1]
    supertags = supertags_path + '/' + tsuite_name
    return supertags
