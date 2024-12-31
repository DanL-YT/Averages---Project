from doctest import debug
import math as m
import numbers
def numberInput():
    global numList
    numList = []
    valid = True
    while valid == True:
        num = input("Enter a number ('done' to end)")
        if num.lower() == "done":
            valid = False
            break
        numList.append(int(num))
def mean():
    if numList == []:
        print("Empty")
    result = sum(numList) / len(numList)
    print(f"Mean: {result}")

def median():
    global numList
    numList2 = []
    if numList == numList or []:
        print("Empty")
    for i in range(len(numList)):
        num = numList[i]
        numList2.append(int(num))
    numList = numList2
    numList = list(numList)
    numList.sort()
    n = len(numList)
    if n % 2 == 0:
        result1 = numList[n // 2]
        result2 = numList[n // 2 - 1]
        result = (result1 + result2) / 2
    else:
        result = numList[n // 2]
    print(f"Median: {result}")
def mode():
    if numList == []:
        print("Empty")
    numList.sort()
    i = 0
    L1 = []
    while i < len(numList):
        L1.append(numList.count(numList[i]))
        i+=1
    d1 = dict(zip(numList, L1))
    d2 = {k for (k, v) in d1.items() if v == max(L1) }
    print(f"Mode: {str(d2)}")
def fileHandling():
    global numList
    print("File Handling Menu:")
    print(
        "1. Save to file",
        "2. Load file",
    )
    option = input("Chose and option: ")
    if option == "1":
        filename = input("Enter filename to save to: ")
        file = open(filename, "a")
        for num in numList:
            file.write(f"{num}\n")
        print(f"Numbers saved to {filename}")
        file.close()
    elif option == "2":
        numList2 = []
        numList = []
        filename = input("Enter filename to load: ")
        file = open(filename, "r")
        numList = [line.strip() for line in file]
        print(f"Numbers loaded from {filename}")
        for i in range(len(numList)):
            num = numList[i]
            numList2.append(int(num))
        numList.clear()
        numList = numList2
        print(numList)
    else:
        print("Invalid")
funtional = True
while funtional == True:
    print("Menu: ")
    print("1. Enter numbers",
        "2. Mean",
        "3. Mode",
        "4. Median",
        "5. File Handling",
        "6. Exit"
    )
    choice = input("Choose an option: ")
    if choice == "1":
        numberInput()
    elif choice == "2":
        mean()
    elif choice == "3":
        mode()
    elif choice == "4":
        median()
    elif choice == "5":
        fileHandling()
    elif choice == "6" or "%":
        print("Exiting program.")
        funtional = False
