#!/bin/python3

from subprocess import run
from sys import argv
from os import geteuid

if geteuid() != 0:
	quit("root required")

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

if debug:
	print("# attempting to kill processes intervening with airmon-ng")

run(["airmon-ng", "check", "kill"])

if debug:
	print("# starting airmon-ng on interface", dev)

run(["airmon-ng", "start", dev])

if debug:
	print("# running airodump-ng on", dev)

run(["airodump-ng", dev])

# while loop with the frequency
# scan channel by channel

