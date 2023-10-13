# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing speed baseline experiments.
This baseline is the time needed to parse a set of sentences using the ACE parser without any speedups.
'''

from ace_wrapper import run_ace_on_ts, run_ace
import time
import compare_results


def run(tsuite, grammar, ace_exec, output_path, gold_mrs, profile_name):
    print('Running baseline 1 (no supertagging)...')
    # Measure time it took to run the experiment:
    start = time.time()
    #results, n = run_ace_on_ts(tsuite, grammar, ace_exec, ['-1'], 'i-input', output_path + '/baseline1/' + profile_name)
    results, n, coverage = run_ace(tsuite, grammar, ace_exec, ['-1'], 'i-input', output_path + '/baseline1/' + profile_name, gold_mrs)
    end = time.time()
    t = (end - start)/n
    #print('Coverage: ' + str(coverage))
    compare_results.report_results(gold_mrs, results, output_path + '/baseline1/' + profile_name, t)

