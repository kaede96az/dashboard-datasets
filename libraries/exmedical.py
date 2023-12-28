def create_graph_by_causal_relationship(issues):
	graph = dict()

	for issue in issues:
		cr = issue['causal_relationship']
		if cr == '':
			if '空白' in graph:
				graph['空白'] += 1
			else:
				graph['空白'] = 1
		else:
			if cr in graph:
				graph[cr] += 1
			else:
				graph[cr] = 1
	
	return graph


def create_graph_severities_of_related(issues):
	graph = dict()

	for issue in issues:
		if issue['causal_relationship'].find('関連あり') == -1:
			continue
		sv = issue['severity']
		if sv == '':
			if '空白' in graph:
				graph['空白'] += 1
			else:
				graph['空白'] = 1
		else:
			if sv in graph:
				graph[sv] += 1
			else:
				graph[sv] = 1
	
	return graph