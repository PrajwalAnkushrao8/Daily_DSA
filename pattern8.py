# Examples:

# Input Format: N = 3
# Result: 
# 1
# 01
# 101

# Input Format: N = 6
# Result:   
# 1
# 01
# 101
# 0101
# 10101
# 010101
n = int(input("enter value of n"))

for i in range(1,n+1):
    if i%2==0:
        start = 0
    else:
        start = 1
    for j in range(i):
        print(start,end="")

        start = 1 - start # to change the value of start after each print
    print()