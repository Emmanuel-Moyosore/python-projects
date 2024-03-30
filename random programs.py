# Program to check if a even number is even or odd
num = int(input('Enter a number: '))
if num % 2 ==0:
    print(num, 'is even')
    
else:
    print(num, 'is odd')
    
    
# program that generates palindromic triangle
N = int(input()) # N<=9
for i in range(1,N+1):
    print(((10**i-1)//9)**2)
    
    
    
# Program that find factorial of a number
num1 = int(input('Enter a number: '))
factorial = 1
for i in range(1, num1+1):
    factorial  *= i
print('factorial of ', num1, 'is', factorial) 



# Program to print the Fibonacci sequence
n = int(input('Enter the number of terms: '))
a,b=0,1
if n <=0:
    print('Please enter a positive integer')
elif n==1:
    print('Fibonacci sequence',n,':',a)
else:
    print('Fibonacci Sequence: ')
    for i in range(n):
        print(a, end='')
        c = a + b
        a=b
        b=c
        break
        
        
