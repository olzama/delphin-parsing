# Olga Zamaraeva (c) 2023

'''
This program will run parsing speed experiments.
Baseline 1 is the time needed to parse a set of sentences using the ACE parser.
Baseline 2 (English only) is the time needed to parse the same set of sentences using the old --ubertagging option
for the ACE parser (based on Dridan 2008, 2009, and 2013).
The experimental results will be the time needed to parse the same set of sentences using models trained with
fine-tuning BERT as well as NCRF++ and classic SVM models.

In addition to the parsing speed, accuracy will need to be measured (whether the parses are correct) but that may
have to be done separately, via partially manual treebanking.
'''

import sys
from baseline1 import baseline1
from baseline2 import baseline2

# Main function
if __name__ == '__main__':
    profiles = sys.argv[1]
    grammar = sys.argv[2]
    ace_exec = sys.argv[3]
    output_path = sys.argv[4]
    # Run baseline 1
    baseline1_results = baseline1.run(profiles, grammar, ace_exec, output_path)
    # Run baseline 2
    baseline2_results = baseline2.run(profiles, grammar, ace_exec, output_path)
    # Run experiments:
    # 1. Maxent


