'''
#Summer exam prep
num1 = int(input("Enter a number "))
num2 = int(input("Enter a second number "))



choice = input()
if choice == 'a' or choice == 'A':
    print (num1 + num2)
    
elif choice == 's' or choice == 'S':
    print (num1 - num2)
    

if choice == 'w':
    print ("Invalid Option")
 '''   

for i in range(1,10):
    print(i)

var1 = "Again"
while var1 =="Again":
    print('running while loop')
    check =input(' Do you want the loop to continue? ')
    if check== 'N':
        break
