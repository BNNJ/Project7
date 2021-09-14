#!/usr/bin/env python3

import argparse
import csv
import json

# from itertools import combinations, chain, product
from more_itertools import powerset
from operator import itemgetter
from functools import reduce


def parse_args():
	argp = argparse.ArgumentParser(description="Stock invester (optimized version)")

	argp.add_argument(
		"input",
		help="Input file (.csv)"
	)

	return argp.parse_args()

def knapsack(dataset):
 
	costs = [int(item['cost']*100) for item in dataset]
	profits = [int(item['profit']) for item in dataset]

	max_cost = 50000
	n = len(profits)
	dp_table = [[0] * (max_cost+1)] * (n+1)
	for i in range(1, n+1):
		for j in range(max_cost+1):
			try:
				if costs[i-1] > j:
					dp_table[i][j] = dp_table[i-1][j]
				else:
					dp_table[i][j] = max(
						dp_table[i-1][j],
						dp_table[i-1][j-costs[i-1]] + profits[i-1]
					)
			except IndexError:
				print(i, j, costs[i-1])

	max_profit = dp_table[n][max_cost]

	return max_profit
	# current_value = max_profit
	# current_cost = 50000
	# items = []
	# for i in range(n, 0, -1):
	# 	if current_value <= 0:
	# 		break
	# 	if current_value == dp_table[i-1][current_cost]:
	# 		continue
	# 	else:
	# 		items.append(dataset[i-1])
	# 		current_value -= val[i-1]
	# 		current_cost -= costs[i-1]

	# print(items)

	# return {
	# 	'cost': [item['cost'] for item in items],
	# 	'profit': [item['profit'] for item in items],
	# 	'items': [item['name'] for item in items]
	# }

def main():
	args = parse_args()

	with open(args.input, 'r') as f:
		dataset = []
		for row in csv.DictReader(f):
			price = float(row['price'])
			profit = float(row['profit'])
			if 0 < price and profit > 0:
				dataset.append({
					'name': row['name'],
					'rate': profit,
					'cost': price,
					'profit': price / 100 * profit,
				})

	print(json.dumps(knapsack(dataset), indent=2))


if __name__ == "__main__":
	main()	