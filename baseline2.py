# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing speed baseline experiments.
This baseline is the time needed to parse a set of sentences using the ACE parser with the --ubertagging option
(based on Dridan 2008, 2009, and 2013).
'''

from ace_wrapper import run_ace_on_ts, run_ace
import time
import compare_results

def run(tsuite, grammar, ace_exec, output_path, gold_mrs, profile_name):
    print('Running baseline 2 (--ubertagging=0.001)...')
    responses = []
    # Measure time it took to run the experiment:
    start = time.time()
    results, n = run_ace_on_ts(tsuite, grammar, ace_exec, ['-1','--ubertagging=0.001', '--max-chart-megabytes=24000', '--max-unpack-megabytes=32000'],
                               'i-input', output_path + '/baseline2/' + profile_name)
    #results, n, coverage = run_ace(tsuite, grammar, ace_exec, ['-1', '--ubertagging=0.001'], 'i-input',
    #                           output_path + '/baseline2/' + profile_name, gold_mrs)
    end = time.time()
    t = (end - start)/n
    #print('Coverage: ' + str(coverage))
    compare_results.report_results(gold_mrs, results, output_path + '/baseline2/' + profile_name, t)



