#!/usr/bin/env python3

from operator import attrgetter

def greedy(dataset, max_cost):
	dataset = sorted(dataset, key=attrgetter('rate'), reverse=True)

	profit, cost = 0, 0
	combo = []
	for item in dataset:
		if cost + item.cost <= max_cost:
			profit += item.profit
			cost += item.cost
			combo.append(item.name)

	return {
		'cost': cost,
		'profit': profit,
		'items': combo
	}
