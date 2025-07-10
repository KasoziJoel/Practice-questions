

def is_prime():
    
    if n % 2 == 1:
        return True
        
    if n % 2 == 0:
        return False
        
n = float(input("Enter a number."))

if is_prime():
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")