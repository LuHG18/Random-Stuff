#Open and read a file
fo = open("foo.txt","r+")
str = fo.read();
print "Read string is: ", str
#Close file
fo.close()
