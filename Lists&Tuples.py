#Convert a tuple to a list; insert data, convert back to tuple.
myTuple = ('zero', 'one', 'two')
print(myTuple)
myList = list(myTuple)
myList.insert(3, 'three')
myTuple = tuple(myList)
print(myTuple)
input()
