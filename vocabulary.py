import sys
import importlib


def fuseDicts(listOfDicts):
    output={}
    for dictio in listOfDicts:
       for key, val in dictio.items():
            if key not in output:
                output[key]=val
            else:
                output[key]=output[key]+", "+val

    return output

def importVocabs(args):
    for file in args:
        try:
            importlib.import_module(file)
        except Exception as r:
            print("Failed to import "+file+".",r)

args = ["vocabulary/amazonSheet.py"]
importVocabs(args)
#ersterVokabeltest= fuseDicts([moduleOneA , amazonSheet])
#put the vocabs you actually want to practice here:
#currentVocabs=module1B
#currentVocabs=brexit
