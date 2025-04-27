n = int(input("number of n"))



for i in range(1,n+1):
    for space in range(n-i):
      print(" ",end="")
    for star in range((i*2)-1):
      print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(i-1):
      print(" ", end="")
    for star in range(2*n-(2*i-1)):
      print("*",end="")
    print()




#[4,1,4]
#[3,3,3]
#[2,5,2]
#[1,7,1]
#[0,9,0

