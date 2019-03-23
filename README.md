# LabTwinChallenge


Explanations and instructions

The answers to the questions are in Labtwin answers.pdf. <br>
All the code is in labtwin_data_normalization.py. <br>
<br>
The output from when I ran it on my computer is in papers/papers_aggregated_result.txt.

Running instructions: 


-	It uses the following libraries which need to be installed to run it:
*	 codecs
*	 unicodedata 
*	BeautifulSoup
*	 functools
*	 os
*	 re 
*	 inflect 
*	 string 


-	At the top, there are two variables that represent the output file and the folder it is in. Their values might need to be changed by the user before running the program.

*	result_name = "papers_aggregated.txt"
		
*		 # 'result_name' is the name of the file which will contain the aggregate of the files 
*		 # intially it should be an empty file
	 
*	path = "C:/Users/Valdi/Documents/papers/"
*		 # 'path' is the folder which contains the papers and an initially empty text file whose name is the value of 'result_name'


- Then it can be run from the command line with "python labtwin_data_normalization.py".
- After running the output should be in path/result_name.
	
	
Explanations of the script : 

	- The script has 7 functions that do some string operations (with docstrings for detailed explanation) .
	
	- It contains one loop that goes through the directory in 'path' and parses each html file in the directory in alphabetical order. 
	
	- It first reads in each html file with codecs, 
	*	then uses BeautifulSoup to extract the paragraphs from it,
	*	changes the numbers to spoken form using the help functions and inflect, 
	*	changes it back into one string using the reduce operation from functools and a help function,
	*	converts the result into printed ascii using unicodedata,
	*	throws away URLs using a regular expression,
	*	removes punctuation 
	*	and finally writes the result to the file, along with a seperator in between papers:
	-		"\n" + "*** Original paper file name: " + file_name  + " ***\n\n"
	
	*More details are in the comments in the script. 
			
	
