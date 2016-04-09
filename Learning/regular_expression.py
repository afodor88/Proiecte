import re

text = '424-423-4444 trararar adsadas da asdsad 444-555-5324'

expresie = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
obiectexpresie = expresie.search(text)
print obiectexpresie.group() # Print the first match; Note we need to use the group command to print the regular expression object

print expresie.findall(text) # Print all the matches; Note we don't use the group command since we return a list'