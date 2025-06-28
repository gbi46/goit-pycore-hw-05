from fibonacci import caching_fibonacci

if __name__ == "__main__":
    print(" === Task 1. Caching fibonacci === ")

    # get the fibonacci function
    fib = caching_fibonacci()
    print("The value of fibonacci sequence with the index 15 is")

    # use the function for getting fibonacci numbers
    print(fib(15))
    print(fib(10))