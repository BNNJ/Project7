#!/usr/bin/env python3

"""
0-1 knapsack solver using either a branch and bound (default) or greedy algorithm.

usage: ./optimized.py [-h] [-m MAX] [-g] [-a] input
	-h		help
	-m MAX	the maximum cost constraint
	-g		use the greedy algorithm
	-a		don't round results to 2 decimals
	input	input file

Input should be a csv file starting with "name, price, profit",
with each following line describing a market share:
	name:	the name of the share
	price:	the buying price of the share
	profit:	the expected gain after 2 years. Not that this is NOT the
			total value of the item, as would usually be given in a standard
			knapsack problem. The value can be obtained by profit / 100 *  price
"""

import argparse
import json

from greedy import greedy
from bnb import bnb
from timeit import default_timer as timer

from csv import DictReader

class Share:
	def __init__(self, name, cost, rate):
		self.name = name
		self.cost = float(cost)
		self.rate = float(rate)
		self.profit = cost * rate / 100

	def __str__(self):
		return f"{self.name}: cost = {self.cost}, rate = {self.rate}, profit = {self.profit}"

def read_dataset(file_name):
	"""Read a csv file and return a list of Share instances."""
	dataset = []
	with open(file_name, 'r') as f:
		for row in DictReader(f):
			price = float(row['price'])
			profit = float(row['profit'])
			if price > 0 and profit > 0:
				dataset.append(Share(
					name=row['name'],
					cost=price,
					rate=profit
				))
	return dataset

def _parse_args():
	argp = argparse.ArgumentParser(description="Stock invester (optimized version)")

	argp.add_argument(
		"-m", "--max",
		type=int,
		default=500,
		help="The maximum cost"
	)

	argp.add_argument(
		"-g", "--greedy",
		action="store_true",
		help="Greedy mode, useful to get lower and upper bounds"
	)

	argp.add_argument(
		"-a", "--accurate",
		action="store_true",
		help="Disable rounding floats to 2 decimals"
	)

	argp.add_argument(
		"input",
		help="Input file (.csv)."
	)

	return argp.parse_args()

def round_floats(data):
	"""Return a rounded-float version of the input data"""
	if isinstance(data, float):
		return round(data, 2)
	if isinstance(data, dict):
		for k, v in data.items():
			data[k] = round_floats(v)
	return data

def _main():
	args = _parse_args()
	file_name = args.input
	max_cost = args.max
	dataset = read_dataset(file_name)

	start = timer()
	if args.greedy:
		print(f"Using greedy Algorithm...")
		result = greedy(dataset, max_cost)
	else:
		print(f"Using branch and bound Algorithm...")
		result = bnb(dataset, max_cost)

	end = timer()

	if not args.accurate:
		round_floats(result)

	print(json.dumps(result, indent=2))
	print(f"computed in {end-start} seconds")

if __name__ == "__main__":
	_main()
