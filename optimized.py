#!/usr/bin/env python3

import argparse
import json

from greedy	 import greedy
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

def parse_args():
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
	if isinstance(data, float):
		return round(data, 2)
	if isinstance(data, dict):
		for k, v in data.items():
			data[k] = round_floats(v)
	return data


def main():
	args = parse_args()
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

	if not args.accurate:
		round_floats(result)

	print(json.dumps(result, indent=2))

	end = timer()
	print(f"computed in {end-start} seconds")

if __name__ == "__main__":
	main()
