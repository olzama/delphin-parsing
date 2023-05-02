# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing speed baseline experiments.
This baseline is the time needed to parse a set of sentences using the ACE parser with the --ubertagging option
(based on Dridan 2008, 2009, and 2013).
'''

from ace_wrapper import run_ace

class baseline2:

    def run(profiles_path, grammar, ace_exec, output_path):
        print('Running baseline 2 (--ubertagging=0.001)...')
        run_ace(profiles_path, grammar, ace_exec, ['--ubertagging=0.001'], output_path)

