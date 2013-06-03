from sys import argv

script, user_name = argv
prompt = '> '

print "hi, %s, I'm the %s script" % (user_name, script)
print "Give me a 1 word answer."
print "Name a color" 
color = raw_input(prompt)

print "List an place  %s?" %user_name
place = raw_input(prompt)

print "What's your favorite exercise?"
verb = raw_input(prompt)

print """
Alright, so you are feeling %r . 
You wish you were  %r instead of at work.  
Once you're there you are going to  %r right away. 
""" % (color, place, verb) 
