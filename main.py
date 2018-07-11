#!/bin/python3

import subprocess
import sys

def PrintUsage():
	quit("usage: ./main.py [wifi dev] [SSID] [scan freq in minutes] [debug y/n]")

def ParseArgv():
	if len(sys.argv) != 5:
		PrintUsage()

	if sys.argv[4] == "y":
		debug = 1
	elif sys.argv[4] == "n":
		debug = 0
	else:
		PrintUsage()

	dev = sys.argv[1]
	ssid = sys.argv[2]
	freq = sys.argv[3]

def main():
	ParseArgv()
	
main()
