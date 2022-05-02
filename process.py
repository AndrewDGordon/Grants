# Started May 2

import json

funder='GB-GOR-PB188'
with open(funder+'.json') as f:
    data = json.load(f)

#print(data)

recipients = [ item['org_name'] for item in data['data'] ]
output = {'funder': funder, 'recipients': recipients}
jsonString = json.dumps(output, indent=2)

# print(jsonString)

file = r'output/'+funder+r'.json'
print(file)

myText = open(file,'w')
myText.write(jsonString)
myText.close()