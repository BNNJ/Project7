#!/usr/bin/env python3

import argparse
import csv
import json

from more_itertools import powerset
from timeit import default_timer as timer

def parse_args():
	argp = argparse.ArgumentParser(description="Stock invester (bruteforce version)")

	argp.add_argument(
		"input",
		help="Input file (.csv)"
	)
	return argp.parse_args()

def best_investment(dataset):
# O(n) n = len(items)
	def double_sum(items):
		profit, cost = 0, 0
		for item in items:
			profit += item['profit']
			cost += item['cost']
		return (profit, cost)

# powerset: O(2^n) n = len(dataset)
	max_profit = 0 
	for items in powerset(dataset):
		profit, cost = double_sum(items)
		if cost <= 500 and profit > max_profit:
			max_profit = profit
			max_cost = cost
			best_combo = items
	return {
		'profit': max_profit,
		'cost': max_cost,
		'items': [item['name'] for item in best_combo]
	}

def main():
	args = parse_args()
	start_time = timer()
# O(n) n = number of shares
	with open(args.input, 'r') as f:
		dataset = [
			{
				'name': row['name'],
				'cost': float(row['price']),
				'rate': float(row['profit']),
				'profit': (float(row['profit']) / 100) * float(row['price'])
			} for row in csv.DictReader(f) if row['price'] != "0.0" and row['profit'] != "0.0"
		]

	dataset = dataset[:20]

	print(json.dumps(best_investment(dataset), indent=2))
	end_time = timer()
	print(f"computed in {end_time-start_time} seconds")

if __name__ == "__main__":
	main()
