#!/usr/bin/env python

#########################################
# CALENDAR GENERATOR
# A script to print a custom calendar
# using user input for month and day and
# the built-in python calendar utility.
# Demonstrates input validation.
# By Rebecca Kuensting
# March, 7, 2017
#########################################

import calendar
import types

#***********************************
# Header-printing function to keep
# things ridiculously good-looking
#***********************************
def headerPrint():
	print "\n"
	print "-+------------------------------------+-"
	print " |         Calendar Generator         |"
	print "-+------------------------------------+-"
	print " | Input your desired YEAR and MONTH, |"
	print " | and the program will display the   |"
	print " | corresponding calendar.            |"
	print "-+------------------------------------+-"

#***********************************
# Input validation function:
# Loops for more input if user-
# supplied values are invalid.
#***********************************
def validate_ints(number):
	while True:
		number = input()
		try:
 			number = int(number)
		except ValueError:
			print "Invalid Input. Please try again:\n"
			continue

		if (0 < number):
			return number
		else:
			print "Invalid Input. Please try again:\n"
			continue

#***********************************
# MAIN PROGRAM BODY:
#***********************************

keepGoing = True

while (keepGoing == True):

	#-----------------------------
	#PRINT THE HEADER:
	#-----------------------------
	headerPrint()


	#-----------------------------
	#GET YEAR AND MONTH FROM USER:
	#-----------------------------
	year = 0
	print ("  Input the year, then press ENTER \n  (e.g. 1776):")
	year = validate_ints(year)

	month = 0
	print ("  Input the month, then press ENTER \n  (e.g. 7):")
	month = validate_ints(month)

	#-----------------------------
	#DEFINE THE CALENDAR:
	#-----------------------------
	cal = calendar.month(year, month)

	#-----------------------------
	#PRINT THE OUTPUT
	#-----------------------------
	print cal

	#-----------------------------
	# ASK USER WHETHER TO CONTINUE
	#-----------------------------
	print "Would you like to make a new calendar?"
	print "1. \tYes"
	print "2. \tNo\n"
	print "Input your selection, then press ENTER:\n"
	keepGoing = validate_ints(keepGoing);

print "Thanks for using Calendar Generator!"
print "\n"