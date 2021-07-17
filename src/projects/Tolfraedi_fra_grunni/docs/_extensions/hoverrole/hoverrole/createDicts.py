# -*- coding: UTF-8-sig -*-

# Author: Simon Bodvarsson
# 12.08.2016

# Create smaller and faster versions of BIN dictionary and Stae.is dictionary.
# Create a combined dictionary from BIN and Stae.is that allows for much faster
# look-up of mathematical terms in any form (E.g. look up of 'algebrunnar' is supported).

# Note: This module is not needed for running the extension or for look up in the dictionaries.
# 		It is only included here for documentation and to show how the dictionary files have 
#		been generated. 

import csv

# Creates a dict with forms from BIN db as 'keys' and a dict as 'values'.
# The dict stores citation forms for both icelandic and english.
# Uses minBIN and minstae as defined by the functions below.
# Dict is saved to 'binstae.py'
def combine():
	try: 
		import minBIN
	except ImportError:
		print("Dictionary module 'minBIN.py' not found. Creating it from 'SHsnid.csv'...")
		createminBIN()
		import minBIN
	try:
		from . import minstae
	except ImportError:
		print("Dictionary module 'minstae.py' not found. Creating it from 'ordasafn.py'...")
		createminstae()
		from . import minstae

	minBIN = minBIN.minBIN
	stae = minstae.minstae

	newDict = {}
	binSize = len(minBIN)
	oldkey = ''
	loopcount = 0
	lastcount = 0
	print(( 'Total number of keys: %d' %binSize))

	# Look up every 'key' from BIN library in stae.is library.
	for key in minBIN:
		# 'key' is any form of a word in BIN.
		# 'value' is a list of words in citation form that 'key' can be 
		# a form of.
		# If stae lookup of 'value' is successful, 'key' is a form
		# of a word defined in stae.is DB. In that case, it is added
		# to the new dictionary. Else it is discarded.

		# Keep track of progress and print it.
		loopcount +=1
		if loopcount >= lastcount+100000:
			perc = 100*loopcount/binSize
			print(('Working: %d of total %d, %d %%' %(loopcount,binSize, perc)))
			lastcount = loopcount

		# For each citation_form given in BIN, look it up in stae db
		for citword in minBIN[key]:
			# If the citation form is found in stae db, add it to the new dict.
			if citword in stae:
				newentry = {}
				staeentry = stae[citword]
				# Any form of the word to be added.
				newkey = key
				newentry['enTerm'] = staeentry['enTerm']
				newentry['isTerm'] = citword
				newDict[newkey] = newentry

	# Add all terms from stae.is DB that were not added before.
	# These entries are not defined in BIN and thus have identical 'isTerm' and 'key'.
	for key in stae:
		newkey = key
		newentry = {}
		newentry['enTerm'] = stae[key]
		newentry['isTerm'] = newkey
		newDict[newkey] = newentry

	# Save the result to file.
	saveDictFile(newDict,'binstae')
	print( "BIN and Stae dictionaries successfully combined.")
	print( "Output saved to file 'binstae.py'")

# Create smaller version of BIN dictionary with all word forms as keys and lists 
# of corresponding citation forms as values. Saved to file 'minBIN.py'.
# E.g. 'algebrunnar': {'isTerm':'algebra', 'enTerm':['algebra']}
def createminBIN():
	newDict = {}
	with open('SHsnid.csv') as csvfile:
		fields = ["citation_form","id_num", "class","bin_class","form","mark"]
		reader = csv.DictReader(csvfile, fieldnames = fields, delimiter = ';')
		for row in reader:
			form = row['form']
			cit_form = row['citation_form']
			# If 'form' is not in the dict, add it.
			if not form in newDict:
				newDict[form] = [cit_form]
			else:
				if cit_form in newDict[form]:
					# If both 'form' and 'cit_form' are in the dict,
					# no action is needed
					pass
				else:
					# If 'form' is in the dict but not 'cit_form',
					# add 'cit_form' to the list w. key 'form'
					newDict[form].append(cit_form)
	saveDictFile(newDict,'minBIN')
	print("Finished. Saved to file 'minBIN.py'")

# Create a smaller version of Stae.is dictionary with the Icelandic citation-form as 
# 'key' and the English citation-forms as 'values'. Saved to file 'minstae.py'.
# E.g. 'aflfræði' : {'enTerm': ['mechanics']}
def createminstae():
	import ordasafn
	newDict = {}
	totalEntries = len(ordasafn.os)
	currentEntry = 0
	lastprinted = 0

	for item in ordasafn.os:
		currentEntry +=1
		if currentEntry > (lastprinted + 100):
			print(('Progress: Entry %d out of %d total' %(currentEntry,totalEntries)))
			lastprinted = currentEntry
		try:
			isTermList = item['isTerm']
			enTermList = item['enTerm']
		except KeyError:
			continue

		if isTermList[0] == '' or enTermList[0] == '':
			# Current entry is missing 'isTerm' or 'enTerm' and is skipped
			continue

		for isTerm in isTermList:
			# For each 'isTerm' in the current entry, create an entry
			# in the new dict with 'isTerm' as key and a dict containing
			# the list of 'enTerm' as the values.
			newkey = isTerm

			# If the key is already in new dict, add the 'enTerms' to that list.
			if newkey in newDict:
				newentry = newDict[newkey]
				for enTerm in enTermList:
					# Do not repeat enTerms
					if enTerm in newentry['enTerm']:
						continue
					newentry['enTerm'].append(enTerm)

			# If they key is not already in the new dict, add it and the 'enTerm'.
			else:
				newDict[newkey] = {'enTerm':item['enTerm']}

	saveDictFile(newDict,'minstae')
	print("Finished. Saved to file 'minstae.py'")

# Create dictionary file 'ordasafn.py' from Stae.is datafile: fileName.
# (Original filename for stae.is file is 'output')
def createOrdasafn(fileName):
	# Read data from file.
	dictFile = open(fileName)
	ordasafn = dictFile.readlines()
	dictFile.close()

	# Extract values according to formatting of stae.is database.

	# Each entry contains seven values:
	# 1: Line number
	# 2: Number of translations
	# 3: English searchterm
	# 4: Context which term is used (e.g. "in Calculus" or "in set theory")
	# 5: Word class. Numbers 3,5 and 7 represent adjectives, nouns and verbs respectively.
	# 6: Icelandic translation of term.
	# 7: English synonyms
	# 8: Related terms, e.g. for a 'See also:...'.
	# Values are seperated by TAB-character and empty values are represented by \N.

	# Replace each line in ordasafn with the same content reformatted 
	# into a dict of lists of the form: 
	# { 'id':[], 'translationNum':[], 'enTerm':[], 'class':[],
	#   'isTerm':[], 'synonyms':[], 'relatedTerms':[] }
	for index,line in enumerate(ordasafn):
		ordasafn[index] = extractOSValues(line)

	targetfile = open('ordasafn.py','w+')
	print(r'# -*- coding: UTF-8-sig -*-', file=targetfile)
	print('os =', end=' ', file=targetfile)
	print(ordasafn, file=targetfile)
	targetfile.close()

# Helper function for createOrdasafn().
# Find and extract values from a given line into a dictionary according
# to the formatting of the stae.is database.
def extractOSValues(line):
	# Values are seperated by TAB character.
	data = line.split('	')
	# Ff the line holds fewer than 8 values, it is not included.
	if len(data) < 8:
		return{}
	# Put the data into a dict splitting multiple entries by ", "
	values= {
				'id':data[0].split(', '),
				'translNum':data[1].split(', '),
				'enTerm':data[2].split(', '),
				'context':data[3].split(', '),
				'class':data[4].split(', '),
				'isTerm':data[5].split(', '),
				'synonyms':data[6].split(', '),
				'relatedTerms':data[7].split(', '),
			}
	# Replace empty values with empty string.
	for key,value in values.items():
		if len(value) == 1 and value[0].find('\\')>-1:
			value[0] = ""

	return values

# Add a leading 'b' in front of all values of dictionary. Used for python 3 compatibilty.
def makeByteStrings(filename):
	targetfile = open(filename + '.py','r')
	dictionary = targetfile.readlines()
	print(dictionary)
	targetfile.close()
	for index,line in enumerate(dictionary):
		line = line.replace(" '"," b'")
		line = line.replace("{'", "{b'")
		dictionary[index] = line.replace("['", "[b'")

	dictionary.remove(dictionary[0])
	targetfile = open(filename + '.py','w+')
	print(r'# -*- coding: UTF-8-sig -*-', file=targetfile)
	print(dictionary[0], file=targetfile)
	targetfile.close()


# Save dict 'dictionary' to file 'filename.py'
def saveDictFile(dictionary,filename):
	targetfile = open(filename + '.py','w+')
	print(r'# -*- coding: UTF-8-sig -*-', file=targetfile)
	print((filename +' ='), end=' ', file=targetfile)
	print(dictionary, file=targetfile)
	targetfile.close()
