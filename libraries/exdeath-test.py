from exdeath import (
	create_graph_data_list_by_age
)

def test_create_graph_data_list_by_age():
	data = [
		{
			"age": "71歳",
			"causal_relationship_by_expert": "γ",
		},
		{
			"age": "99歳",
			"causal_relationship_by_expert": "γ",
		},
		{
			"age": "20歳",
			"causal_relationship_by_expert": "β",
		},
		{
			"age": "79歳",
			"causal_relationship_by_expert": "γ",
		},
		{
			"age": "20歳",
			"causal_relationship_by_expert": "α",
		},
	]
	result = create_graph_data_list_by_age(data)
	assert result[0].get('x') == '20代' and result[0].get('y') == 1
	assert result[1].get('x') == '70代' and result[1].get('y') == 2
	assert result[2].get('x') == '90代' and result[0].get('y') == 1