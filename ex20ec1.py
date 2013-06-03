# import argv paramters from sys
from sys import argv
# assign variables to argv
script, input_file = argv
# creates function print_all with argument f
def print_all(f):
# prints argument f and reads it.
	print f.read()
# rewind method used to go back to argument f	
def rewind(f):
# uses seek method to 0 out where you're at in the file.
	f.seek(0)
# creates function print_a_line.	
def print_a_line(line_count, f):
#prints the number of line you're on and uses the readline method to read just one line.
	print line_count, f.readline()
# assigns open method to open argument which is file uses in command.	
current_file = open(input_file)
#prints string and goes to the next line.
print "First, lets print the whole file: \n"
# runs function print_all which is the file you use in the script.
print_all(current_file)
# prints string
print "Now lets rewind, kind of like a tape."
# uses rewind method to implement current_file function by using current_file as argument.
rewind(current_file)
# prints string
print "Let's print three lines:"
# assigns value to variable current_line
current_line = 1
# uses print_a_line function which as arguments current_line (the number 1) then a comma 
# to ove to next argument which is function current_file which says to open argument 
# input_file which is the file you use when opening script.
print_a_line(current_line, current_file)
# adds 1 to varaiable current_lines and assigns value to variable current_line 
current_line = current_line + 1
# uses print_a_line function which as arguments current_line (the number 1) then a comma 
# to ove to next argument which is function current_file which says to open argument 
# input_file which is the file you use when opening script.
print_a_line(current_line, current_file)
# adds 1 to varaiable current_lines and assigns value to variable current_line 
current_line = current_line + 1
# uses print_a_line function which as arguments current_line (the number 1) then a comma 
# to ove to next argument which is function current_file which says to open argument 
# input_file which is the file you use when opening script.
print_a_line(current_line, current_file)