from delphin import ace, itsdb, mrs, dmrs
from delphin.codecs import simplemrs
import glob

def load_gold_mrs(profiles_path):
    dmrs_lst = []
    id2mrs = {}
    for tsuite in sorted(glob.iglob(profiles_path + '/**')):
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