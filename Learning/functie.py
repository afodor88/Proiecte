"""Title:  [easy] challenge #1 Text:  create a program that will ask the users name, age, and reddit username.
    have it tell them the information back, in the format:
    your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.  """


def writingfile(name, age, reddituser):
    """

    :param name:
    :param age:
    :param reddituser:
    """

    file = open("userinfo.txt", "w")
    file.write(name + "\n")
    file.write(age + "\n")
    file.write(reddituser + "\n")

    file.close()
    return name, age, reddituser

name = raw_input("Hi, Can I please know your name?")
age = raw_input("And your age?")
reddituser = raw_input("And finally your reddit user?")

writingfile(name, age, reddituser)
file = open("userinfo.txt", "r")
print file.read()
file.close()
