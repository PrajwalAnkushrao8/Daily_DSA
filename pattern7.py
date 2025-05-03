# Examples:

# Input Format: N = 3
# Result: 
#   *  
#   **
#   ***  
#   **
#   *   
# Input Format: N = 6
# Result:   
#      *
#      **
#      *** 
#      ****
#      *****
#      ******  
#      *****
#      ****
#      ***    
#      **
#      *
n = int(input("enter n"))
for i in range(1,2*n):
    if i<=n:
        for j in range(i):
            print("*",end="")
        print()
    else:
        for j in range((2*n)-i):
            print("*",end="")
        print()
