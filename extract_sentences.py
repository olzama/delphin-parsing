from delphin import ace, itsdb
import sys, glob

def extract_sentences(tsuite):
    ts = itsdb.TestSuite(tsuite)
    items = list(ts.processed_items())
    sentences = []
    for item in items:
        sentences.append(item['i-input'])
    return sentences

if __name__ == '__main__':
    tsuite_path = sys.argv[1]
    output_path = sys.argv[2]
    sentences = extract_sentences(tsuite_path)
    with open(output_path, 'w') as f:
        for s in sentences:
            f.write(s + '\n')
