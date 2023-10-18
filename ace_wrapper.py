# Author: Olga Zamaraeva (c) 2023

'''
This program is a pydelphin wrapper for the ACE parser.
'''
from delphin import ace, itsdb, mrs, dmrs
from delphin.codecs import simplemrs
import glob
import time

'''
This function will run the ACE parser on a set of sentences obtained from a [incr tsdb()] database.
Pydelphin libraries are used for both reading from the database and running the parser.
The grammar should have been compiled with the exact same version of ACE as the one used to run this program.
The cmdargs is a list of command-line arguments to pass to the ACE parser. The list can be empty.
See https://github.com/delph-in/docs/wiki/AceOptions 
'''
def run_ace(tsuite, grammar, ace_exec, cmdargs, ace_input_type, output_path, id2gold_mrs):
    ts = itsdb.TestSuite(tsuite)
    id2mrs = {}
    items = list(ts['item'])
    responses = []
    no_result = []
    with open(output_path + '/ace_err.txt', 'w') as errf:
        with ace.ACEParser(grammar, cmdargs=cmdargs, executable=ace_exec, stderr=errf) as parser:
            for item in items:
                print('Parsing ' + item['i-input'])
                response = parser.interact(item[ace_input_type])
                if len(response['results']) == 0:
                    no_result.append(item['i-input'])
                    print('*** No parse. ***')
                else:
                    responses.append(response)
                    id = item['i-id']
                    id2mrs[id] = simplemrs.decode(response['results'][0]['mrs'])
                    if id in id2gold_mrs:
                        if not mrs.is_isomorphic(id2gold_mrs[id], id2mrs[id]):
                            print('*** Different MRS ***')
                        else:
                            print('*** Same MRS ***')
                    else:
                        print('*** No gold MRS ***')
    coverage = len(responses)/len(items)
    print("Parsed {}/{} sentences".format(len(responses), len(items)))
    return id2mrs, len(items), coverage

def run_ace_on_ts(tsuite, grammar, ace_exec, cmdargs, ace_input_type, output_path):
    ts = itsdb.TestSuite(tsuite)
    with open(output_path + '/ace_err.txt', 'w') as errf:
        with ace.ACEParser(grammar, cmdargs=cmdargs, executable=ace_exec, stderr=errf) as parser:
            ts.process(parser)
    id2mrs = {}
    for i,response in enumerate(ts.processed_items()):
        if len(response['results']) > 0:
            res = response.result(0)
            id2mrs[response['i-id']] = simplemrs.decode(res['mrs'])
    print("Parsed {}/{} sentences".format(len(id2mrs), len(ts['item'])))
    return id2mrs, len(ts['item'])