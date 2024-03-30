# Program to print all prime numbers between 1 and a given number
n = int(input('Enter a number:'))
for num in range(2, n+1):
    for i in range(2, num):
        if num % i==0:
            break
    else:
        print(num)
        
#  program to find area and perimeter of rectangle
length= float(input('Enter length of rectangle: '))
width = float(input('Enter width of rectangle: '))
area = length * width
perimeter = 2 * (length + width)
print('Area =', area)
print('Perimter =', perimeter)