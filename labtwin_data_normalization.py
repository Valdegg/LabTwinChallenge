# Data Normalization for the Methods and Materials part of 363 papers dealing with genetics, from the US National Library of Medicine National Institutes of Health.
 
 
 
import codecs
import unicodedata 
from bs4 import BeautifulSoup
import functools
import os
import re 
import inflect 
import string 



result_name = "papers_aggregated.txt"
# 'result_name' is the name of the file which will contain the aggregate of the files
# intially it should be an empty file
 
path = "C:/Users/Valdi/Documents/papers/"
# 'path' is the folder which contains the papers and an initially empty text file whose name is the value of 'result_name'

result = open(path + result_name, "a")
# result is an object for the result file to be written into

inflector = inflect.engine()
# inflector is an object for changing numbers into spoken form, used by numberToSpoken()



def newLineCat(string1, string2): 
	"""Use: string3 = newLineCat(string1,string2)
	Before: string1, string2 are strings that represent paragraphs
	After: string3 is the paragraphs with an empty  line in between them """	
	return string1 + "\n \n" + string2 

 

def  removePunctuation(strengur): 
	"""Use: without = removePunctuation(strengur)
	Before: 'strengur' is a string 
	After: 'without' is a 'strengur' without punctuation """
	# note:  words consisting only of punctuation marks give an extra space
	return ''.join(word.strip(string.punctuation) for word in strengur)
	

def hasNumbers(inputString):
	""" Use: b = hasnumbers(inputString)
	Before: 'inputString' is a string 
	After: b is True iff 'inputString' contains a digit"""
	return any(char.isdigit() for char in inputString)


def isFloat(inputString):
	""" Use: b = hasnumbers(inputString)
	Before: 'inputString' is a word string (no whitespaces)
	After: b is True iff 'inputString' is a rational number 
	i.e. is a string of only numbers and one dot in the middle, like 0.1  and isn't an integer like 12"""
		
	
	return inputString.replace('.','',1).isdigit() and not inputString.isdigit()
	
def isACT1231(inputString):
	""" Use: b = hasnumbers(inputString)
	Before: 'inputString' is a word string (no whitespaces)
	After: b is True iff 'inputString' is a letter sequence that ends with a number sequence
	e.g. K562"""
		# split into two 	
		# not enough time for this feature at the moment 
	
	return	bool(re.match('^([a-zA-Z]+[0-9]+)$', inputString))
	
def is1231ACT():
	""" same as isACT1231 but with number that ends with character sequence """ 
	return 0

def numberToSpoken(strengur): 
	""" Use: spoken = numberToSpoken(number)
	Before: 'strengur' is a string that may contain numbers e.g. "it costs 1000 dollars and is worth 1.5 hours"
	After: 'spoken' is 'strengur' with numbers in spoken form, e.g. "it costs one thousand dollars and is worth one point five hours" """
	words = strengur.split()

	words2 = [inflector.number_to_words(word) if isFloat(word) or word.isdigit() else  word  for word in words]
	#words3 = [inflector.number_to_words(word, group = 1) if isACT1231(word) else  word  for word in words2]
		# later time feature 
	if words2 != []:
		words3 = functools.reduce( lambda x,y: x + " " + y, words2 ) 
	else: 
		words3 = ""
	return words3



	



i = 0
for file_name in sorted(os.listdir(path)):
	# Loop invariant: 
	# The first i html files in 'path' have been written to 'result' in alphabetical order.
	# The text is lower-case plain ASCII without punctuation and with words in spoken form.
	# Paragraphs from the html files are separated by new-lines. 
	# html files are separated by lines with *** Original paper file name: FILENAME ***
	
	if(file_name[-4:] == "html"):
		
		html = codecs.open(path + file_name, 'r').read()  
		# 'html' is the html file in 'file_name'
		
		soup = BeautifulSoup(html, 'html.parser')
		# 'soup' is a BeautifulSoup object for parsing the html 
		
		paragraphs = [p.get_text() for p in soup.findAll('p')]	
		# all the paragraphs from paper with name 'file_name' are in 'paragraphs'
		
		words_no_numbers = [numberToSpoken(paragraph) for paragraph in paragraphs]
		# words_no_numbers is the paragraphs with number words like 1.5 and 333 changed to spoken form. 
		
		text = functools.reduce( lambda x,y: newLineCat(x,y), words_no_numbers ) 
		# 'text' is a single string with all paragraphs with an empty line in between 
		

		text2 = unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode().lower()
		# 'text2' is text transformed such that it's a string in ASCII (not bytes), in lower case.		

		text3  = re.sub(r'http\S+', '', text2)
		# text3 doesn't contain links 
		

		text4 = removePunctuation(text3)		
		
		# 'text4' is a string with the contents of the paper from 'file_name', in ASCII, in lower case and without punctuation and with numbers in spoken form 
		
		result.write("\n" + "*** Original paper file name: " + file_name  + " ***\n\n") 
		result.write(text4 +"\n") 
		# the contents of 'text4' have been written to the result file 
		
		i = i +1 
				
		
		
 
 

result.close()

# some tests I used :
tests = False
if(tests):
	# print(bool(re.match('^([a-zA-Z]+[0-9]+)$', 'hasAlphanum123')))
	# s = "ara12311"
	# print(isFloat("12.5"))
	# print(isFloat("5"))
	# print("15".isdigit())		
	# print(removePunctuation("# After: 'spoken' is 'number' in... spoken form, e.g. 'twelve'"))
	# print(inflector.number_to_words("12.5"))
	# print(inflector.number_to_words("125"))
	 print(numberToSpoken("ACS300 costs 1000 dollars and is worth 1.5 hours of time"))
