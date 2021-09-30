#!/usr/bin/env python3

from operator import attrgetter

def greedy(dataset, max_cost):
	dataset = sorted(dataset, key=attrgetter('rate'), reverse=True)

	lower_bound, upper_bound, cost = 0, 0, 0
	combo = []
	for item in dataset:
		if cost + item.cost <= max_cost:
			lower_bound += item.profit
			cost += item.cost
			combo.append(item.name)
		elif upper_bound == 0:
			upper_bound = lower_bound + ((max_cost-cost) / item.cost) * item.profit

	return {
		'lower_bound': {
			'cost': cost,
			'profit': lower_bound,
			'items': combo
		},
		'upper_bound': max(lower_bound, upper_bound)
	}
