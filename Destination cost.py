'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
car = list(map(int, input().split()))
bus = list(map(int, input().split()))
half = int(n / 2)
carmin = []
busmin = []
for i in range(n):
    carmin.append(car[i] - bus[i])
    busmin.append(bus[i] - car[i])
carmin.sort()
busmin.sort()
x = sum(bus) + sum(carmin[:half])
y = sum(car) + sum(busmin[:half])
print(min(x, y))
