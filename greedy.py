#!/usr/bin/env python3

import argparse
import csv
import json

from operator import itemgetter

def parse_args():
	argp = argparse.ArgumentParser(description="Stock invester (greedy version)")

	argp.add_argument(
		"input",
		help="Input file (.csv)"
	)
	return argp.parse_args()

def best_investment(dataset):

	dataset = sorted(dataset, key=itemgetter('rate'), reverse=True)

	profit, cost = 0, 0
	combo = []
	for item in dataset:
		if cost + item['cost'] <= 500:
			profit += item['profit']
			cost += item['cost']
			combo.append(item['name'])

	return {
		'profit': profit,
		'cost': cost,
		'items': combo
	}

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

	print(json.dumps(best_investment(dataset), indent=2))

if __name__ == "__main__":
	main()
