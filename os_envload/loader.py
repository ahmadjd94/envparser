"""Author: Ahmad Da'na
import this function and provide the path the your .env file
Version 0.2: bug fixes and code cleanups"""

import os
import re


def load(path=""):
	"""
	load variables stored within a file into OS Environment variables
	:type path: str
	:param path: path your .env file
	:return: None
	"""
	try:
		with open(path, 'r') as fil:
			for i in fil:
				if re.match("#.*|\n", i):
					continue
				line = re.sub("""\s|\n|\t|\'|\"""", "", i)
				line = line.split("=", maxsplit=-1)
				os.environ[line[0]] = line[1]
	except FileNotFoundError as exc1:
		print(exc1)
