            ############# Question no 1 #############

#Write a Python program to get the Fibonacci series between 0 to 50
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.

#Expected Output : 1 1 2 3 5 8 13 21 34

num = int(input("Enter the value of 'n': "))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()

