#!/usr/bin/python3

import sys

length = len(sys.argv)
summation = 0


if __name__ == '__main__':
	if length == 1:
		summation = 0
	else:
		for i in range(1, length):
			
			summation += int(sys.argv[i])
		print("{:d}".format(summation))
	
	
