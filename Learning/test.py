"""cat = {'name': 'Zophie', 'age': '7', 'color': 'grey'}
allCats = []
allCats.append({'name': 'Pooka', 'age': '5', 'color': 'black'})
allCats.append({'name': 'Fat-tail', 'age': '3', 'color': 'gray'})
allCats.append({'name': '???', 'age': '-1', 'color': 'orange'})

print allCats"""
import pprint


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }
pprint.pprint(theBoard)

def printBoard(board):
    print (board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
    print ('-----')
    print (board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] )
    print ('-----')
    print (board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] )

printBoard(theBoard)