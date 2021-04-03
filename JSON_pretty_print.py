
import simplejson as json
import pprint

json_file = open('data/TravLITE_NPCs.json', 'r')
just_read_in = json.load(json_file)
json_file.close()

for traveller in just_read_in['NPCs']:
    pprint.pprint (traveller)
    print
    print