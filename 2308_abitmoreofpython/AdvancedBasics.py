#!/usr/bin/env python

#this script is demonstrating  a few commands
#and tools for python.


#MORE are ideas of small exercices. 



###1 LINE: OUTPUT


print 'Hello, world!' # Number 1!


###STRING INDEXING

a = 'Hello, world'
a[1]  # Python is zero based, grab the first position
a[0:5] # from the beginning to 5 ( excluding five, lengh = 4)
a[:5] # beginning does not need to be specified
a[2:] # end does not need to be specified either
a[-1] # print the last character
a[-3:] # print the the three last characters
a[1:10:2] # from 1 to 10 jumping 1 position every time
a.upper() # print A in upper case, upper is a method (a function for object a)

#MORE can you print the reverse string 'dlrow ,olleH'?
#MORE try a few function for objects of class strings", find them out using (dir)


####LINES: FOR LOOP, BUILT-IN ENUMERATE FUNCTION, NEW STYLE FORMATTING


friends = ['rachel', 'monica', 'joey','chandler','ross']  # this is a list it can be enumerated over
for  name in friends:
    print  name


friends = ['rachel', 'monica', 'joey','chandler','ross'] # this is a list it can be enumerated over
for i, name in enumerate(friends):  # get rid of counters!
    print  i, name


#MORE: What is enumerate() about?
#MORE :What is the type of enumerate, of friends?

#CONDITIONAL


####LINES: FUNCTIONS


def greet(name):  # we define this function
    print 'Hello', name 

greet('Jack') # run the function for jack
greet('Lea') # run the function for lisa


def greet(name,weather="good"):  # we add an optional argument
    print 'Hello', name,"the weather is",weather,"today"
    return name

greet('Andy') #use the default weather value
greet('Anna',weather="bad") # use the specified one
greet('Bob',weather =2) # as you see, you can specify different type of integers



#MORE modify greet() so that you make sure that weather
#is a string or then it stop the program use google to
# find out how to stop the program!
#MORE what is return about?


###LINES: FIBONACCI, MULMOREE ASSIGNMENTS

parents, babies = 1, 1 # python allows you to assign  two variables at the same time.
while babies < 100: # as long as babies is less than 100, go through this
    print 'This generation has ' + str(babies) + " babies"  # create a long string, note that ''  = ""
    parents, babies = babies, parents + babies # recomputing number of parents and babies


#MORE: Can have add grand parents and do a triple assignment?
#MORE: Can you transform this into a function that take 
#the maximum number of babies as an argument


###LINES: TIME, CONDITIONALS, FROM..IMPORT, FOR..ELSE


import time # collection of tools to manage the time format

activities = {8: 'Sleeping', 
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

time_now = time.localtime() # the localtime that is inside module time
hour = time_now.tm_hour # extract the hour from the current time

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print "next: At",activity_time," you will be",activities[activity_time]
        break 
else:
    print 'Unknown, AFK or sleeping!'

#MORE What if you add an activity at 16 on the line abobe commuting?
#MORE can you print " the last thing you did was"
#MORE look what helse is in time using help(time)



###CONDITIONAL
# python will get into the block if all the statement is true
if True: # True is true
  print "this is true"

if not False: # not false is true 
  print "this is true"


if True or False:  # at least one side of the "or" has to be true
  print "this is true"

if True and True:  # if both sides of "and" are true
   print "this is true"

1<=3  or 1>= 3# this is true
1<=1 # this is true
1<1 #false

#other handy booleans

"line".startswith("l") # true
"a" in "jnwkejfn" # false, check if a the first is a subset of the second

all([True,False,True,True]) # check that all are true
any([True,False,True,True]) # check that at least one is true


#MORE what about not all() and not any()
#MORE play with more complicated expression and with expressions that contains more than two statements


###LINES: TRIPLE-QUOTED STRINGS, WHILE LOOP


#triple quoted string are type 'string' but they can be spicified over multiple lines!
#%i specify that the user will specify an integer after the string after the modulo sign 
# It could also be %s for specifying string.
# It is very practical to format
REFRAIN = ''' 
%i bottles of beer on the wall,
%i bottles of beer,
take one down, pass it around,
%i bottles of beer on the wall!
'''    
bottles_of_beer = 99
while bottles_of_beer > 1:
    print REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1) # the part after the modulo assign values to the rhee %d
    bottles_of_beer -= 1 # this is a short for bottles_of_beer  = bottles_of_beer -1
