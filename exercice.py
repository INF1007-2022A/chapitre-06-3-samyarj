#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers: list[list]) -> list:
	return [max(small_list) for small_list in numbers]

def join_integers(numbers: list[int]) -> int:
	result = ''
	for num in numbers:
		result += str(num)
	return int(result)

def generate_prime_numbers(limit):
	return [0]

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples) -> list[str]:
	result = []
	for i in range(1, num_combinations+1):
		if excluded_multiples == None:
			result.append(strings[0] + str(i))
			result.append(strings[1] + str(i))
		elif i % excluded_multiples != 0:
			result.append(strings[0] + str(i))
			result.append(strings[1] + str(i))
	return result

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
