from pro1 import sorting,firstandlast
try:


    arr2 = []
    n = int(input("enter number of our list elements :"))
    for i in range(0, n):
        element = int(input("enter numer :"))
        arr2.append(element)
    print("your old list is :", arr2)
    sorting(arr2)
    print("you array sorted to :", arr2)
    n=len(arr2)
    x=int(input("enter your target sir :"))
    firstandlast(arr2, n, x)
    
except ValueError as err:
    print(err)
    print("please try again sir ")
