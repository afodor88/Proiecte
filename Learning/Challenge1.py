"""Title:  [easy] challenge #1 Text:  create a program that will ask the users name, age, and reddit username.
    have it tell them the information back, in the format:
    your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later. """

name = raw_input("Hi, Can I please know your name?")
age = raw_input("And your age?")
age = int(age)  # changing to integer so it can be printed as %i
reddituser = raw_input("And finally your reddit user?")

print "Hi, your name is %s, your age is %i and your username is %s" % (name, age, reddituser)
age = str(age)  # turning the age variable back to string so it can be concatenated with the new line when writing file

file = open("userinfo.txt", "w")  # creating and opening file called userinfo.txt and assigning it to file variable
file.write(name + "\n")  # writing in the file the containing of name variable
file.write(age + "\n")  # writing in the file the containing of age variable
file.write(reddituser + "\n")  # writing in the file the containing of reddituser variable
file.close()  # closing file

file = open("userinfo.txt", "r")  # opening previously written file since you first need to open file before read
print file.read()  # printing the containing of the previously written file
file.close()
