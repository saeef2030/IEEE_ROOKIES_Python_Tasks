def evennum():
 listSize = int(input("Enter the list size: "))
 numbers = []
 evenCount = 0

 for i in range(listSize):
    number = int(input("Enter a number: "))
    numbers.append(number)
 for number in numbers:
    if number % 2 == 0:
        evenCount = evenCount + 1
 print("You have",evenCount, "even number")


try:
    evennum()
except ValueError as err:
    print(err)
    print("please try again sir ")
