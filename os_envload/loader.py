"""Author: Ahmad Da'na
import this function and provide the path the your .env file """

import os
import re
__all__ = ("load",)

def load(path=""):
	"""
	load environment variables from text file
	:type path: str
	:param path: path your .env file
	:return: None
	"""
	with open(path, 'r') as fil:
		for i in fil:
			if re.match("#.*|\n", i):
				continue
			line = re.sub("""\s|\n|\t|\'|\"""", "", i)
			line = line.split("=")
			os.environ[line[0]] = line[1]
