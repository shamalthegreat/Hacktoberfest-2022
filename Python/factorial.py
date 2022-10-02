#WAP to print the factoral of a given number
# 5! = 5*4*3*2*1


number = int(input("enter the number to find its factoral: "))

#now n! = n*(n-1)*(n-2)... until the common difference is less than the number

b = 1
for i in range (1, number + 1, 1):
    a = i
    b = a * b 
print(b)