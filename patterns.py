#Example 2:
#Input: N = 6
#Output:
#* * * * * *
#* * * * * *
#* * * * * *
#* * * * * *
#* * * * * *
#* * * * * *


rows = int(input("enter rows number"))

def getPattern(rows):
    for i in range(rows):
        for j in range(rows):
            print("*", end = " ")
        print()


getPattern(rows)
