#!/usr/bin/env python3

"""
0-1 knapsack solver using a bruteforce algorithm.

usage: ./bruteforce.py [-h] input

Input should be a csv file starting with "name, price, profit",
with each following line describing a market share:
	name:	the name of the share
	price:	the buying price of the share
	profit:	the expected gain after 2 years. Not that this is NOT the
			total value of the item, as would usually be given in a standard
			knapsack problem. The value can be obtained by profit / 100 *  price
"""


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
	"""
	Return the most profitable subset of shares from the input.

	time complexity: O(2^n) with n = len(dataset)
	parameter:
		dataset: [
			{
				name: string
				cost: float
				rate: float
				profit: float
			}
		]
	return:
		{
			profit: the total profit of the selected shares
			cost: the total cost of the selected shares
			items: the names of the selected shares
		}
	"""

	def double_sum(items):
		profit, cost = 0, 0
		for item in items:
			profit += item['profit']
			cost += item['cost']
		return (profit, cost)

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
