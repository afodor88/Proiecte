listanumere = [1, 1, 2, 3, 1, 2]
duplicate = {}

for number in listanumere:
    duplicate.setdefault(number, 0)
    duplicate[number] = duplicate[number] + 1
    
for number in duplicate:
    if duplicate[number] > 1:
        print 'The key ' + str(number) + ' is listed ' + str(duplicate[number]) + ' times.'
 
    