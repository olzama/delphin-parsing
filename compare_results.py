from delphin import ace, itsdb, mrs, dmrs
from delphin.codecs import simplemrs
import glob

def load_gold_mrs(tsuite):
    dmrs_lst = []
    id2mrs = {}
    ts = itsdb.TestSuite(tsuite)
    for i,res in enumerate(ts['result']):
        id = ts['item'][i]['i-id']
        dmrs_lst.append(dmrs.from_mrs(simplemrs.decode(res['mrs'])))
        id2mrs[id] = simplemrs.decode(res['mrs'])
    return id2mrs

def compare_results(gold, experimental):
    same = []
    not_same = []
    for id in gold:
        if id not in experimental:
            not_same.append(id)
        else:
            mrs_i = gold[id]
            if mrs.is_isomorphic(mrs_i, experimental[id]):
                same.append(id)
            else:
                not_same.append(id)
    return same, not_same

def report_results(gold_mrs, results, output_path, t):
    same, diffs = compare_results(gold_mrs, results)
    results_str = "{} same, {} different, {}% exact match, {} sec/sen".format(len(same), len(diffs),
                                                                            len(same) / len(gold_mrs), t)
    print(results_str)
    with open(output_path + '/results.txt', 'w') as f:
        f.write(results_str)
