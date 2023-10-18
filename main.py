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

import sys, os
import baseline1
import baseline2
import maxent_supertagger
import bert_supertagger
import compare_results


# Create directories under output_path/baseline1, output_path/baseline2, and output_path/bert, named same as gold_profile:
def set_up_experiment(output_path, gold_path, gold_profile):
    baseline1_profile = output_path + '/baseline1/'
    baseline2_profile = output_path + '/baseline2/'
    bert_profile = output_path + '/bert/'
    # Create new directories unless they already exist:
    if not os.path.exists(baseline1_profile):
        os.makedirs(baseline1_profile)
    if not os.path.exists(baseline2_profile):
        os.makedirs(baseline2_profile)
    if not os.path.exists(bert_profile):
        os.makedirs(bert_profile)
    # Clear the directories:
    os.system('rm -rf ' + baseline1_profile + gold_profile + '/*')
    os.system('rm -rf ' + baseline2_profile + gold_profile + '/*')
    os.system('rm -rf ' + bert_profile + gold_profile + '/*')
    # Copy the gold profile to the three new directories:
    os.system('cp -r ' + gold_path + ' ' + baseline1_profile)
    os.system('cp -r ' + gold_path + ' ' + baseline2_profile)
    os.system('cp -r ' + gold_path + ' ' + bert_profile)
    # uncompress any .gz files:
    os.system('gunzip ' + baseline1_profile + gold_profile + '/*.gz')
    os.system('gunzip ' + baseline2_profile + gold_profile + '/*.gz')
    os.system('gunzip ' + bert_profile + gold_profile + '/*.gz')
    return baseline1_profile+gold_profile, baseline2_profile+gold_profile, bert_profile+gold_profile


# Main function
if __name__ == '__main__':
    gold_profile = sys.argv[1]
    gold_path = "/home/olga/delphin/erg/trunk/tsdb/gold/" + gold_profile
    grammar = sys.argv[2]
    ace_exec1 = sys.argv[3]
    output_path = sys.argv[4]
    supertags_path = sys.argv[5] + '/' + gold_profile + '/'
    ubertag_grammar = sys.argv[6]
    ace_exec2 = sys.argv[7]
    run_all = sys.argv[8]
    baseline1_profile, baseline2_profile, bert_profile = set_up_experiment(output_path, gold_path, gold_profile)
    # Extract gold MRS:
    gold_mrs = compare_results.load_gold_mrs(gold_path)
    if run_all == 'all':
        # Run baseline 1
        baseline1.run(baseline1_profile, grammar, ace_exec1, output_path, gold_mrs, gold_profile)
    # Run baseline 2
    baseline2.run(baseline2_profile, ubertag_grammar, ace_exec2, output_path, gold_mrs, gold_profile)
    # Run experiments:
    # 1. Maxent
    # maxent_results = maxent_supertagger.run(profiles, grammar, ace_exec, output_path)
    # 2. NCRF++
    # 3. BERT
    bert_supertagger.run(bert_profile, supertags_path, grammar, ace_exec1, output_path, gold_mrs, gold_profile)
