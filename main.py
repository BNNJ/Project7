#!/usr/bin/env python3

import argparse
import json

from greedy	 import greedy
from bnb import bnb

from csv import DictReader
from operator import attrgetter

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
		nargs=1,
		default=500,
		help="The maximum cost"
	)

	argp.add_argument(
		"mode",
		nargs="?",
		choices=["greedy", "bnb", "dp"],
		default="greedy",
		help="Algorithm to use."
	)

	argp.add_argument(
		"input",
		help="Input file (.csv)."
	)

	return argp.parse_args()

def main():
	args = parse_args()
	file_name = args.input
	max_cost = args.max
	dataset = read_dataset(file_name)

	if args.mode == "greedy":
		result = greedy(dataset, max_cost)
	elif args.mode == "bnb":
		result = bnb(dataset, max_cost)

	print(json.dumps(result, indent=2))

if __name__ == "__main__":
	main()
