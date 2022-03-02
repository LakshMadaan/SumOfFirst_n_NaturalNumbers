# program to print the sum of first n natural numbers.
n=int(input('Enter the ending number: '))
total=0
for i in range(1,n+1,1):
    total+=i
print('The sum of first',n,'natural numbers is: ',total)