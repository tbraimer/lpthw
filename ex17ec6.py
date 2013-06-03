from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file); indata = in_file.read()
out_file = open(to_file, 'w'); out_file.write(indata)

# I erased the output.close lines and the code still works.  I imagine the files are 
#still open.