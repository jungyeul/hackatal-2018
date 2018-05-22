#python3

'''
Evaluation script made for the Hackathon 2018
possible classes : 'fakeNews' 'trusted' 'satire'

example : python3 eval-hackathon2018.py -g data/hackatal-data/test2/storyzy_en_test2_full.tsv -p data/hackatal-data/test2/storyzy_en_test2_full.tsv -s


@author: Gael Guibon
'''

import csv, argparse
from random import shuffle
from collections import OrderedDict


type_col = 2
id_col = 0

id_pred_col = 0
type_pred_col = 1

class metrics():
    def f1(precision,recall):
        return (2.0*precision*recall)/(precision+recall)

    def precision(gold_rows, pred_rows, classname):
        prec = 0
        n_pred = [pred for pred in pred_rows if pred[type_pred_col] == classname]
        for gold, pred in zip(gold_rows, pred_rows):
            if pred[type_pred_col] == classname and gold[type_col] == pred[type_pred_col]:
                    prec+=1

        return prec/len(n_pred)

    def recall(gold_rows, pred_rows, classname):
        rec = 0
        n_gold = [gold for gold in gold_rows if gold[type_col] == classname]
        for gold, pred in zip(gold_rows, pred_rows):
            if pred[type_pred_col] == classname and gold[type_col] == pred[type_pred_col]:
                    rec+=1
        return rec/len(n_gold)

def read_csv(p, pred=False):
    with open(p, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter='\t')#, quotechar='"')
        rows = [row for row in data]
        if not pred:
            global type_col 
            type_col = rows[0].index("type")
            global id_col 
            id_col = rows[0].index("id")
        else:
            global type_pred_col 
            type_pred_col = rows[0].index("type")
            global id_pred_col 
            id_pred_col = rows[0].index("id")
        return rows[1:], ['fakeNews', 'trusted', 'satire']

def read_csv_nosatire(p, pred=False):
    with open(p, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter='\t')#, quotechar='"')
        rows = [row for row in data]
        merged = list()
        if not pred:
            global type_col 
            type_col = rows[0].index("type")
            global id_col 
            id_col = rows[0].index("id")
        else:
            global type_pred_col 
            type_pred_col = rows[0].index("type")
            global id_pred_col 
            id_pred_col = rows[0].index("id")
        if pred:
            for row in rows :
                row[type_pred_col] = row[type_pred_col].replace('satire', 'fakeNews')
                merged.append(row)
        else:
            for row in rows :
                row[type_col] = row[type_col].replace('satire', 'fakeNews')
                merged.append(row)
        return merged[1:], ['fakeNews', 'trusted']

def reorder(rows):
    d = {row[id_col]: row for row in rows}
    sorteddict = OrderedDict(sorted(d.items()))
    return list(sorteddict.values())




def startEval(gold, pred, classes):
    '''
    Start evaluation based on two lists : pred and gold. (list (rows) of lists (columns))
    '''
    precisions = list()
    recalls = list()
    f1scores = list()
    gold, pred = reorder(gold), reorder(pred)
    res = list()
    for c in classes:
        precision = metrics.precision(gold, pred, c) 
        precisions.append(precision)
        recall = metrics.recall(gold, pred, c)
        recalls.append(recall) 
        f1 = metrics.f1(precision, recall)
        f1scores.append(f1)
        res.append('{}\tPrecision\t{}\tRecall\t{}\tF1\t{}'.format(c, precision, recall, f1) )
    res.append( '{}\tPrecision\t{}\tRecall\t{}\tF1\t{}'.format('TOTAL', sum(precisions)/len(precisions), sum(recalls)/len(recalls), sum(f1scores)/len(f1scores) ) )
    return '\n'.join(res)

def eval(goldpath, predpath, satire=False):
    '''
    Shortcut for programmatic usage.
    '''
    if satire :
        gold, classes = read_csv(args.gold)
        pred, classes = read_csv(args.pred, pred=True)
    else :
        gold, classes = read_csv_nosatire(args.gold)
        pred, classes = read_csv_nosatire(args.pred, pred=True)

    gold = reorder(gold)
    pred = reorder(pred)
    res = startEval(gold, pred, classes)
    return res 


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gold", help="gold path file")#, action="store_true")
    parser.add_argument("-p", "--pred", help="pred path file")
    parser.add_argument("-s", "--satire", help="include satire (only for english)", action="store_true")
    args = parser.parse_args()
    
    if args.satire :
        gold, classes = read_csv(args.gold)
        pred, classes = read_csv(args.pred, pred=True)
    else :
        gold, classes = read_csv_nosatire(args.gold)
        pred, classes = read_csv_nosatire(args.pred, pred=True)

    gold = reorder(gold)
    pred = reorder(pred)
    print(id_col, type_col, id_pred_col, type_pred_col)
    print(startEval(gold, pred, classes))

