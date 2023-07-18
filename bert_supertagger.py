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
        supertags = "/media/olga/lapka/BERT/erg/output/pestpredictions.txt"
        run_ace(tsuite, grammar, ace_exec, ['-z', supertags], 'i-input', output_path)

def find_supertags(tsuite, supertags_path):
    # the tsuite name is the portion after the last slash:
    tsuite_name = tsuite.rsplit('/', 1)[-1]
    supertags = supertags_path + '/' + tsuite_name
    return supertags