#!/usr/bin/env python

#COMMAND LINE SCRIPT 
# example usage: python summary_fasta.py <inputfile> <outputfile>"
#fasta_file.txt is a provided fasta_file you can use as input

#DESCRIPTION
#Command line scripts are great because they allow someone who
# does know how to code to use your scripts. They are not run directly from python
# but from a terminal.
#This script take a fasta file (use fasta_file.txt) to obtain a few statistics.
#A fasta file is a standard format to store biological sequences(i.e. dna, proteins). 
#It has one line of description per sequence starting by
# he character ">". All the next lines are sequence until the next sequence descriptor

#INSTRUCTIONS

#1.Run it according to example usage (line 4)
#2.take time to understand how it works, function by function. The functions are ran at the end of the program
#pay particular attention to the two functions that habdke files (i.e. parse_fasta output_summary).
#Add some print statement to understand the code or modif the script.

# for more on file handling https://www.tutorialspoint.com/python/python_files_io.htm
# For more advanced argument parsing  https://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/ 

# This program adds up integers in the command line
import sys


def read_in_argument(arguments):
	'''check the input'''
	if not len(sys.argv) == 3: #check that the user entered two argument ( the name of the script is the third)
		raise Exception ("usage: python test.py <inputfile> <outputfile>")
	return arguments[1:] # the argument 0 is the script name, return input file and output file


def parse_fasta(input_fasta):
	'''return a dictionnary of sequences'''
	dict_sequences = {} # a dictionnary to store sequence
	with open(input_fasta) as f: #open the file
		for line in f: # start a loop going line by line
			if line.startswith(">"): #startswith is a method of string
				header=line[1:].strip("\n") # the header line without the ">" and the newline character
				dict_sequences[header] = ''  #start an empty sequence as a dict value for that header
			else:
				dict_sequences[header] += line.strip("\n") # add sequence without end of character signs
	return dict_sequences


def output_summary(dict_sequences,outputfile):
	''' write a short summary of the sequences in 
	dict_sequences to outputfile '''
	output_handle = open(outputfile,"w") #open the output_file in "w" (writing) mode
	header = "seq\tgc\tundefined_bases\tlength\n" # tab separated and then new line
	output_handle.write(header) #writing the header, write is a methof of object of type: file
	for key in dict_sequences.keys(): # all the headers
		myseq = dict_sequences[key]
		gc_content =  gc(myseq)
		number_of_n = missingdata(myseq)
		len_seq = str(len(myseq))
		###write the output now
		output_line = "\t".join([key,gc_content,number_of_n,len_seq])+"\n"
		output_handle.write(output_line) #write the line for that sequence
	output_handle.close() # flush the memory, important when you are donewriting a file! this function has no return

def gc(sequence):
	''' Calculate the gc content
	of a dna sequence, a basic parameter that
	has importance in diverse fields'''
	lower = sequence.lower() # transform all letters in lower case, easier for pattern matching
	gc = lower.count("g")+lower.count("c") #count the g+ the c
	at = lower.count("a")+lower.count("t") # count the a + the t to not take account undefined bases
	gc_content = float(gc)/(at+gc) # here we calculate gc content
	rounded_gc_content = round(gc_content,3) # we make the whole number shorter.
	return str(rounded_gc_content) # we return it as a string


def missingdata(sequence):
	''' Return the number of undefined bases in a sequence
	Any base that is not N'''
	number_of_undefined = 0 # a counter for the number of bases
	for base in sequence:
		if base not in "atgcATGC": # check if base is a substring of "atgcATGC"
			number_of_undefined += 1
	return str(number_of_undefined)



#MAIN PROGRAM

input_file,output_file = read_in_argument(arguments = sys.argv)
my_sequences = parse_fasta(input_fasta =input_file)
output_summary(dict_sequences= my_sequences,outputfile=output_file)



