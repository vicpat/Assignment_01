                    ############# Question no 3 #############

#Write a Python program to count the number of even and odd numbers from a series of numbers.
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output :
#Number of even numbers : 4
#Number of odd numbers : 5


a = []
even_no = 0
odd_no = 0

size = int(input("Enter the Size: "))
print("Enter Numbers: ") 

for i in range(size):
  a.insert(i, int(input()))

for num in a:
    if num % 2 == 0:
        even_no += 1
    else:
        odd_no += 1
print("Number of even numbers : ", even_no)
print("Number of odd numbers : ", odd_no)

