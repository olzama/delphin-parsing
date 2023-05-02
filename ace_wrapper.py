# Author: Olga Zamaraeva (c) 2023

'''
This program is a pydelphin wrapper for the ACE parser.
'''
from delphin import ace, itsdb
import glob

'''
This function will run the ACE parser on a set of sentences obtained from a [incr tsdb()] database.
Pydelphin libraries are used for both reading from the database and running the parser.
The grammar should have been compiled with the exact same version of ACE as the one used to run this program.
The cmdargs is a list of command-line arguments to pass to the ACE parser. The list can be empty.
See https://github.com/delph-in/docs/wiki/AceOptions 
'''
def run_ace(profile_path, grammar, ace_exec, cmdargs, ace_input_type, output_path):
    for i, tsuite in enumerate(sorted(glob.iglob(profile_path + '/**'))):
        ts = itsdb.TestSuite(tsuite)
        items = list(ts.processed_items())
        responses = []
        no_result = []
        with open(output_path + '/ace_err.txt', 'w') as errf:
            with ace.ACEParser(grammar, cmdargs=cmdargs, executable=ace_exec, stderr=errf) as parser:
                for response in items:
                    # Reparse each sentence, to measure the parser speed without supertagging
                    response = parser.interact(response[ace_input_type])
                    if len(response['results']) == 0:
                        no_result.append(response['input'])
                    else:
                        responses.append(response)
        with open(output_path + '/ace_err.txt', 'r') as errf:
            errors = errf.readlines()
            for ln in errors:
                print(ln)
        #with open(output_path + '/noresults.txt', 'w') as f:
        #    for i, nrs in enumerate(no_result):
        #        f.write(nrs + ': ' + errors[i] + '\n')
        return responses
