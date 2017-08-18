from sys import argv
script,filename=argv
print "We are going to erase %r" % filename
print "Hit ctrl-c to cancel" 
print "Hit enter to proceed"

raw_input("?")

print "Opening the file..."
target=open(filename,'w')

print "Truncating the file"
target.truncate()

print "Now i m going to ask you for 3 lines"
line1=raw_input("L1:")
line2=raw_input("L2:")
line3=raw_input("L3:")

print "I am going to write these to the files"

target.write(line1)
target.write(line2)
target.write(line3)
