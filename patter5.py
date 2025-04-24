#Input Format: N = 3
#Result: 
#* * *
#* * 
#*
#
#Input Format: N = 6
#Result:
#* * * * * *
#* * * * * 
#* * * * 
#* * * 
#* * 
#*


n = int(input("enter the value for n")) 


for i in range (1, n+1):
    for j in range(1,n-i+1):
        print("*", end="")
    print()

