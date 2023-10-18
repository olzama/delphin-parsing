# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing experiments using fine-tuned BERT supertagger.
'''

import glob
from ace_wrapper import run_ace_on_ts, run_ace
import time
import compare_results
#class bert_supertagger:

def run(tsuite, supertags_path, grammar, ace_exec, output_path, gold_mrs, profile_name):
    print('Running experiment with BERT supertags')
    #supertags = find_supertags(tsuite, supertags_path)
    print('Testsuite: ' + tsuite + '...')
    # Measure time it took to run the experiment:
    start = time.time()
    results, n = run_ace_on_ts(tsuite, grammar, ace_exec, ['-1', '--max-chart-megabytes=24000', '--timeout=120', '-z', supertags_path], 'i-input', output_path + '/bert/' + profile_name)
    #results, n, coverage = run_ace(tsuite, grammar, ace_exec, ['-1', '-z', supertags_path], 'i-input', output_path + '/bert/' + profile_name, gold_mrs)
    end = time.time()
    t = (end - start)/n
    #print('Coverage: ' + str(coverage))
    compare_results.report_results(gold_mrs, results, output_path + '/bert/' + profile_name, t)


def find_supertags(tsuite, supertags_path):
    # the tsuite name is the portion after the last slash:
    tsuite_name = tsuite.rsplit('/', 1)[-1]
    supertags = supertags_path + '/' + tsuite_name
    return supertags
