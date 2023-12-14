import glob
import json
import os

jsonFileList = glob.glob('summary-data/*.json')
output_dir = '../_datasets'

carditis_issues = []
myocarditis_list = []
pericarditis_list = []
for file in jsonFileList:
	with open(file, "r", encoding='utf-8') as f:
		data = json.load(f)
		carditis_issues.append(data)
		myocarditis_list.append(data['myocarditis_count'])
		pericarditis_list.append(data['pericarditis_count'])

sorted_issues = sorted(carditis_issues, key=lambda issue: issue['vaccine_name'])

myocarditis_sum = sum(myocarditis_list)
pericarditis_sum = sum(pericarditis_list)
total_sum = sum([myocarditis_sum, pericarditis_sum])

summary_data = {
	"carditis_summary": {
		"total": total_sum,
		"myocarditis": myocarditis_sum,
		"pericarditis": pericarditis_sum,
	},
	"carditis_issues_with_vaccine_name": sorted_issues
}

json_string = json.dumps(summary_data, ensure_ascii=False, indent=2)

output_path = os.path.join(output_dir, 'carditis-summary.json')
with open( output_path, "w", encoding='utf-8') as f:
    f.write(json_string)