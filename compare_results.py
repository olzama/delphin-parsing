from delphin import ace, itsdb, mrs, dmrs, edm
from delphin.codecs import simplemrs
import glob

def load_gold_mrs(tsuite):
    id2mrs = {}
    ts = itsdb.TestSuite(tsuite)
    for i,response in enumerate(ts.processed_items()):
        if len(response['results']) > 0:
            res = response.result(0)
            id2mrs[response['i-id']] = simplemrs.decode(res['mrs'])
    return id2mrs

def compare_results(gold, experimental):
    same = []
    not_same = []
    new = []
    dmrs_to_compare = []
    in_both = set(gold.keys()).intersection(set(experimental.keys()))
    only_in_gold = set(gold.keys()).difference(set(experimental.keys()))
    only_in_experimental = set(experimental.keys()).difference(set(gold.keys()))
    for id in in_both:
        if mrs.is_isomorphic(gold[id], experimental[id]):
            same.append(id)
        else:
            not_same.append(id)
    for id in only_in_gold:
        not_same.append(id)
    for id in only_in_experimental:
        new.append(id)
    return same, not_same, new

def report_results(gold_mrs, results, output_path, t):
    same, diffs, new = compare_results(gold_mrs, results)
    gold_dmrs = [dmrs.from_mrs(gm) for gm in gold_mrs.values()]
    results_dmrs = []
    for id in gold_mrs:
        if id not in results:
            results_dmrs.append(None)
        else:
            results_dmrs.append(dmrs.from_mrs(results[id]))
    edm_p, edm_r, edm_f = edm.compute(gold_dmrs, results_dmrs)
    results_str = "{} same, {} different, {}% exact match, {} sec/sen".format(len(same), len(diffs),
                                                                            len(same) / len(gold_mrs), t)
    results_str += "\n{} new parses for sentences not parsed in the gold profile".format(len(new))
    results_str += "\nEDM: P = {}, R = {}, F = {}".format(edm_p, edm_r, edm_f)
    print(results_str)
    with open(output_path + '/results.txt', 'w') as f:
        f.write(results_str)
