import json
import itertools
import more_itertools as mit
import numpy as np

weights = {"Moderate":1.0,"Minor":0.4}

f = open('final_drugs.json')
temp = json.load(f)
db = {}
for a in temp:
    if len(a["diseases"]) != 0:
        sranie = {
            "drug_interactions": {b["name"]: b["class"] for b in a["drug_interactions"]},
            "diseases":a["diseases"]
            }
        db[a["drug name"]] = sranie

db_keys = list(db.keys())

def sorting(lis):
    
    temp = [np.sum([weights[db[b1]["drug_interactions"][b2]]for b1, b2 in itertools.combinations(a,2)]) for a in lis]
    return np.array(lis)[np.argsort(temp)].tolist()
    
def findDrugs(disieses, banned = [], redundant=False):
    subsets = [set(x) for x in list(mit.powerset(disieses))[1:]]
    #wyfiltrować banned
    unga=set(disieses)
    helper = {str(idx):{0:[]} for idx in subsets}
    for i in range(1,len(db_keys)+1):
        for subset in subsets:
            helper[str(subset)][i] = [*helper[str(subset)][i-1]]
            if db_keys[i-1] not in banned:
                intersec = set(db[db_keys[i-1]]["diseases"]).intersection(unga)
                if intersec == subset:
                    helper[str(subset)][i] += [[i-1]]
                if not intersec.difference(subset):                                                   
                    names = [str(subset.difference(set(s))) for s in list(mit.powerset(intersec)) if str(subset.difference(set(s))) != 'set()']
                    if redundant:
                        names=names[1:]
                    for name in names:
                        for a in list(itertools.product(helper[name][i - 1], [[i - 1]])):
                            wrong = False
                            for b in a[0]:
                                try:
                                    if db[db_keys[b]]["drug_interactions"][db_keys[a[1]]] == "Major":
                                        wrong = True
                                        break
                                except:
                                    print("pass")
                            if not wrong:
                                helper[str(subset)][i] += [a[0] + a[1] for a in list(itertools.product(helper[name][i - 1], [[i - 1]]))]

    result = helper[list(helper.keys())[-1]][len(db_keys)]
    result = [[db_keys[b] for b in a ] for a in result]
    return sorting(result)

def findBest(lis, ill):

    found = {}
    for key in db_keys:
        if ill in db[key]["diseases"]:
            works = True
            score=0
            for el in lis:
                try:
                    if db[el]["drug_interactions"][key] == "Major":
                        works = False
                        break
                    score += weights[db[el]["drug_interactions"][key]]
                except:
                    "pass"
            if works:
                found[key] = score
    # zwrócić minimalną wartość z dictu = chillera




    
print(findDrugs(["Hydrocephalus"]))
