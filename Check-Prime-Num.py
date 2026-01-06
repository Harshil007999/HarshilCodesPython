n1=int(input("Enter number 1:"))
if(n1 == 2):
    print(f"{n1} is a prime number")

prime = True
for i in range (3,n1 + 1):
    if n1 % i == 0:
            print(f"{n1} not a prime number")
            prime = False
            break
if prime == True:
    print(f"{n1} is a prime number")