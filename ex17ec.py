from sys import argv
#from os.path import exists

script, a, b = argv; indata = open(a).read(); output = open(b,'w');output.write(indata)

print "Copying from %s to %s" % (a, b)

# we could do these two on one line too, how?
#input = open(from_file)
#indata = input.read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)


#output = open(to_file, 'w')
#output.write(indata)

print "Alright, all done."
#output.close()
#input.close()
