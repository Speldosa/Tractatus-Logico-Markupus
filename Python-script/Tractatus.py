#!/usr/bin/env python

# Import necessary libraries.
import sys
import os.path

def printHelpMessage(error):
	print("\nError: " + error + "\n\nUsage: python Tractatus [name of original file] [name of output file]\n\nSee the readme file for further instructions.\n")
	sys.exit()

# Check if enough arguments have been given.
if len(sys.argv) < 2:
	printHelpMessage("Too few arguments given.")

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
	# Remove leading and trailing whitespace the line might have.
	line = line.strip()
	# Put back the new line command at the end of the line.
	line = line + "\n"
	# Go through each command in the commands list until a match for the first character of the line is found.
	for command in listOfCommands:
		if command in line[0]:
			commandFound = True
			break
	# If the line is to be kept...
	if not commandFound:
		if len(outputContent) != 0:
			last_saved_line = outputContent[len(outputContent)-1]
			# If the current line or the last saved line isn't just a new line, remove the new line command from the end of the last saved line and add a space to it. This means that lines without blank lines between them will form single paragraphs.
			if line != "\n":
				if last_saved_line != "\n":
					outputContent[len(outputContent)-1] =  outputContent[len(outputContent)-1][:-1]
					outputContent[len(outputContent)-1] = outputContent[len(outputContent)-1] + " "
		outputContent.append(line)

# If the last saved line isn't just a new line, remove the new line command at the end.
last_saved_line = outputContent[len(outputContent)-1]
if last_saved_line != "\n":
	outputContent[len(outputContent)-1] =  outputContent[len(outputContent)-1][:-1]

# Write the list to a new file.
output = open(outputFilename, "w")
output.writelines(outputContent)
output.close()
