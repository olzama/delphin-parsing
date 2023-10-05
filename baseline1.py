# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing speed baseline experiments.
This baseline is the time needed to parse a set of sentences using the ACE parser without any speedups.
'''

import glob
from ace_wrapper import run_ace_on_ts
import time

#class baseline1:

def run(profiles_path, grammar, ace_exec, output_path):
    print('Running baseline 1 (no supertagging)...')
    responses = []
    for i, tsuite in enumerate(sorted(glob.iglob(profiles_path + '/**'))):
        # Measure time it took to run the experiment:
        start = time.time()
        results, n = run_ace_on_ts(tsuite, grammar, ace_exec, ['-1','--timeout=10'], 'i-input', output_path)
        end = time.time()
        t = (end - start)/n
        #responses_tsuite, coverage, avg_time = run_ace(tsuite, grammar, ace_exec, ["-1"], 'i-input', output_path)
        #responses.extend(responses_tsuite)
        #print('Coverage for ' + tsuite + ': ' + str(coverage))
        #print('Average parsing time per sentence time for ' + tsuite + ': ' + str(avg_time))
        return results, t

