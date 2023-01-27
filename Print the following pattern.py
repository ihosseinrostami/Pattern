#print the following patern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

len = int(input("enter your range of number:"))

for num in range(len+1):
    for i in range(num):
        print(num , end =" ")
    print("\n")
