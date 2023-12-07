import glob, json, os
import yaml

json_file_list = glob.glob('reports-data/*.json')
output_dir = '../_datasets'


# 抽出した認定・否認一覧をひとつにまとめてファイルに保存する。
certified_reports = []
for file in json_file_list:
	with open(file, "r", encoding='utf-8') as f:
		data = json.load(f)
		certified_reports.extend(data)

sorted_reports = sorted(certified_reports, key=lambda issue: issue['certified_date'])

all_reports_json_string = json.dumps(sorted_reports, ensure_ascii=False, indent=2)
output_path = os.path.join(output_dir, 'certified-reports.json')
with open( output_path, "w", encoding='utf-8') as f:
    f.write(all_reports_json_string)


# 判定が「認定」の案件のみを対象として、症状ごとに性別で集計を実施する。
# 結果をファイルに保存する。
certified_symptoms_names_list = []
for item in sorted_reports:
	if item['judgment_result'] == '認定':
		certified_symptoms_names_list.extend(item['symptoms'])
certified_symptoms_names_set = set(certified_symptoms_names_list) # 一意な名前の一覧にする

certified_symptoms_names_dict = {s_name: { 'name': s_name, 'counts': {'male': 0, 'female': 0, 'sum': 0} } for s_name in certified_symptoms_names_set}
for item in sorted_reports:
	for symptom_name in item['symptoms']:
		# 空文字列の症状は保存されないような抽出にしているつもりなので、不要な読点「、」などがある
		# 元データの場合などの可能性あり。
		if symptom_name == "":
			print('[警告] 空白の症状名が抽出されているようです。以下の案件です。')
			print(item)
			print('-'*10)
			continue
			
		certified_symptoms_names_dict[symptom_name]['counts']['sum'] += 1
		if item['gender'] == '男':
			certified_symptoms_names_dict[symptom_name]['counts']['male'] += 1
		else:
			certified_symptoms_names_dict[symptom_name]['counts']['female'] += 1

symptom_summary_list = sorted(list(certified_symptoms_names_dict.values()), key=lambda issue: issue['name'])
symptom_summary_list_json_string = json.dumps(symptom_summary_list, ensure_ascii=False, indent=2)
output_path = os.path.join(output_dir, 'certified-symptoms.json')
with open( output_path, "w", encoding='utf-8') as f:
    f.write(symptom_summary_list_json_string)

certified_count = 0
denied_count = 0
for item in sorted_reports:
	if item['judgment_result'] == '認定':
		certified_count += 1
	elif item['judgment_result'] == '否認':
		denied_count += 1
	else:
		print(f'[警告] 認定と否認以外の判定結果が抽出されているようです')
		print(item)
		print('-'*10)

print(certified_count)
print(denied_count)
