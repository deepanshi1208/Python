fib_cache={}
def fib(n):
    if n in fib_cache:       #if we have cached the value then return it.
        return fib_cache[n]

    #Compute nth terms
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n >2:
        value= fib(n-1)+fib(n-2)

    #cache the value and return it
    fib_cache[n]=value
    return value

for n in range (1,11):
    print(fib(n))