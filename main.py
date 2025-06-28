from fibonacci import caching_fibonacci
from generator_numbers import generator_numbers, sum_profit

if __name__ == "__main__":
    print(" === Task 1. Caching fibonacci === ")

    # get the fibonacci function
    fib = caching_fibonacci()
    print("The value of fibonacci sequence with the index 15 is")

    # use the function for getting fibonacci numbers
    print(fib(15))
    print(fib(10))

    print(" === Task 2. Print employee's total income === ")

    text = "The employee's total income consists of several parts: 1000.09 as the main income, supplemented by additional income of 27.49 and 324.02 dollars."
    # get the total profit from the sum_profit function
    total_income = sum_profit(text, generator_numbers)

    # print the total profit
    print(f"Total profit: {total_income}")