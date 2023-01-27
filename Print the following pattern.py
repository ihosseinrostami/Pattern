#print the following patern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

#get the range of number from user and save it in "len"
len = int(input("enter your range of number:"))

#create a loop to cout
for num in range(len+1):
    for i in range(num):
        print(num , end =" ")
    print("\n")
