# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing speed baseline experiments.
This baseline is the time needed to parse a set of sentences using the ACE parser without any speedups.
'''

from ace_wrapper import run_ace

class baseline1:

    def run(profiles_path, grammar, ace_exec, output_path):
        print('Running baseline 1 (no supertagging)...')
        run_ace(profiles_path, grammar, ace_exec, [], 'i-input', output_path)
