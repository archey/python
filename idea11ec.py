#!/usr/bin/python
print "Do you love python?",
py = raw_input( )
print "How many days are in a week?",
wk = raw_input( )

if py.lower() == "no":
   print "You are an idiot, python is the greatest"
else:
   print "So you love python, %s\n and there are %s days in a week." % (py, wk)




