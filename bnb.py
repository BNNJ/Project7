#!/usr/bin/env python3

from queue import PriorityQueue
from operator import attrgetter

class Node:
	def __init__(self, item, item_index, available, cost):
		self.item = item
		self.item_index = item_index
		self.available = available
		self.cost = cost
		self.lower_bound, self.upper_bound = bound(available)
		self._items = None

	def __lt__(self, other):
		return self.upper_bound > other.upper_bound
	def __gt__(self, other):
		return self.upper_bound < other.upper_bound
	def __le__(self, other):
		return not self.__gt__(other)
	def __ge__(self, other):
		return not self.__lt__(other)
	def __eq__(self, other):
		return self.upper_bound == other.upper_bound
	def __ne__(self, other):
		return not self.__eq__(other)

def bound(available):
	lower_bound, upper_bound, cost = 0, 0, 0
	for i, item in enumerate(ITEMS):
		if available >> i & 1 == 0:
			continue
		if cost + item.cost <= MAX_COST:
			cost += item.cost
			lower_bound += item.profit
		elif upper_bound == 0:
			upper_bound = lower_bound + ((MAX_COST-cost) / item.cost) * item.profit
			break
	upper_bound = max(lower_bound, upper_bound)
	return lower_bound, upper_bound

def explore(parent):
	index = parent.item_index + 1
	item = ITEMS[index]
	inc = parent.available
	exc = parent.available & ~(1 << index)
	return (
		Node(item, index, inc, parent.cost + item.cost),
		Node(item, index, exc, parent.cost)
	)

def bnb(dataset, max_cost):
	cost, profit, items = 0, 0, []
	dataset = sorted(dataset, key=attrgetter('rate'), reverse=True)
	global MAX_COST, ITEMS
	MAX_COST, ITEMS = max_cost, dataset

	pending = PriorityQueue()

	# makes a `bitfield` of size len(dataset) filled with 1s
	available = (1 << len(dataset)) - 1

	root = Node(None, -1, available, 0)
	current_node = root
	while current_node.item != dataset[-1]:
		inc, exc = explore(current_node)
		if inc.cost <= MAX_COST:
			pending.put(inc)
		pending.put(exc)	
		current_node = pending.get()

	selected = current_node.available
	result = {
		'cost': round(sum([item.cost for i, item in enumerate(dataset) if selected & 1 << i]), 4),
		'profit': round(sum([item.profit for i, item in enumerate(dataset) if selected & 1 << i]), 4),
		'items': [item.name for i, item in enumerate(dataset) if selected & 1 << i],
	}
	return result

def main():
	pass
	# while not q.empty()

if __name__ == "__main__":
	global ITEMS
	ITEMS = [1, 2, 3, 4, 5]
	sel = 0b10011
	print(get_items(sel))
