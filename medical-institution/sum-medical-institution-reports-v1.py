import glob, json, os, sys
import yaml
sys.path.append("../libraries")
from exmedical import (
	create_graph_by_causal_relationship,
	create_graph_severities_of_related
)

jsonFileList = glob.glob('reports-data/*.json')
output_dir = '../_datasets'

medical_institution_issues = []
for file in jsonFileList:
	with open(file, "r", encoding='utf-8') as f:
		data = json.load(f)
		for d in data:
			if type(d['no']) == type(''):
				dNo = d['no']
				dNo = dNo.split('\n')[0]
				dNo = dNo.split('注')[0]
				dNo = dNo.split('※')[0]
				dNo = dNo.split('→')[0]
				d['no'] = int(dNo)
			d['vaccine_name'] = d['vaccine_name'].replace('\n', '')
			for osd in d['onset_dates']:
				osd = osd.strip()
			for grd in d['gross_result_dates']:
				grd = grd.strip()
			for gr in d['gross_results']:
				gr = gr.strip()
			medical_institution_issues.append(d)

# 抽出した事例一覧の保存
sorted_issues = sorted(medical_institution_issues, key=lambda issue: issue['no'])
json_string = json.dumps(sorted_issues, ensure_ascii=False, indent=2)
output_path = os.path.join(output_dir, 'medical-institution-reports.json')
with open( output_path, "w", encoding='utf-8' ) as f:
	f.write(json_string)

# メタ情報と組み合わせつつ、抽出した事例一覧からいくつかの集計情報抽出を行う
with open('summary-metadata.yaml', "r", encoding='utf-8') as file:
	metadata_root = yaml.safe_load(file)
metadata = metadata_root['metadata']

sum_causal_relationship = create_graph_by_causal_relationship(sorted_issues)
sum_severities_of_related = create_graph_severities_of_related(sorted_issues)

summary_data = {
	"medical_institution_summary_from_reports": {
		"date": metadata['issues']['date'],
		"sum_causal_relationship": sum_causal_relationship,
		"sum_severities_of_related": sum_severities_of_related
	}
}

json_string = json.dumps(summary_data, ensure_ascii=False, indent=2)
output_path = os.path.join(output_dir, 'medical-institution-summary-from-reports.json')
with open( output_path, "w", encoding='utf-8') as f:
    f.write(json_string)