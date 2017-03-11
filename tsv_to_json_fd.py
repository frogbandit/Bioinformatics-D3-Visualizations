import csv
import json

import time

start = time.time()
start_process = time.clock()

nodes = []
drug_list = []
pair_dict = {}
effect_list = []

links = []

group_number = 1
# umls_dict = {}
# num_lines = 0

# with open("offsides_first1500.tsv") as tsv:
# 	next(tsv)
# 	for line in csv.reader(tsv, dialect="excel-tab"):
# 		umls_id = line[2]
# 		if umls_id not in umls_dict:
# 			umls_dict[umls_id] = group_number
# 			group_number += 1

with open("offsides.tsv") as tsv:
	next(tsv)
	for line in csv.reader(tsv, dialect="excel-tab"):
		drug = line[1]
		umls_id = line[2]
		effect = line[3]
		value = line[7] 

		if drug not in drug_list:
			drug_list.append(drug)
			# drug_dict = {"name": drug, "group": umls_dict[umls_id]}
			# nodes.append(drug_dict)

		if effect not in effect_list:
			effect_list.append(effect)
			# effect_dict = {"name": effect, "group": umls_dict[umls_id]}
			# nodes.append(effect_dict)

	for drug in drug_list:
		drug_dict = {"id": drug, "group": group_number}
		group_number += 1
		nodes.append(drug_dict)

	for effect in effect_list:
		effect_dict = {"id": effect, "group": group_number}
		group_number += 1
		nodes.append(effect_dict)


with open("offsides.tsv") as tsv:
	next(tsv)
	for line in csv.reader(tsv, dialect="excel-tab"):
		drug = line[1]
		effect = line[3]
		value = line[7]

		try:
 			drug_index = drug_list.index(drug)
 			effect_index = effect_list.index(effect)
 		except ValueError:
 			continue

		links_dict = {"source": drug, "target": effect, "value": float(value)}
			
		if links_dict not in links:
  			links.append(links_dict)

data = {"nodes": nodes, "links": links}

with open('templates/offsides_every20.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, separators=(',', ': '))



end = time.time()
end_process = time.clock() 
print "time: " + str(end - start)
print "process time: " + str(end_process - start_process)

