# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from array import *
arr =array('i',[])
n=int(input("Enter Length of a string"))
for i in range(n):
        x=int(input("Enter The next value"))
        arr.append(x)
print(arr)

val=int(input("Enter value for Search"))
print(arr.index(val))