# Started May 2

import json

d = dict()

def process(funder):
    with open(funder+'.json') as f:
        data = json.load(f)
    recipients = [ item['org_name'] for item in data['data'] ]
    d[funder] = recipients
    output = {'funder': funder, 'recipients': recipients}
    jsonString = json.dumps(output, indent=2)
    #print(jsonString)
    file = r'output/'+funder+r'.json'
    #print(file)
    myText = open(file,'w')
    myText.write(jsonString)
    myText.close()

with open('inputs.json') as g:
    inputs = json.load(g)
#print(json.dumps(inputs, indent=2))

for funder in inputs['ids']:
    process(funder)

d2 = {k: set(v) for k,v in d.items()}

from itertools import combinations
distances = {(a,b): len(d2[a]&d2[b])/len(d2[a]|d2[b]) for a,b in combinations(d, 2)}

file='output.txt'
myFile = open(file,'w')
for (a,b),v in distances.items():
    if(v!=0):
        myFile.write(f"{a},{b},{v},{len(d2[a]&d2[b])},{len(d2[a]|d2[b])}\n")
myFile.close()