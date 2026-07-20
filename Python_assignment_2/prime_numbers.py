def checkPrime(n):
    count=0
    for i in range(2,n+1):
        count+=1
    if count==1:
        return True
    else:
        return False

def print_prime():
    for i in range(1,11):
        if checkPrime(i):
            print(i)    

print_prime()