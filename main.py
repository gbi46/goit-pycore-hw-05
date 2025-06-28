from fibonacci import caching_fibonacci

if __name__ == "__main__":
    print(" === Task 1. Caching fibonacci === ")
    fib = caching_fibonacci()
    print("The value of fibonacci sequence with the index 15 is")
    print(fib(15))