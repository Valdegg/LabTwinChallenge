# Data Normalization for the Methods and Materials part of 363 papers dealing with genetics, from the US National Library of Medicine National Institutes of Health.
 
 
 
import codecs
import unicodedata 
from bs4 import BeautifulSoup
import functools
import os
import re 
import inflect 
import string 


inflector = inflect.engine()



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
	



def numberToSpoken(strengur ): 
	""" Use: spoken = numberToSpoken(number)
	Before: 'strengur' is a string that contains numbers e.g. "it costs 1000 dollars"
	After: 'spoken' is 'strengur' with numbers in spoken form, e.g. "it costs one thousand dollars" """
	return inflector.number_to_words(strengur)
	#return ''.join(inflector.number_to_words(word) for word in strengur if  

print(removePunctuation("# After: 'spoken' is 'number' in... spoken form, e.g. 'twelve'"))
print(numberToSpoken("asldka"))


s = "hg19 reference genome using novoalign software version 20714  picard software version 167  and the genome analysis toolkit gatk  27 variant discovery genotype calling and annota"
s2 = "hg19 reference genome using novoalign software version 20714.32  picard software version 167  and the genome analysis toolkit gatk  27 variant discovery genotype calling and annota"
l = []
for t in s.split():
    try:
        l.append(float(t))
    except ValueError:
        pass
print(l)
# þetta nær 20714 og 27 en bætir við .0
# þarf að gera greinarmun á ints og floats 
	# ef það er punktur í orðinu (ekki í endann) og orðið samanstendur annars af tölum þá float 
# þarf fyrst að finna orðin, allt sem hefur bil í kringum sig  \b\w\b eitthvað
	# nei bara Ekki bil 
	
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
	

result_name = "papers_aggregated.txt"
# 'result_name' is the name of file containing the aggregate of the files

 
path = "C:/Users/Valdi/Documents/papers/"
# 'path' is the folder which contains the papers and an initially empty text file whose name is the value of 'result_name'

result = open(path + result_name, "a")
# result is an object for the result file to be written into



i = 0
for file_name in sorted(os.listdir(path)):
	# Loop invariant: 
	# The first i html files in 'path' have been written to 'result' in alphabetical order.
	# The text is lower-case plain ASCII without punctuation and with words in spoken form.
	# Paragraphs from the html files are separated by new-lines. 
	# html files are separated by lines with *** Original paper file name: FILENAME ***
	
	if(file_name[-4:] == "html" and i < 0):
		
		html = codecs.open(path + file_name, 'r').read()  
		# 'html' is the html file in 'file_name'
		
		soup = BeautifulSoup(html, 'html.parser')
		# 'soup' is a BeautifulSoup object for parsing the html 
		
		paragraphs = [p.get_text() for p in soup.findAll('p')]	
		# all the paragraphs from paper with name 'file_name' are in 'paragraphs'

		text = functools.reduce( lambda x,y: newLineCat(x,y), paragraphs ) 
		# 'text' is a single string with all paragraphs with an empty line in between 
		
		text2 = unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode().lower()
		# 'text2' is text transformed such that it's a string in ASCII, in lower case.		

		text3  = re.sub(r'http\S+', '', text2)
		# text3 doesn't contain links 
		
		#text3 = numberToSpoken(
	# ath þarf að vera gert áður en punctuation er tekið svo 1.5 verði one point five 
		
		text4 = removePunctuation(text3)		
		
		# 'text5' is a string with the contents of the paper from 'file_name', in ASCII, in lower case and without punctuation and with numbers in spoken form 
		
		result.write("\n" + "*** Original paper file name: " + file_name  + " ***\n\n") 
		result.write(text5 +"\n") 
		# the contents of 'text5' have been written to the result file 
		
		i = i +1 
				
		
		
 
 

result.close()
 
# testa minimum requirements
 
# vista aggregate í skjal

		#bla = re.sub(r'(\b\w+\b)', "5", s)
			# lambda x: removePunctuation(x.group())		
		#text3 = re.sub(r'[^\s]+', lambda word: ''.join(e for e in word if e.isalnum()), text2)
		# every sequence of not-whitespaces (i.e. words) which contain only alphanumerics (non-punctuation)

