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

from baseline1 import baseline1

# Main function
if __name__ == '__main__':
    sentence_set = ['The cat sat on the mat.', 'The dog sat on the mat.', 'The cat sat on the dog.']
    # Run baseline 1
    baseline1_results = baseline1.run(sentence_set)
    pass