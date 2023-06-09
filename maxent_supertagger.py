# Author: Olga Zamaraeva (c) 2023

'''
This program will run parsing speed experiments.
The Maxent baseline should in principle yield similar results as the baseline 2 (--ubertagging=0.001), however,
baseline2 involves a token lattice.
'''

from ace_wrapper import run_ace

class maxent_supertagger:

    def run(profiles_path, grammar, ace_exec, output_path):
        all_models_path = '/mnt/kesha/ERG/supertagging-accuracy-experiments/classic-models/repro-trunk-nonautoregress/models'
        model_path = all_models_path + '/Multinomial-L2-saga.model'
        print('Loading maxent (scikit-learn) model...')

        print('Pruning lexical types in the input profiles...')

        print('Running ACE on input pruned with maxent (scikit-learn) supertagger...')
        run_ace(profiles_path, grammar, ace_exec, ['-y'], 'p-input', output_path)
