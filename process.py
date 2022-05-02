# Started May 2

import json

with open('inputs.json') as g:
    inputs = json.load(g)

print(json.dumps(inputs, indent=2))

for funder in inputs['ids']:
    print(funder)
    with open(funder+'.json') as f:
        data = json.load(f)
    recipients = [ item['org_name'] for item in data['data'] ]
    output = {'funder': funder, 'recipients': recipients}
    jsonString = json.dumps(output, indent=2)
    file = r'output/'+funder+r'.json'
    print(file)
    myText = open(file,'w')
    myText.write(jsonString)
    myText.close()