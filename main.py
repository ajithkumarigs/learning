thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)

#extend values

name  = ["apple", "banana", "cherry"]
name2 = ["orange", "kivi", "curd"]
name.extend(name2)
print(name)

#insert functiom

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "orange")
print(thislist)

#remove list
#romove only specifc word

thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)

#The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

#If you do not specify the index, the pop() method removes the last item
#if you not menshon

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


#The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)

#The clear() method empties the list
#its clear all thinks in list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# continue one by one
#continue process
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#
