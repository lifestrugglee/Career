#!/usr/bin/env python
# -*- coding: utf-8 -*-
##########################################################################
#                                                                        #
# It's just a free tool for helping people to make a reference,          #
# BUT NOT FOR MAKING PROFIT!                                             #
#                                                                        #
# It's using the function of Google Scholar which generating the file in #
# EndNote formate, and then transfer it to the formate accepting in      #
# MS Word.                                                               #
#                                                                        #
##########################################################################
#                                                                        #
# 2020/05/14                                                             #
# Note: this code remain the issue of reading latin or spanish character #
# if title include '-' then will get an error >>> needs fix              #
#                                                                        #
##########################################################################

import os
import shutil

def initAddedFolder(dirName):
	if os.path.isdir(dirName) is False:
		os.mkdir(dirName)

def generateAuthorStr(xmlDict):
	authourStr = '''<NameList>'''
	for a in xmlDict['author']:
		als = a.split(',')
		if len(als) == 1:
			lName = als[0].strip()
			fName = ''
		elif len(als) == 2:
			lName = als[0].strip()
			fName = als[1].strip()
		onePerson = '''
					<Person>
						<Last>%s</Last>
						<First>%s</First>
					</Person>'''%(lName, fName)
		authourStr = authourStr + onePerson

	authourStr = authourStr + '''
				</NameList>'''
	return authourStr

addedDir = "added enw"
initAddedFolder(addedDir)

fileLs = os.listdir()
enwls = [f for f in fileLs if '.enw' in f]

newENWLs = []
enwTagls = []
enwTagDuplls = []
for enw in enwls:
	# print(enw)
	if str(enw).replace('.enw','') in enwTagDuplls:
		continue
	finalxml = ''
	xmlDict = {'sourcetype':'',
				'tag':'',
				'title':'',
				'year':'',
				'author':[],
				'volume':'',
				'issue':'',
				'pages':'',
				'journalname':''}
	# enw = enwls[1]
	with open(enw, 'r') as f:
		for line in f.readlines():
			# print(line)
			if '%0' in line:
				xmlDict['sourcetype'] = line.replace('%0', '').strip().replace(' ','')
			elif '%T' in line:
				xmlDict['title'] = line.replace('%T', '').strip()
			elif '%A' in line:
				xmlDict['author'].append(line.replace('%A', '').strip())
			elif '%J' in line:
				xmlDict['journalname'] = line.replace('%J', '').strip()
			elif '%V' in line:
				xmlDict['volume'] = line.replace('%V', '').strip()
			elif '%N' in line:
				xmlDict['issue'] = line.replace('%N', '').strip()
			elif '%P' in line:
				xmlDict['pages'] = line.replace('%P', '').strip()
			elif '%D' in line:
				xmlDict['year'] = line.replace('%D', '').strip()

	xmlDict['tag'] = xmlDict['author'][0].split(',')[0] + xmlDict['year'] + xmlDict['title'].split(' ')[0]
	print(xmlDict['tag'])

	finalxml = '''	<Source>
		<SourceType>%s</SourceType>
		<Tag>%s</Tag>
		<Title>%s</Title>
		<Year>%s</Year>
		<URL></URL>
		<Author>
			<Author>
				<NameList></NameList>
			</Author>
		</Author>
		<Volume>%s</Volume>
		<Issue>%s</Issue>
		<Pages>%s</Pages>
		<JournalName>%s</JournalName>
	</Source>'''%(xmlDict['sourcetype'], xmlDict['tag'], xmlDict['title'], xmlDict['year'],
		 xmlDict['volume'], xmlDict['issue'], xmlDict['pages'], xmlDict['journalname'])
	# print(finalxml)
	if xmlDict['tag'] not in enwTagls:
		print(enw)
		authorxmlStr = generateAuthorStr(xmlDict)
		finalxml = finalxml.replace('<NameList></NameList>', authorxmlStr)
		newENWLs.append(finalxml)
		enwTagls.append(xmlDict['tag'])
		newFileName = xmlDict['tag'] + '.enw'

		if os.path.isfile(newFileName) and newFileName != enw:
			os.remove(enw)
			print('It is duplicated - %s >>> file deleted'%xmlDict['tag'])
			enwTagDuplls.append(xmlDict['tag'])
		else:
			os.rename(enw, newFileName)
		addedFilePath = os.path.join(addedDir, newFileName)

		if os.path.isfile(addedFilePath):
			os.remove(newFileName)
		else:
			shutil.move(newFileName, addedFilePath)
	else:
		os.remove(enw)
		print('It is duplicated - %s >>> file deleted'%xmlDict['tag'])
		enwTagDuplls.append(xmlDict['tag'])

	if xmlDict['sourcetype'] != 'JournalArticle':
		print('It is NOT a JournalArticle - %s, Tag - %s'%(enw, xmlDict['tag']))




headStr='''<?xml version="1.0"?>
<Sources xmlns="http://schemas.openxmlformats.org/officeDocument/2006/bibliography">
'''
endStr = '''
</Sources>'''
finalxml = ''
for unit in newENWLs:
	finalxml += '\r' + unit
finalxml = headStr + finalxml + endStr
with open('generateReference.xml', 'w')as f:
	f.write(finalxml)

# Final Report
print('DONE - total: %d papers, add: %d papers to xml file, duplicated #: %d'%( len(enwls), len(enwTagls), len(enwTagDuplls) ))
