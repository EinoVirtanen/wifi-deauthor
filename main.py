#!/bin/python3

from subprocess import run
from sys import argv

def PrintUsage():
	quit("usage: ./main.py [wifi dev] [SSID] [whitelisted MAC] [scan freq in minutes] [debug y/n]")

if len(argv) != 6:
	PrintUsage()

if argv[5] == "y":
	debug = 1
elif argv[5] == "n":
	debug = 0
else:
	PrintUsage()

if len(argv[3].split(":")) != 6:
	PrintUsage()

dev = argv[1]
ssid = argv[2]
freq = argv[4]


