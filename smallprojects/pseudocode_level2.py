#!/usr/bin/env python2
##WRITTEN BY LUDOVIC DUTOIT, AUGUST 2018
#AIM: This scrpit aims at detecting windows that are suitable for amplification in a Fasta alignment
#It is full of conditions and the proposed primers should always checked visually in the alignbment using a simple alignment visualisation software


#READ THE ARGUMENTS
# input_file =   MULTIFASTA input file ) # add the parser
 #output_summary    =File with results ) # add the parser
 #output_alignment  =  File with new alignmment( just trimming the end where there is no info) ) # add the parser
 #n_inv_primer  =  number of sites that are required invariable at the 3' end of both primers ,type=int) # add the parser
 #n_deg_sites  =  number of sites that are allowed to be variable in the primer ,type=int) # add the parser
 #-length_window   = length of desired sequence to amplify (default: 300) ,type=int,default=300) # add the parser
 #-length_primer .=   length of primers (default: 20) ,type=int,default=20) # add the parser

   
###SOME FUNCTIONS 
#Put the fasta squencences into a dictionary
def getpos(pos,dic_multifasta):
	''' return a set with all the base found at position pos in the values of dic_multifasta'''
	return bases

def number_of_variable_site(start,end,dic_multifasta):
	''' return a list with the number of bases found for each position in the window defined from start to end (0 base included), ignores N or - '''
	return numb_variable_per_site

def count_variable_sites(start,end,dic_multifasta):
	''' return the number of variable sites in seq from start to end (0 base included), ignores N or -'''


def getseqprimer(start,end,dic_multifasta):

	return "".join(seq)
    return bases

#READ THE FASTA FILE
dict_fasta={}
# put >: seq inside

#CHECK INPUT
verify all sequences have same lengthlen_sequence = len(dict_fasta.values()[0])
print("The total length of the sequence is "+str(len_sequence)+" bp")



#for window by window from the length of the primer, go through the alignment shifting 1 base at the time

  # store primer sequences
  # store window sequences
  #calculate diversity
  # check for invariable sites at the end of primer
  # Look at the above and our input and see if the window is good or not


#Output the okay window to a file




