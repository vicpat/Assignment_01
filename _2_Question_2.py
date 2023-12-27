                ############# Question no 2 #############

#Write a Python program that accepts a word from the user and reverse it.
#Sample Test Case
#Input : Edyoda
#output: adoydE

a = input("Enter your string: ")
b = ''
i = len(a) - 1

while i >= 0 :
    b = b + a[i]
    i -= 1
    
print("Original string = ", a)
print("Reversed string = ", b)