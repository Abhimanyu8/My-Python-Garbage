#program to find palindrome:

n=int(input("Enter any number :"))
rev=0
k=n
while n!=0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print("The reverse of the number is :",rev)
if k==rev:
    print("its a palindrome .")
else:
    print("palindrome'nt")