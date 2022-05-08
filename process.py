# Started May 2
# TODO given a funder, there's a set of funders that co-fund with it, and a set of fundees that are co-funded (plus a set that are only funded by the funder)
# Perhaps they could be visualized in a matrix?  why is nobody else funding those singletons?

import json

d = dict()
names = dict()

#TODO fix "/" problem in the filename XI-PB-gb/bord-na-gaidhlig.json

def process(funder):
    funder_id = funder['id']
    funder_name = funder['name']
    names[funder_id] = funder_name
    with open(funder_id+'.json') as f:
        data = json.load(f)
    recipients = [ item['org_name'] for item in data['data'] ]
    d[funder_id] = recipients
    output = {'funder': funder_id, 'recipients': recipients}
    jsonString = json.dumps(output, indent=2)
    #print(jsonString)
    file = r'output/'+funder_id+r'.json'
    #print(file)
    myText = open(file,'w')
    myText.write(jsonString)
    myText.close()

with open('inputs.json') as g:
    inputs = json.load(g)
#print(json.dumps(inputs, indent=2))

for funder in inputs['ids']:
    process(funder)

#calculate Jaccard distance between all funders
d2 = {k: set(v) for k,v in d.items()}

from itertools import combinations
distances = {(a,b): len(d2[a]&d2[b])/len(d2[a]|d2[b]) for a,b in combinations(d, 2)}

file='output.csv'
myFile = open(file,'w', encoding="utf-8")
myFile.write(f"Funder 1,Name 1,Funder 2,Name 2,Intersection,Union,Distance,Fundees in Common\n")
for (a,b),v in distances.items():
    if(v!=0):
        intersection = d2[a]&d2[b]
        union = d2[a]|d2[b]
        string_inter = "|".join(list(intersection)[0:10])
        #print(string_inter)
        myFile.write(f"{a},\"{names[a]}\",{b},\"{names[b]}\",{len(intersection)},{len(union)},{v},{string_inter}\n")
        myFile.write(f"{b},\"{names[b]}\",{a},\"{names[a]}\",{len(intersection)},{len(union)},{v},{string_inter}\n")
myFile.close()

#TODO
#calculate Jaccard distance between recipient and other recipients
recipient = "Teardrops Supporting the Homeless"
#calculate all recipients