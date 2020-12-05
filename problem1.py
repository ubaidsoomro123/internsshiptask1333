def isPrime(n):
    isPrimeFlag = True
    for k in range(2,n):
        if (n%k==0):
            isPrimeFlag = False
            break
    return isPrimeFlag

def smpf(n):
    primeFactors = []
    for i in range(2,n+1):
        if (n%i==0):
            if (isPrime(i)):
               primeFactors.append(i)
    return min(primeFactors)        

def S(n):
    sum = 0
    for j in range(2,n+1):
        sum = sum + smpf(j)

    return sum

print("S(100) = %d",S(100))

print("S(1012) mod 9 = %d",S(1012)%9)
