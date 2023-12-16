import re, sys, traceback

def create_graph_data_list_by_age(data):
	'''
	10代、20代などざっくりした年齢に対して人数をカウントして返す。

	Parameters
    ----------
    data: []
		PDFから抽出した死亡事例の一覧情報

    Returns
    -------
	result: dict
		{'0代': 1, '10代': 17, (以下略
	'''

	result = dict()
	for d in data:
		if d['causal_relationship_by_expert'] == 'β':
			# ワクチンと死亡が否定されているものだけ除外
			continue

		age_str = d['age'].split('歳')[0]
		if not age_str.isdecimal():
			# 年齢が数字に変換できない場合は、計算できないので除外
			continue
		generation = select_ages(int(age_str))
		if generation in result:
			result[generation] += 1
		else:
			result[generation] = 1
	
	# 文字列のままだと10代, 100代, 20代・・という順になるので、一旦数字にしてソート
	result_list = sorted(result.items(), key=lambda x: int(x[0].replace('代', '')))

	age_list = []
	for r in result_list:
		age_list.append({'x': r[0], 'y': r[1]})

	return age_list


def select_ages(age):
	if 0 <= age < 10:
		return '0代'
	elif 10 <= age < 20:
		return '10代'
	elif 20 <= age < 30:
		return '20代'
	elif 30 <= age < 40:
		return '30代'
	elif 40 <= age < 50:
		return '40代'
	elif 50 <= age < 60:
		return '50代'
	elif 60 <= age < 70:
		return '60代'
	elif 70 <= age < 80:
		return '70代'
	elif 80 <= age < 90:
		return '80代'
	elif 90 <= age < 100:
		return '90代'
	elif 100 <= age < 110:
		return '100代'
	elif 110 <= age < 120:
		return '110代'
	elif 120 <= age < 130:
		return '120代'
	else:
		print(f'特殊な年齢: {age}')
		return '長寿'