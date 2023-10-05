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
import baseline1
import baseline2
import maxent_supertagger
import bert_supertagger
import compare_results

# Main function
if __name__ == '__main__':
    profiles = sys.argv[1]
    grammar = sys.argv[2]
    ace_exec = sys.argv[3]
    output_path = sys.argv[4]
    gold_profiles = sys.argv[5]
    # Extract gold MRS:
    gold_mrs = compare_results.load_gold_mrs(gold_profiles)
    # Run baseline 1
    baseline1_results, time_per_sentence_baseline = baseline1.run(profiles, grammar, ace_exec, output_path)
    same_baseline, diffs_baseline = compare_results.compare_results(gold_mrs, baseline1_results)
    # Run baseline 2
    #baseline2_results = baseline2.run(profiles, grammar, ace_exec, output_path)
    # Run experiments:
    # 1. Maxent
    # maxent_results = maxent_supertagger.run(profiles, grammar, ace_exec, output_path)
    # 2. NCRF++
    # 3. BERT
    supertags_path = sys.argv[6]
    bert_results, time_per_sentence_bert = bert_supertagger.run(profiles, supertags_path, grammar, ace_exec, output_path)
    same_bert, diffs_bert = compare_results.compare_results(gold_mrs, bert_results)
    print("Baseline: {} same, {} different, {}% exact match, {} seconds per sentence".format(len(same_baseline),
                                                                                             len(diffs_baseline),
                                                                                             len(same_baseline)/len(gold_mrs),
                                                                                             time_per_sentence_baseline))
    print("BERT: {} same, {} different {}% exact match, {} seconds per sentence".format(len(same_bert), len(diffs_bert),
                                                                                        len(same_bert)/len(gold_mrs),
                                                                                        time_per_sentence_bert))

