#!/usr/bin/env python

import sys
import os
import os.path
import re

def printHelpMessage(error):
	print("\nError: " + error + "\n\nUsage: python Tractatus [name of original file] [name of output file]\n\nSee the readme file for further instructions.\n")
	sys.exit()

# Check if enough arguments have been given.
if len(sys.argv) < 2:
	printHelpMessage("To few arguments given.")

# Check if the input file exists.
if not (os.path.isfile(sys.argv[1]) and os.access(sys.argv[1], os.R_OK)):
	printHelpMessage("Input file is either missing or is not readable.")

# Fetch the filename of the input file from system input
inputFilename = sys.argv[1]

# Fetch the filename of the output file from system input
outputFilename = sys.argv[2]

# Fetch list of commands that should be used to indicate which lines should be affected.
listOfCommands = "@"

# Read the file into a list.
with open(inputFilename) as f:
    content = f.readlines()

outputContent = []

# Go through each line in the list.
for a, line in enumerate(content):
	commandFound = False
	# Remove tabs.
	line = line.replace('\t', '')
	# Go through each command in the command list.
	for command in listOfCommands:
		if command in line[0]:
			commandFound = True
			break
	if not commandFound:
		outputContent.append(line)

# Write the list to a new file.
output = open(outputFilename, "w")
output.writelines(outputContent)
output.close()
